import math
from filesystem import Directory, File, getFileSystemRoot

THRESHOLD = 100000
result = 0
queue = [getFileSystemRoot()]

while queue:
    dir = queue.pop()
    if dir.size <= THRESHOLD:
        result += dir.size

    queue.extend(list(dir.directories))

# before calculating size during file system creation:
def dirsWithinThreshold(dir: Directory, threshold: int):
    totalSize: int = 0

    for file in dir.files:
        totalSize += int(file.size)

    for subDir in dir.directories:
        totalSize += dirsWithinThreshold(subDir, threshold)

    if totalSize <= threshold:
        global result
        result += totalSize

    return totalSize

# dirsWithinThreshold(getFileSystemRoot(), 100000)
print (result)
