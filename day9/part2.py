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
NUM_KNOTS = 10
knots = [Position(0,0) for _ in range(NUM_KNOTS)]
visited = {knots[-1]}

for line in input:
    instruction = line.strip().split(" ")
    head_direction = Direction[instruction[0]].value
    num_steps = int(instruction[1])

    for _ in range(num_steps):
        knots[0] = knots[0].move(head_direction)

        for n in range(1, len(knots)):
            knot_direction = knots[n-1].relative_position(knots[n])
        
            if abs(knot_direction.x) >= STRETCH or abs(knot_direction.y) >= STRETCH:
                knots[n] = knots[n].step_toward(knot_direction)
                if n == len(knots) - 1:
                    visited.add(knots[n])
            else:
                break

print (len(visited))

