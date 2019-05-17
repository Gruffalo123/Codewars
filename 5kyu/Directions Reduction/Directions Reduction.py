def dirReduc(arr):
    opposite = {'EAST': 'WEST', 'NORTH': 'SOUTH', 'WEST': 'EAST', 'SOUTH': 'NORTH'}
    new_arr = []
    for item in arr:
        if new_arr and new_arr[-1] == opposite[item]:
            new_arr.pop()
        else:
            new_arr.append(item)
    return new_arr


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(a))
    print(dirReduc(u))