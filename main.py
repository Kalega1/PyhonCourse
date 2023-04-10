
# def power(A, B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     else:
#         return A * power(A, B-1)

# A = 3
# B = 5
# result = power(A, B)
# print(result) # Output: 243

# A = 2
# B = 3
# result = power(A, B)
# print(result) # Output 8


########################


def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

a = 2
b = 2
result = sum(a, b)
print(result) # Output: 4




