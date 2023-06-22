import os
import datetime
import glob
import json


def get_time_expfile(input_file):
    write = []
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
                        write.append(row)
                else:
                    write.append(row)
        return True

    path = input_file.split("/")
    dfs(path)

    max_time = max(datetime.datetime.fromtimestamp(os.path.getmtime(file)) for file in se)
    return max_time, "".join(write)


def main():
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
        time, write = get_time_expfile(file)
        data[file] = time.strftime("%Y-%m-%d %H:%M:%S")
        if timestamps.get(file, None) == data[file]:
            continue
        output_file = file.replace("src", "expansion", 1)
        with open(output_file, "w") as f:
            f.write(write)
        print(f"copy {file}")

    with open(json_path, "w") as fh:
        json.dump(data, fh, sort_keys=True, indent=0)


if __name__ == "__main__":
    main()
