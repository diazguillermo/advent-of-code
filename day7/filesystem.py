with open("day7/input.txt") as data:
    input = data.readlines()

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name: str = name
        self.size: int = size
    
    # def __eq__(self, __o: object) -> bool:
    #     return isinstance(object, File)

    def __eq__(self, __o: object) -> bool:
        return hash(__o) == hash(self)
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.size}"

class Directory:
    def __init__(self, name: str, prevDir: "Directory" = None) -> None:
        self.name = name
        self.prevDir = prevDir
        self.directories: set[Directory] = set()
        self.files: set[File] = set()
        self.size = 0

    def __eq__(self, __o: object) -> bool:
        return hash(__o) == hash(self)
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __str__(self) -> str:
        return self.name

    def addFile(self, file: File) -> None:
        self.files.add(file)
        self._updateDirSize(file.size)

    def addDirectory(self, dir: "Directory") -> None:
        self.directories.add(dir)

    # Updates the directory's size and trickles the update up to its parent recursively
    def _updateDirSize(self, addedSize: int) -> None:
        self.size += int(addedSize)
        if self.prevDir:
            self.prevDir._updateDirSize(addedSize)


assert input[0].startswith("$ cd")
rootDir = Directory(input[0][5:].strip())

currentDir: Directory = rootDir
lineNum = 1
currentLine: str = input[1]

while lineNum < len(input):
    # executing command (we always start with a command)
    currentLine = input[lineNum].rstrip()
    command = currentLine[2:].split()
    commandName = command[0]

    if commandName == "cd":
        arg = command[1]
        if arg == "..":
            assert currentDir.prevDir, "trying to escape out of root directory (no previous directory available)"
            currentDir = currentDir.prevDir
        else:
            assert arg in currentDir.directories, f" cd: {arg}: No such file or directory"
            for directory in currentDir.directories:
                if directory.name == arg:
                    currentDir = directory
                    break
        lineNum += 1

    elif commandName == "ls":
        lineNum += 1
        
        while lineNum < len(input):
            entry = input[lineNum].strip()
            if not entry.startswith("$"):
                # viewing new file/directory
                if entry.startswith("dir"):
                    dirName = entry.split(" ")[1]
                    newDirectory = Directory(dirName, currentDir)
                    currentDir.addDirectory(newDirectory)
                else:
                    fileSize, fileName = entry.split(" ")
                    newFile = File(fileName, fileSize)
                    currentDir.addFile(newFile)
                lineNum += 1
            else: 
                break

def getFileSystemRoot() -> Directory:
    return rootDir