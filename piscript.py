import os
import json
import subprocess
import sys

files = sys.argv[1].split()
severity = sys.argv[2]

results = {}

for f in files:
    try:
        subprocess.run(
            ["verilator", "--lint-only", f],
            check=True,
            capture_output=True,
            text=True
        )
        results[f] = "PASS"

    except subprocess.CalledProcessError:
        results[f] = "FAIL"

print(json.dumps(results, indent=2))

with open("result.json", "w") as fp:
    json.dump(results, fp)

with open(
    os.environ["GITHUB_OUTPUT"],
    "a"
) as out:
    out.write(
        f"result={json.dumps(results)}\n"
    )
