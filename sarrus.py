from typing import List


def wyznacznik(matrix):
    det = matrix[0][0]*matrix[1][1]*matrix[2][2] + \
          matrix[0][1]*matrix[1][2]*matrix[2][0] + \
          matrix[0][2]*matrix[1][0]*matrix[2][1] - \
          matrix[0][2]*matrix[1][1]*matrix[2][0] - \
          matrix[0][1]*matrix[1][0]*matrix[2][2] - \
          matrix[0][0]*matrix[1][2]*matrix[2][1]

    return det

def crop_matrix(matrix_src: List, column_number: int):
    matrix_for_wyznacznik = []
    for full_row in matrix_src:
        cropped_row = full_row.copy()
        del cropped_row[column_number]
        matrix_for_wyznacznik.append(cropped_row)

    return matrix_for_wyznacznik

# matrix_src = [[1, -3, 1, -2],
#              [-2, 7, -6, 13],
#              [2, -9, 3, -9]]

matrix_src = [[2, -3, 3, 17],
             [1, 1, 1, 2],
             [3, -1, -1, 2]]

matrix_for_x_wyl = crop_matrix(matrix_src, 0)
matrix_for_y_wyl = crop_matrix(matrix_src, 1)
matrix_for_z_wyl = crop_matrix(matrix_src, 2)
matrix_for_w_wyl = crop_matrix(matrix_src, 3)

wyznacznik_x = wyznacznik(matrix_for_x_wyl)
wyznacznik_y = wyznacznik(matrix_for_y_wyl)
wyznacznik_z = wyznacznik(matrix_for_z_wyl)
wyznacznik_w = wyznacznik(matrix_for_w_wyl)

print(f"wyznacznik x = {wyznacznik_x}")
print(f"wyznacznik y = {wyznacznik_y}")
print(f"wyznacznik z = {wyznacznik_z}")
print(f"wyznacznik w = {wyznacznik_w}")

print(f"x = {wyznacznik_x}/{wyznacznik_w} = {wyznacznik_x/wyznacznik_w}")
print(f"y = {wyznacznik_y}/{wyznacznik_w} = {wyznacznik_y/wyznacznik_w}")
print(f"z = {wyznacznik_z}/{wyznacznik_w} = {wyznacznik_z/wyznacznik_w}")