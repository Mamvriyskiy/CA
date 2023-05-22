from Table import Table
import calcAlg as ca

fileNameOne = "../data/dataOne.csv"
fileNameTwo = "../data/new.csv"

def inputTableData(dim: int):

    amountX = int(input("\nКоличество строк: "))
    xStart = int(input("Начальное значение x: "))
    xEnd = int(input("Конечное значение x: "))

    if dim == 1:
        return [amountX], xStart, xEnd
    else:
        amountY = int(input("\nКоличество строк: "))
        yStart = int(input("Начальное значение y: "))
        yEnd = int(input("Конечное значение y: "))

        return [amountX, amountY], xStart, xEnd, yStart, yEnd

def inputPolyPow():
    power = int(input("\nСтепень полинома: "))

    return power

def changeWeights(myTable: Table):

    # msg = "\n1. All ones\n" \
    #       "2. By number\n"
    
    # print(msg)

    # opt = int(input("Выберите пункт меню: "))

    num = None
    weight = None

    # if opt == 2:
    num = int(input("Введите число: "))
    weight = float(input("Введите вес: "))

    

    myTable.editWeight(1, num, weight)



oneDimTable = Table()
twoDimTable = Table()

# opts = "\n#Одномерная апроксимация\n" \
#         "1. Создать таблицу\n" \
#         "2. Чтение таблицы из файла\n" \
#         "3. Вывод таблицы\n" \
#         "4. Изменить вес\n" \
#         "5. Построить график\n" \
#         "\n#Двумерная апроксимация\n" \
#         "6. Cоздать таблицу\n" \
#         "7. Чтение таблицы из файла\n" \
#         "8. Вывод таблицы\n" \
#         "9. Изменить вес\n" \
#         "10. Построить график\n" \
#         "\n#Решение дифф уравнения\n" \
#         "11. Решение\n" \
#         "\n0. Exit\n" \

opts = "\n#Одномерная апроксимация\n" \
        "1. Создать таблицу\n" \
        "2. Чтение таблицы из файла\n" \
        "3. Вывод таблицы\n" \
        "4. Построить график\n" \
        "\n#Двумерная апроксимация\n" \
        "5. Cоздать таблицу\n" \
        "6. Чтение таблицы из файла\n" \
        "7. Вывод таблицы\n" \
        "8. Построить график\n" \
        "\n#Решение дифф уравнения\n" \
        "9. Решение\n" \
        "\n0. Exit\n" \


def menu():
            
    print(opts)
            
    opt = int(input("Выберите пункт меню: "))

    if opt == 0:
        return
    else:
        if opt == 1:
            amount, xStart, xEnd = inputTableData(1)
            oneDimTable.generateTable(ca.funcA, amount, [xStart, xEnd])
        elif opt == 2:
            oneDimTable.readFromFile(fileNameOne)
        elif opt == 3:
            oneDimTable.printTable()
        # elif opt == 4:
        #     changeWeights(oneDimTable)
        elif opt == 4:
            power = inputPolyPow()
            koefs1 = ca.solveSystemOne(oneDimTable, 1)
            koefs2 = ca.solveSystemOne(oneDimTable, 4)

            koefsN = ca.solveSystemOne(oneDimTable, power)
            oneDimTable.drawGraphics(koefs1, koefs2, koefsN)

            # if power < len(oneDimTable.x):
            #     koefsN = ca.solveSystemOne(oneDimTable, power)
            #     oneDimTable.drawGraphics(koefs1, koefs2, koefsN)
            # else:
            #     print("Not enough points for {}-power polynom!".format(power))
            #     oneDimTable.drawGraphics(koefs1, koefs2)

        elif opt == 5:
            amount, xStart, xEnd, yStart, yEnd = inputTableData(2)
            twoDimTable.generateTable(ca.funcB, amount, [xStart, xEnd, yStart, yEnd])
        elif opt == 6:
            twoDimTable.readFromFile(fileNameTwo)
        elif opt == 7:
            twoDimTable.printTable()
        # elif opt == 8:
        #     changeWeights(twoDimTable)
        elif opt == 8:
            power = inputPolyPow()

            if power != 1 and power != 2:
                print("Incorrect power for polynom")
            else:
                koefs = ca.solveSystemTwo(twoDimTable, power)
                twoDimTable.drawGraphics(koefs)
        elif opt == 9:
            ca.solveODE()

        menu()

menu()