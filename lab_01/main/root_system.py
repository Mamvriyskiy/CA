import newton
import input_output
import general_func

def system_table():
    table = []

    file = open("../data/data_a.txt", "r")

    for line in file:
        row = list(map(float, line.split()))
        table.append([row[1], row[0], None])

    file.close()

    file = open("../data/data_b.txt")

    for line in file:
        row = list(map(float, line.split()))
        table.append([row[0], None, row[1]])

    table.sort()


    file.close()

    return table

def get_y_index(table, y):
    diff = abs(table[0][1] - y)
    index = 0

    for i in range(len(table)):
        if abs(table[i][1] - y) < diff:
            diff = abs(table[i][1] - y)
            index = i

    return index

def create_system(table):
    system_a = []
    system_b = []
    for i in range(len(table)):
        if table[i][1] is not None:
            system_a.append([table[i][0], table[i][1]])
        else:
            system_b.append([table[i][0], table[i][2]])

    return system_a, system_b

def subtract_table(table):
    new_table = []

    for i in range(len(table)):
        new_table.append([table[i][0], table[i][1] - table[i][2], None])

    return new_table

def change_axis(table):
    for i in range(len(table)):
        table[i][0], table[i][1] = table[i][1], table[i][0]

    return table

def search_newton_root(table, n):
    root_table = []
    for i in table:
        root_table.append([i[0], i[1]])  # заполняем таблицу стартовыми координатами

    root_table = change_axis(root_table)
    root_table.sort()
    newton.create_interpolating_newton_polinom(root_table, n)


    input_output.create_table(root_table)
    print("Вычисленный корень: {:.5f}\n".format(general_func.calculate_polinom(root_table, 0)))

def root_system_ex(n):
    table = system_table()
    
    system_a, system_b = create_system(table)

    newton.NewtonMethod(system_a, len(system_a) - 1) 
    newton.NewtonMethod(system_b, len(system_b) - 1)

    for i in range(len(table)):
        if table[i][2] is None:
            table[i][2] = general_func.calculate_polinom(system_b, table[i][0])
        if table[i][1] is None:
            table[i][1] = general_func.calculate_polinom(system_a, table[i][0])

    table = subtract_table(table)

    index = get_y_index(table, 0)

    border_one, border_two = general_func.create_border(table, n, table[index][0])

    table = table[border_one:border_two]

    search_newton_root(table, n)


    # print("Root: ", root)


