from enum import Enum

with open("day9/input.txt") as data:
    input = data.readlines()

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Position) and self.x == __o.x and self.y == __o.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def move(self, pos: "Position") -> "Position":
        return Position(self.x + pos.x, self.y + pos.y)

    def relative_position(self, pos: "Position") -> "Position":
        return Position(self.x - pos.x, self.y - pos.y)
    
    def step_toward(self, pos: "Position") -> "Position":
        x = pos.x/abs(pos.x) if pos.x else 0
        y = pos.y/abs(pos.y) if pos.y else 0
        return self.move(Position(x, y))


class Direction(Enum):
    L = Position(-1,0)
    R = Position(1, 0)
    U = Position(0, 1)
    D = Position(0,-1)


STRETCH = 2
head = Position(0,0)
tail = Position(0,0)
visited = {tail}

for line in input:
    instruction = line.strip().split(" ")
    head_direction = Direction[instruction[0]].value
    num_steps = int(instruction[1])

    for _ in range(num_steps):
        head = head.move(head_direction)
        tail_direction = head.relative_position(tail)
        
        if abs(tail_direction.x) >= STRETCH or abs(tail_direction.y) >= STRETCH:
            tail = tail.step_toward(tail_direction)
            visited.add(tail)

print (len(visited))

