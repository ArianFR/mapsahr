p1n = int(input("how many days?: "))
p1d = list(map(str, input("which weekdays?: ").split(" ")))
p2n = int(input("how many days?: "))
p2d =list(map(str, input("which weekdays?: ").split(" ")))
p3n = int(input("how many days?: "))
p3d = list(map(str, input("which weekdays?: ").split(" ")))

weekdays = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']


weekedit1 = [day for day in weekdays if day not in p1d]
weekedit2 = [day for day in weekedit1 if day not in p2d]
weekedit3 = [day for day in weekedit2 if day not in p3d]

len_we = len(weekedit3)

print(len_we)
print(weekedit3)