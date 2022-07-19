def generate(numRows):
    triangle = [[1]]
    for outer_position in range(numRows - 1):  # (numRows - 1) because we created the first row.
        temporary_array = [0] + triangle[-1] + [0]  # [-1] looks at the last item on the list.
        new_row = []
        for inner_position in range(len(triangle[-1]) + 1):  # Len of previous row + 1 because each row increases by 1.
            new_row.append(temporary_array[inner_position] + temporary_array[inner_position + 1])
        triangle.append(new_row)
    return triangle
