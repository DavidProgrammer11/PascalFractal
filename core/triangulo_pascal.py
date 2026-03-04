from math import factorial

# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x-1)


def binomio(n, k):
    return (factorial(n)/(factorial(k)*(factorial(n - k))))

k = 4
triag = []

# for i in range(0, k+1):
#     print(f"{binomio(4, i): ^{k*20}}")

triangle = []
def create_triangulo(x):
    new_list = []
    for i in range(x + 1):
        new_list.append(binomio(x, i))
    triangle.append(new_list)

def create(x):
    for i in range(x):
        create_triangulo(i)
    return triangle

for i in create(20):
    print(" " * (78-len(str(i))//2), end = "")
    print(i)
# formateo de cadenas

print(binomio(4,2))