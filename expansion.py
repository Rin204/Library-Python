import os
import sys


def main(input_file, output_file):
    with open(output_file, "w") as f:
        se = set()

        def dfs(path):
            filename = "/".join(path)
            if not os.path.exists(filename):
                return False
            if filename in se:
                return True
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
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
