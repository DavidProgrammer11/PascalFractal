from math import factorial

#Con sumas

def binomio(n, k, mode=0):
    result = (factorial(n)//(factorial(k)*(factorial(n - k))))
    if mode == 0:
        return result
    elif mode == 1:
        result = result%5
        if result == 0:
            return " "
        elif result == 1:
            return "+"
        elif result == 2:
            return "Ç"
        elif result == 3:
            return "´´"
        else:
            return 1

def generate_diagonal(n, l):
    result_list = []
    if n >= 0 and l >= 0:
        for i in range(l):
            result_list.append(binomio(n+i,i,mode=0))
    return result_list

triangle = []
def create_triangulo(x,mode=0):
    new_list = []
    for i in range(x + 1):
        new_list.append(binomio(x, i,mode))
    triangle.append(new_list)

def create(rows,mode=0):
    """Esta función crea las filas del triangulo
    y las mete en una lista
    mode 0 -> triangulo de pascal
    mode 1 -> triangulo de sierpinsky
    """
    for i in range(rows+1):
        create_triangulo(i,mode)
    return triangle

def draw_triangle(row_list):
    global triangle
    max_width = len("   ".join(map(str, row_list[-1])))
    for i in range(len(row_list)-1):
        fila_str = "  ".join(map(str, row_list[i]))
        num_sep = (max_width - len(fila_str)) // 2
        print(" " * num_sep + fila_str)
    triangle = []

# Prueba
print(generate_diagonal(5,6))
draw_triangle(create(30,0))
draw_triangle(create(70,1))
