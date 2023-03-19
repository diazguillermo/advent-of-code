from filesystem import getFileSystemRoot

TOTAL_SPACE  = 70000000
SPACE_NEEDED = 30000000
rootDir = getFileSystemRoot()

smallestToFree = rootDir.size
startingFreeSpace = TOTAL_SPACE - rootDir.size
target = SPACE_NEEDED - startingFreeSpace

queue = list(rootDir.directories)

while queue:
    dir = queue.pop()
    if dir.size >= target:
        smallestToFree = min(smallestToFree, dir.size)
        queue.extend(list(dir.directories))
        
print (smallestToFree)