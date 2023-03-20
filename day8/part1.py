with open("day8/input.txt") as data:
    input = data.readlines()

tree_map = []
for line in input:
    tree_map.append([int(height) for height in list(line.strip())])

def rotate_2d_array(arr):
    res = list(zip(*arr[::-1]))
    return [list(row) for row in res]

num_visible = 0
result_map = [list(row) for row in tree_map]
for _ in range(4):
    for r, trees in enumerate(tree_map):
        clearing = -1
        for c, tree_height in enumerate(trees):
            if tree_height > clearing:
                clearing = tree_height
                if result_map[r][c] != -1:
                    num_visible += 1
                    result_map[r][c] = -1

    tree_map = rotate_2d_array(tree_map)
    result_map = rotate_2d_array(result_map)

print (num_visible)