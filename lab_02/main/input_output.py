from tabulate import *

def read_file(name_file):
    
    file = open(name_file, "r")

    data = []

    for i in file:
        data.append(list(map(float, i.split())))


    file.close()

    return data

def create_table(data):
    
    lenl = len(data)

    col_names = ["x"]
    for i in range(lenl):   
        col_names.append("y" + "'" * i)


    print(tabulate(data, headers = col_names, tablefmt = "fancy_grid"))
    print()
    