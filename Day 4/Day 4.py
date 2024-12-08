import numpy as np
import time


space = "."
obstacle = "#"
guard_path = "X"
guard = {"^": (0, 1),
         ">": (-1, 0),
         "v": (0, -1),
         "<": (1, 0)
         }

file = "Day 4 Input.txt"

with open(file) as f:
    data = []
    for line in f:
        line_data = list(line.replace("\n", ""))
        data.append(line_data)
    data_array = np.array(data)

print(data_array, data_array.shape)

time.sleep(5)
while True:
    try:
        guard_position = None
        guard_direction = None

        for char in guard:
            if char in data_array:
                guard_position = np.where(data_array == char)
                guard_direction = char

        guard_x = int(guard_position[1][0])
        guard_y = int(guard_position[0][0])
        guard_position = (guard_x, guard_y)

        if guard_position[0] - guard[guard_direction][0] < 0:
            raise IndexError
        elif guard_position[1] - guard[guard_direction][1] < 0:
            raise IndexError

        new_space = np.subtract(guard_position, guard[guard_direction])
        new_space_data = data_array[new_space[1]][new_space[0]]


        #print(new_space_data, obstacle)


        if new_space_data != obstacle:
            data_array[new_space[1]][new_space[0]] = guard_direction
            data_array[guard_position[1]][guard_position[0]] = guard_path
            new_space = guard_direction

        else:
            path_index = list(guard).index(guard_direction)

            try:
                guard_direction = list(guard)[path_index+1]
            except IndexError:
                path_index = 0
                guard_direction = list(guard)[path_index]


            data_array[guard_position[1]][guard_position[0]] = guard_direction
            new_space = guard_direction

            if guard_position[1] < 0 or guard_position[0] < 0:
                raise IndexError

        #print(data_array)
        #time.sleep(0.5)

    except IndexError:
        np.set_printoptions(threshold=np.inf,linewidth=np.inf)
        with open("output.txt", 'w') as f:
            f.write(np.array2string(data_array, separator=' '))

        test = np.count_nonzero(data_array == guard_path)
        print(f"{test + 1} Unique Locations visited")
        break




