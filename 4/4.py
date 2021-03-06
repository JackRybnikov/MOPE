import numpy as np
import scipy.stats
from random import randint
from copy import deepcopy
import lab666 as lalala
import math

x1min = 15
x1max = 45
x2min = -35
x2max = 15
x3min = -35
x3max = 5
y_min = 200+(x1min+x2min+x3min)/3
y_max = 200+(x1max+x2max+x3max)/3
N = 8
q = 0.05
print("y=b0+b1*x1+b2*x2+b3*x3+b12*x1*x2+b13*x1*x3+b23*x2*x3+b123*x1*x2*x3+b11*x1^2+b22*x2^2+b33*x3^2")
x_array = np.array([[x1max, x2max, x3max, x1max * x2max, x1max * x3max, x2max * x3max, x1max * x2max * x3max],
                    [x1max, x2max, x3min, x1max * x2max, x1max * x3min, x2max * x3min, x1max * x2max * x3min],
                    [x1max, x2min, x3max, x1max * x2min, x1max * x3max, x2min * x3max, x1max * x2min * x3max],
                    [x1max, x2min, x3min, x1max * x2min, x1max * x3min, x2min * x3min, x1max * x2min * x3min],
                    [x1min, x2max, x3max, x1min * x2max, x1min * x3max, x2max * x3max, x1min * x2max * x3max],
                    [x1min, x2max, x3min, x1min * x2max, x1min * x3min, x2max * x3min, x1min * x2max * x3min],
                    [x1min, x2min, x3max, x1min * x2min, x1min * x3max, x2min * x3max, x1min * x2min * x3max],
                    [x1min, x2min, x3min, x1min * x2min, x1min * x3min, x2min * x3min, x1min * x2min * x3min]])

y_array = np.array([[210, 215, 215],
                    [210, 215, 215],
                    [210, 224, 215],
                    [225, 215, 219],
                    [210, 215, 215],
                    [210, 235, 218],
                    [210, 230, 215],
                    [231, 215, 232]])


def average_y(i, m):
    total = 0
    for j in range(0, len(y_array[0])):
        total += y_array[i][j]
    return total / m


def dispersion(line, average, m):
    total = 0
    for i in range(0, len(y_array[0])):
        total += (y_array[line][i] - average) ** 2
    return total / m


def kohren():
    m = 3
    global x_array, y_array
    kohrensList = [(1, 0.6798), (2, 0.5157), (3, 0.4377), (4, 0.391), (5, 0.3595), (6, 0.3362), (7, 0.3185),
                   (8, 0.3043), (9, 0.2926), (10, 0.2829), (16, 0.2462), (36, 0.2022), (144, 0.1616)]
    while True:
        myAverageArray = []
        for i in range(0, N):
            myAverageArray.append(average_y(i, m))
        myDispersionArray = []
        for i in range(0, N):
            myDispersionArray.append(dispersion(i, myAverageArray[i], m))
        Gp = np.max(np.array(myDispersionArray)) / np.sum(np.array(myDispersionArray))
        f1 = m - 1
        f2 = N
        if Gp <= kohrensList[f1 - 1][1]:
            return Gp, m, myAverageArray, myDispersionArray, f1, f2
        m += 1
        additional = np.array([[randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)],
                               [randint(y_min, y_max)]])
        y_array = np.append(y_array, additional, axis=1)
        myAverageArray = []
        myDispersionArray = []


Gp, m, my_Y_averageArray, myDispersionArray, f1, f2 = kohren()
print(f"m={m}, при Gр={Gp}")

my_X_averageArray = []


def averageX_inLine(position):
    total = 0
    for i in range(N):
        total += x_array[i][position]
    return total / N


for i in range(3):
    my_X_averageArray.append(averageX_inLine(i))
my = np.sum(my_Y_averageArray) / m


def get_sum(*args):
    summa = 0
    try:
        if args[0] == "y":
            if len(args) == 1:
                summa = sum(my_Y_averageArray)
            else:
                for j in range(N):
                    sum_i_temp = 1
                    for i in range(len(args) - 1):
                        sum_i_temp *= x_array[j][args[i + 1] - 1]
                    sum_i_temp *= my_Y_averageArray[j]
                    summa += sum_i_temp

        elif len(args) == 1:
            args = args[0] - 1
            for obj in x_array:
                summa += obj[args]
        else:
            for obj in x_array:
                sum_i_temp = 1
                for i in range(len(args)):
                    sum_i_temp *= obj[args[i] - 1]
                summa += sum_i_temp
    except:
        print("def error")
    return summa


coeffList_1 = [N, get_sum(1), get_sum(2), get_sum(3), get_sum(1, 2), get_sum(1, 3),
               get_sum(2, 3), get_sum(1, 2, 3)]
coeffList_2 = [get_sum(1), get_sum(1, 1), get_sum(1, 2), get_sum(1, 3), get_sum(1, 1, 2),
               get_sum(1, 1, 3), get_sum(1, 2, 3), get_sum(1, 1, 2, 3)]
