from collections import deque
import os

with open("day6/input.txt") as input:
    buffer = iter(input.readline())

MARKER_SIZE = 14

signal = next(buffer, None)
markerLocation = 1
lastReceived = deque()
while signal:
    if len(lastReceived) == MARKER_SIZE:
        lastReceived.popleft()

    lastReceived.append(signal)
    signal = next(buffer, None)

    if len(lastReceived) == MARKER_SIZE and len(set(lastReceived)) == len(lastReceived):
        break

    markerLocation += 1

print(markerLocation)