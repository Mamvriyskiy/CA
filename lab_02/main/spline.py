import newton_method

def search_index_in_list(data, x):
    size = len(data)
    index = 1

    while index < size and data[index] < x:
        index += 1

    return index - 1

def calcAValues(list_y):
    list_a = list()
    for i in range(len(list_y) - 1):
        list_a.append(list_y[i])

    return list_a

def fi(y1, y2, y3, h1, h2):
    return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)

def ksi(ksi1, h1, h2):
    return - h1 / (h2 * ksi1 + 2 * (h2 + h1))


def teta(fi, teta_i, ksi_i, h1, h2):
    return (fi - h1 * teta_i) / (h1 * ksi_i + 2 * (h2 + h1))

def B(y1, y2, c1, c2, hi):
    return (y2 - y1) / hi - (hi * (c2 + 2 * c1) / 3)


def D(c1, c2, hi):
    return (c1 - c2) / (3 * hi)

    
def calcCValues(xValues, yValues, start, end):
    sizeX = len(xValues)

    cValues = [0] * (sizeX - 1)
    cValues[0] = start
    cValues[1] = end
    if start == 0 and end == 0:
        ksiValues = [0, 0]
        tetaValues = [0, 0]
    elif start == 0:
        ksiValues = [0, end / 2]
        tetaValues = [0, end / 2]
    else:
        ksiValues = [start / 2, end / 2]
        tetaValues = [start / 2, end / 2]

    for i in range(2, sizeX):
        h2 = xValues[i] - xValues[i - 1]
        h1 = xValues[i - 1] - xValues[i - 2]

        fiCur = fi(yValues[i - 2], yValues[i - 1], yValues[i], h1, h2)
        ksiCur = ksi(ksiValues[i - 1], h1, h2)
        tetaCur = teta(fiCur, tetaValues[i - 1], ksiValues[i - 1], h1, h2)

        ksiValues.append(ksiCur)
        tetaValues.append(tetaCur)

    cValues[-1] = tetaValues[-1]

    for i in range(sizeX - 2, 0, -1):
        cValues[i - 1] = cValues[i] * ksiValues[i] + tetaValues[i]

    return cValues

def calcBValues(xValues, yValues, cValues):
    bValues = list()
    for i in range(1, len(xValues) - 1):
        hi = xValues[i] - xValues[i - 1]
        bValues.append(B(yValues[i - 1], yValues[i], cValues[i - 1], cValues[i], hi))

    hi = xValues[-1] - xValues[-2]
    bValues.append(B(yValues[-2], yValues[-1], 0, cValues[-1], hi))

    return bValues


def calcDValues(xValues, cValues):
    dValues = []

    size = len(xValues)

    for i in range(1, size - 1):
        hi = xValues[i] - xValues[i - 1]
        dValues.append(D(cValues[i], cValues[i - 1], hi))

    hi = xValues[-1] - xValues[-2]
    dValues.append(D(0, cValues[-1], hi))

    return dValues

def calculateCoefsSpline(xValues, yValues, start, end):
    aValues = calcAValues(yValues)
    cValues = calcCValues(xValues, yValues, start, end)
    bValues = calcBValues(xValues, yValues, cValues)
    dValues = calcDValues(xValues, cValues)

    return aValues, bValues, cValues, dValues

def countPolynom(x, xValues, index, coefs):
    h = x - xValues[index]
    y = 0

    for i in range(4):
        y += coefs[i][index] * (h ** i)

    return y

def spline(table, x, start, end):
    xValues = [i[0] for i in table]
    yValues = [i[1] for i in table]


    coeffs = calculateCoefsSpline(xValues, yValues, start, end)

    index = search_index_in_list(xValues, x)

    y = countPolynom(x, xValues, index, coeffs)

    return y
