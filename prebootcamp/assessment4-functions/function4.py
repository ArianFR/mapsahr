def khayam_pascal(n):
  triangle = []
  for i in range(n):
    row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    triangle.append(row)
  return triangle

n = int(input('how many rows?: '))

triangle = khayam_pascal(n)

for row in triangle:
    row = ' '.join(map(str, row))
    print(row)