coeffList_3 = [get_sum(2), get_sum(1, 2), get_sum(2, 2), get_sum(2, 3), get_sum(1, 2, 2),
               get_sum(1, 2, 3), get_sum(2, 2, 3), get_sum(1, 2, 2, 3)]
coeffList_4 = [get_sum(3), get_sum(1, 3), get_sum(2, 3), get_sum(3, 3), get_sum(1, 2, 3),
               get_sum(1, 3, 3), get_sum(2, 3, 3), get_sum(1, 2, 3, 3)]
coeffList_5 = [get_sum(1, 2), get_sum(1, 1, 2), get_sum(1, 2, 2), get_sum(1, 2, 3),
               get_sum(1, 1, 2, 2), get_sum(1, 1, 2, 3), get_sum(1, 2, 2, 3), get_sum(1, 1, 2, 2, 3)]
coeffList_6 = [get_sum(1, 3), get_sum(1, 1, 3), get_sum(1, 2, 3), get_sum(1, 3, 3),
               get_sum(1, 1, 2, 3), get_sum(1, 1, 3, 3), get_sum(1, 2, 3, 3), get_sum(1, 1, 2, 3, 3)]
coeffList_7 = [get_sum(2, 3), get_sum(1, 2, 3), get_sum(2, 2, 3), get_sum(2, 3, 3),
               get_sum(1, 2, 2, 3), get_sum(1, 2, 3, 3), get_sum(2, 2, 3, 3), get_sum(1, 2, 2, 3, 3)]
coeffList_8 = [get_sum(1, 2, 3), get_sum(1, 1, 2, 3), get_sum(1, 2, 2, 3), get_sum(1, 2, 3, 3),
               get_sum(1, 1, 2, 2, 3), get_sum(1, 1, 2, 3, 3), get_sum(1, 2, 2, 3, 3), get_sum(1, 1, 2, 2, 3, 3)]

coeffListNinth = [k0, k1, k2, k3, k4, k5, k6, k7] = [get_sum("y"), get_sum("y", 1), get_sum("y", 2), get_sum(
    "y", 3), get_sum("y", 1, 2), get_sum("y", 1, 3), get_sum("y", 2, 3), get_sum("y", 1, 2, 3)]

fullList = [coeffList_1, coeffList_2, coeffList_3, coeffList_4, coeffList_5, coeffList_6, coeffList_7, coeffList_8]


def positioning(position):
    newFulllist = deepcopy(fullList)
    count = 0
    for each in newFulllist:
        each.insert(position, coeffListNinth[count])
        each.pop(position + 1)
        count += 1
    return newFulllist


fullDet = np.linalg.det(np.array(fullList))

b0 = np.linalg.det(np.array(positioning(0))) / fullDet
b1 = np.linalg.det(np.array(positioning(1))) / fullDet
b2 = np.linalg.det(np.array(positioning(2))) / fullDet
b3 = np.linalg.det(np.array(positioning(3))) / fullDet
b12 = np.linalg.det(np.array(positioning(4))) / fullDet
b13 = np.linalg.det(np.array(positioning(5))) / fullDet
b23 = np.linalg.det(np.array(positioning(6))) / fullDet
b123 = np.linalg.det(np.array(positioning(7))) / fullDet

# Стьюдент
S2B = np.sum(myDispersionArray) / N
S2Bs = S2B / m / N
Sbs = np.sqrt(S2Bs)

x_array_normal = [
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1],
]


def get_beta(i):
    summa = 0
    for j in range(N):
        summa += my_Y_averageArray[j] * x_array_normal[j][i]
    summa /= N
    return summa


beta0 = get_beta(0)
beta1 = get_beta(1)
beta2 = get_beta(2)
beta3 = get_beta(3)

t0 = abs(beta0) / Sbs
t1 = abs(beta1) / Sbs
t2 = abs(beta2) / Sbs
t3 = abs(beta3) / Sbs

f3 = f1 * f2

t_tab = scipy.stats.t.ppf((1 + (1 - q)) / 2, f3)
print("t from table:", t_tab)

t_arr = np.array([t0, t1, t2, t3])
b_arr = np.array([b0, b1, b2, b3])
b_arr[t_arr < t_tab] = 0 

b0,b1,b2,b3=b_arr

y_hat = b0 + b1 * x_array[:,0] + b2 * x_array[:,1] + b3 * x_array[:,2] + b12 * x_array[:,0] * x_array[:,1] + b13 * x_array[:,0] * x_array[:,2] + b123 * x_array[:,0] * x_array[:,1] * x_array[:,2]

d = 2
f4 = N - d
S2_ad = 0
for i in range(N):
    S2_ad += (m / (N - d) * ((y_hat[i] - my_Y_averageArray[i]) ** 2))

Fp = S2_ad / S2B
Ft = scipy.stats.f.ppf(1 - q, f4, f3)
print("Fp:", Fp)
print("Ft:", Ft)
#if Fp > Ft:
print("Adequate precisely at 0,05")
#else:
print("Not adequate precisely at 0,05")
lalala