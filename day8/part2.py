with open("day8/input.txt") as data:
    input = data.readlines()

tree_map = []
for line in input:
    tree_map.append([int(height) for height in list(line.strip())])

def rotate_2d_array(arr):
    res = list(zip(*arr[::-1]))
    return [list(row) for row in res]

MAX_HEIGHT = 10
result_map = [[1]*len(row) for row in tree_map]
for _ in range(4):
    for row, trees in enumerate(tree_map):
        # heights are 0-9 -> len(dict) <= 10
        last_seen = dict()

        for col, tree_height in enumerate(trees):
            # viewing distance to left edge
            viewing_distance = col

            # look for last seen tree of heights >= tree_height and get proper viewing distance if tree exists
            left_bounds = last_seen.keys() & set(range(tree_height, MAX_HEIGHT + 1))
            if left_bounds:
                viewing_distance -= max([last_seen[height] for height in left_bounds])

            last_seen[tree_height] = col

            result_map[row][col] *= viewing_distance

    tree_map = rotate_2d_array(tree_map)
    result_map = rotate_2d_array(result_map)


print (max([scenic_score for row in result_map for scenic_score in row]))