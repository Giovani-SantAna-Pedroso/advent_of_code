import sys

file_pah = sys.argv[1]

def check_triangle(arr):
    max_val =max(arr)
    arr.remove(max_val)
    return sum(arr) > max_val

with open(file_pah, 'r') as file:
    amount_triangles = 0
    amount_triangles_col = 0
    tri_col0 =[]
    tri_col1 =[]
    tri_col2 =[]
    
    for line in file:
        line = list(map(int, line.strip().split()))
        tri_col0.append(line[0])
        tri_col1.append(line[1])
        tri_col2.append(line[2])

        amount_triangles += 1 if check_triangle(line) else 0
    tri_col = tri_col0 + tri_col1 + tri_col2


    for i in range(0, len(tri_col), 3):
        amount_triangles_col += 1 if check_triangle(tri_col[i:i+3]) else 0

    print("AnsA: ", amount_triangles)
    print("AnsB: ", amount_triangles_col)
