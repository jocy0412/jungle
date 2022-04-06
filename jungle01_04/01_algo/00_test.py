import sys
# a,b = map(str,sys.stdin.readline().split())

# # print(f'a는 {a}, b는 {b}')

# reverse_a = ''
# reverse_b = ''
# compare = []

# for i in a :
#     reverse_a = i + reverse_a

# for i in b :
#     reverse_b = i + reverse_b

# compare.append(reverse_a)
# compare.append(reverse_b)

data = list(map(str,sys.stdin.readline().split()))

# print(f'a는 {a}, b는 {b}')

reverse_data = []
for i in range(len(data)) :
    reverse_number = ''
    for j in data[i] :
        reverse_number = j + reverse_number
    reverse_data.append(reverse_number)

print(type(reverse_data[0]))
print(type(reverse_data[1]))
print(max(reverse_data))
