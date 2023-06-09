from typing import List



def wyznacznik(matrix):
    det = matrix[0][0]*matrix[1][1]*matrix[2][2] + \
          matrix[0][1]*matrix[1][2]*matrix[2][0] + \
          matrix[0][2]*matrix[1][0]*matrix[2][1] - \
          matrix[0][2]*matrix[1][1]*matrix[2][0] - \
          matrix[0][1]*matrix[1][0]*matrix[2][2] - \
          matrix[0][0]*matrix[1][2]*matrix[2][1]

    print(
        f"({matrix[0][0]*matrix[1][1]*matrix[2][2]} + "
        f"{matrix[0][1]*matrix[1][2]*matrix[2][0]} + "
        f"{matrix[0][2]*matrix[1][0]*matrix[2][1]})"
        f"  -  "
        f"({matrix[0][2]*matrix[1][1]*matrix[2][0]} + "
        f"{matrix[0][1]*matrix[1][0]*matrix[2][2]} + "
        f"{matrix[0][0]*matrix[1][2]*matrix[2][1]})"
    )

    return det

def crop_matrix(matrix_src: List, column_number: int):
    matrix_for_wyznacznik = []
    for full_row in matrix_src:
        cropped_row = full_row.copy()
        if column_number < 3:
            cropped_row[column_number], cropped_row[3] = cropped_row[3], cropped_row[column_number]

        del cropped_row[3]
        matrix_for_wyznacznik.append(cropped_row)

    return matrix_for_wyznacznik

def determinant_laplace(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

def chio_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def get_cofactor(matrix, row, col):
        submatrix = [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]
        return chio_determinant(submatrix)

    return sum((-1) ** col * matrix[0][col] * get_cofactor(matrix, 0, col) for col in range(len(matrix)))


matrix_src = [[3, -1, 1, 2],
             [2, 4, -1, 1],
             [1, 1, 1, 3]]

matrix_for_x_wyl = crop_matrix(matrix_src, 0)
print(f"Matrix x: {matrix_for_x_wyl}")
matrix_for_y_wyl = crop_matrix(matrix_src, 1)
print(f"Matrix y: {matrix_for_y_wyl}")
matrix_for_z_wyl = crop_matrix(matrix_src, 2)
print(f"Matrix z : {matrix_for_z_wyl}")
matrix_for_w_wyl = crop_matrix(matrix_src, 3)
print(f"Matrix w: {matrix_for_w_wyl}")

wyznacznik_w = wyznacznik(matrix_for_w_wyl)
wyznacznik_x = wyznacznik(matrix_for_x_wyl)
wyznacznik_y = wyznacznik(matrix_for_y_wyl)
wyznacznik_z = wyznacznik(matrix_for_z_wyl)

determinant_laplace_w = determinant_laplace(matrix_for_w_wyl)
determinant_laplace_x = determinant_laplace(matrix_for_x_wyl)
determinant_laplace_y = determinant_laplace(matrix_for_y_wyl)
determinant_laplace_z = determinant_laplace(matrix_for_z_wyl)

determinant_chio_w = chio_determinant(matrix_for_w_wyl)
determinant_chio_x = chio_determinant(matrix_for_x_wyl)
determinant_chio_y = chio_determinant(matrix_for_y_wyl)
determinant_chio_z = chio_determinant(matrix_for_z_wyl)




print(f"wyznacznik w = {wyznacznik_w}; determinant laplace w = {determinant_laplace_w}; determinant chio w = {determinant_chio_w}")
print(f"wyznacznik x = {wyznacznik_x}; determinant laplace x = {determinant_laplace_x}; determinant chio x = {determinant_chio_x}")
print(f"wyznacznik y = {wyznacznik_y}; determinant laplace y = {determinant_laplace_y}; determinant chio y = {determinant_chio_y}")
print(f"wyznacznik z = {wyznacznik_z}; determinant laplace z = {determinant_laplace_z}; determinant chio z = {determinant_chio_z}")


print(f"x = {wyznacznik_x}/{wyznacznik_w} = {wyznacznik_x/wyznacznik_w}")
print(f"y = {wyznacznik_y}/{wyznacznik_w} = {wyznacznik_y/wyznacznik_w}")
print(f"z = {wyznacznik_z}/{wyznacznik_w} = {wyznacznik_z/wyznacznik_w}")