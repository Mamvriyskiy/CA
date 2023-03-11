"""
    Чтение, вывод информации
"""

from tabulate import *

def read_element():
    n = 0
    x = 0
    while True:
        try:
            n = int(input("Введите n: ")) 
            x = float(input("Введите x: "))
            break
        except ValueError:
            print("Данные введены неверно.")

    return n, x

def read_file(name_file):
    
    file = open(name_file, "r")

    data = []

    for i in file:
        data.append(i.split())

    file.close()

    return data


def create_table(data):

    lenl = len(data)

    col_names = ["x"]
    for i in range(lenl):   
        col_names.append("y" + "'" * i)


    print(tabulate(data, headers = col_names, tablefmt = "fancy_grid"))
    print()


 
