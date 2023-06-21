import os
import datetime
import glob
import json


def main(input_file, output_file):
    with open(output_file, "w") as f:
        se = set()

        def dfs(path):
            filename = "/".join(path)
            if not os.path.exists(filename):
                return False
            if filename in se:
                return
            se.add(filename)
            path.pop()
            with open(filename, "r") as f2:
                for row in f2:
                    if row[:4] == "from":
                        P = row.split()[1].split(".")
                        P[-1] += ".py"
                        if not dfs(P):
                            f.write(row)
                    else:
                        f.write(row)
            return True

        path = input_file.split("/")
        dfs(path)


if __name__ == "__main__":
    json_path = "src/timestamps.json"
    timestamps = {}
    if os.path.exists(json_path):
        with open(json_path) as fh:
            data = json.load(fh)
        for path, timestamp in data.items():
            if path == "~" and timestamp == "dummy":  # for backward compatibility
                continue
            timestamps[path] = timestamp
    data = {}
    for file in glob.glob("src/**/*.py", recursive=True):
        timestamp = os.path.getmtime(file)
        modifiedtime = datetime.datetime.fromtimestamp(timestamp)
        data[file] = modifiedtime.strftime("%Y-%m-%d %H:%M:%S")
        if timestamps.get(file, None) == data[file]:
            continue
        output_file = file.replace("src", "expansion", 1)
        main(file, output_file)
        print(f"copy {file}")

    with open(json_path, "w") as fh:
        json.dump(data, fh, sort_keys=True, indent=0)
