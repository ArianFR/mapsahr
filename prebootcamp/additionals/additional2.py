n, m = map(int, input('how many rows and columns?: ').split())

count = 0

while n > 0:
    n -= 1
    sky_map = input()
    for i in sky_map:
        if i == '*':
            count += 1
print(count)

