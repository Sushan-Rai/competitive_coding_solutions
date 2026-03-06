import subprocess
import matplotlib.pyplot as plt
from collections import defaultdict

# get git file changes
log = subprocess.check_output(
    ["git", "log", "--name-only", "--pretty=format:"]
).decode()

folders = defaultdict(int)

for line in log.split("\n"):
    if "/" in line:
        folder = line.split("/")[0]
        folders[folder] += 1

# plotting
names = list(folders.keys())
counts = list(folders.values())

plt.bar(names, counts)
plt.title("Commits per Folder")
plt.xlabel("Folder")
plt.ylabel("Commits")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("commit_graph.png")