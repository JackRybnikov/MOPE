import random
import numpy
import math
from scipy.stats import t,f


def table_student(prob, n, m):
    x_vec = [i*0.0001 for i in range(int(5/0.0001))]
    par = 0.5 + prob/0.1*0.05
    f3 = (m - 1) * n
    for i in x_vec:
        if abs(t.cdf(i, f3) - par) < 0.000005:
            return i


def table_fisher(prob, n, m, d):
    x_vec = [i*0.001 for i in range(int(10/0.001))]
    f3 = (m - 1) * n
    for i in x_vec:
        if abs(f.cdf(i, n-d, f3)-prob) < 0.0001:
            return i


def combination_mul(arr):
    return [
        1, *arr,
        round(arr[0]*arr[1], 3),
        round(arr[0]*arr[2], 3),
        round(arr[1]*arr[2], 3),
        round(arr[0]*arr[1]*arr[2], 3),
        round(arr[0]*arr[0], 3),
        round(arr[1]*arr[1], 3),
        round(arr[2]*arr[2], 3)
    ]


def geny(n, m, f):
    mat_y = [[round(sum([f[k] * combination_mul(x[i])[k] for k in range(11)]) + random.randint(0, 10) - 5, 2)
              for j in range(m)]for i in range(n)]
    return mat_y


def dispersion(array_y, array_y_average):
    array_dispersion = []

    for j in range(N):
        array_dispersion.append(0)
        for g in range(m):
            array_dispersion[j] += (array_y[j][g] - array_y_average[j])**2
        array_dispersion[j] /= m
    return array_dispersion


def cohren(y_array, y_average_array):
    dispersion_array = dispersion(y_array, y_average_array)
    max_dispersion = max(dispersion_array)
    Gp = max_dispersion/sum(dispersion_array)
    fisher = table_fisher(0.95, N, m, 1)
    Gt = fisher/(fisher+(m-1)-2)
    return Gp < Gt


def calcxi(n, listx):
    sumxi = 0
    for i in range(n):
        lsumxi = 1
        for j in range(len(listx)):
            lsumxi *= listx[j][i]
        sumxi += lsumxi
    return sumxi


def calcb(lmaty):
    a00 = [[], [xnatmod[0]], [xnatmod[1]], [xnatmod[2]], [xnatmod[0], xnatmod[1]], [xnatmod[0], xnatmod[2]],
           [xnatmod[1], xnatmod[2]], [xnatmod[0], xnatmod[1], xnatmod[2]], [xnatmod[0], xnatmod[0]],
           [xnatmod[1], xnatmod[1]], [xnatmod[2], xnatmod[2]]]
    a0 = [15]
    for i in range(10):
        a0.append(calcxi(N, a00[i + 1]))
    a1 = [calcxi(N, a00[i] + a00[1]) for i in range(len(a00))]
    a2 = [calcxi(N, a00[i] + a00[2]) for i in range(len(a00))]
    a3 = [calcxi(N, a00[i] + a00[3]) for i in range(len(a00))]
    a4 = [calcxi(N, a00[i] + a00[4]) for i in range(len(a00))]
    a5 = [calcxi(N, a00[i] + a00[5]) for i in range(len(a00))]
    a6 = [calcxi(N, a00[i] + a00[6]) for i in range(len(a00))]
    a7 = [calcxi(N, a00[i] + a00[7]) for i in range(len(a00))]
    a8 = [calcxi(N, a00[i] + a00[8]) for i in range(len(a00))]
    a9 = [calcxi(N, a00[i] + a00[9]) for i in range(len(a00))]
    a10 = [calcxi(N, a00[i] + a00[10]) for i in range(len(a00))]
    a = numpy.array([[a0[0], a0[1], a0[2], a0[3], a0[4], a0[5], a0[6], a0[7], a0[8], a0[9], a0[10]],
                     [a1[0], a1[1], a1[2], a1[3], a1[4], a1[5], a1[6], a1[7], a1[8], a1[9], a1[10]],
                     [a2[0], a2[1], a2[2], a2[3], a2[4], a2[5], a2[6], a2[7], a2[8], a2[9], a2[10]],
                     [a3[0], a3[1], a3[2], a3[3], a3[4], a3[5], a3[6], a3[7], a3[8], a3[9], a3[10]],
                     [a4[0], a4[1], a4[2], a4[3], a4[4], a4[5], a4[6], a4[7], a4[8], a4[9], a4[10]],
                     [a5[0], a5[1], a5[2], a5[3], a5[4], a5[5], a5[6], a5[7], a5[8], a5[9], a5[10]],
                     [a6[0], a6[1], a6[2], a6[3], a6[4], a6[5], a6[6], a6[7], a6[8], a6[9], a6[10]],
                     [a7[0], a7[1], a7[2], a7[3], a7[4], a7[5], a7[6], a7[7], a7[8], a7[9], a7[10]],
                     [a8[0], a8[1], a8[2], a8[3], a8[4], a8[5], a8[6], a8[7], a8[8], a8[9], a8[10]],
                     [a9[0], a9[1], a9[2], a9[3], a9[4], a9[5], a9[6], a9[7], a9[8], a9[9], a9[10]],
                     [a10[0], a10[1], a10[2], a10[3], a10[4], a10[5], a10[6], a10[7], a10[8], a10[9],
                      a10[10]]])
    c0 = [calcxi(N, [lmaty])]
    for i in range(len(a00) - 1):
        c0.append(calcxi(N, a00[i + 1] + [lmaty]))
    c = numpy.array([c0[0], c0[1], c0[2], c0[3], c0[4], c0[5], c0[6], c0[7], c0[8], c0[9], c0[10]])
    b = numpy.linalg.solve(a, c)
    return b


def fisher(b_0, n, m, d, y_array, y_average_array):
    if d == n:
        return True
    dispersion_array = dispersion(y_array, y_average_array)
    sad = sum([(sum([combination_mul(x[i])[j] * b_0[j] for j in range(11)]) - y_average_array[i]) ** 2 for i in range(n)])
    sad = sad * m / (n - d)
    fp = sad / sum(dispersion_array) / n
    ft = table_fisher(0.95, n, m, d)
    return fp < ft


def student(y_array, y_average_array):
    general_dispersion = sum(dispersion(y_array, y_average_array)) / N
    statistic_dispersion = math.sqrt(general_dispersion / (N*m))
    beta = []
    for i in range(N):
        b = 0
        for j in range(3):
            b += y_average_array[i] * xn[i][j]
        beta.append(b / N)
    ts = [abs(beta[i]) / statistic_dispersion for i in range(N)]
    tt = table_student(0.95, N, m)
    st = [n > tt for n in ts]
    return st

def main():
    N = 15
    m = 2
    l = 1.75

    x1min = -30
    x1max = 20
    x01 = (x1min + x1max) / 2
    xl1 = l*(x1max-x01)+x01

    x2min = -70
    x2max = -10 
    x02 = (x2min + x2max) / 2
    xl2 = l*(x2max-x02)+x02

    x3min = -70
    x3max = -40
    x03 = (x3min + x3max) / 2
    xl3 = l*(x3max-x03)+x03

    xn = [
        [-1, -1, -1],
        [-1, 1, 1],
        [1, -1, 1],
        [1, 1, -1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1],
        [1, 1, 1],
        [-l, 0, 0],
        [l, 0, 0],
        [0, -l, 0],
        [0, l, 0],
        [0, 0, -l],
        [0, 0, l],
        [0, 0, 0]
    ]

    x = [
        [x1min, x2min, x3min],
        [x1min, x2min, x3max],
        [x1min, x2max, x3min],
        [x1min, x2max, x3max],
        [x1max, x2min, x3min],
        [x1max, x2min, x3max],
        [x1max, x2max, x3min],
        [x1max, x2max, x3max],
        [-xl1, x02, x03],
        [xl1, x02, x03],
        [x01, -xl2, x03],
        [x01, xl2, x03],
        [x01, x02, -xl3],
        [x01, x02, xl3],
        [x01, x02, x03]
    ]

    f_x1_x2_x3 = [
        2.1,
        1.7, #x1
        6.8, #x2
        6.6, #x3
        3.0, #x1x2
        0.1, #x1x3
        4.5, #x2x3
        1.8, #x1x2x3
        9.5, #x1^2
        1.0, #x2^2
        3.9  #x3^2
    ]

    condition_cohren = False
    condition_fisher = False


    while not condition_fisher:
        while not condition_cohren:
            print(f'm={m}')
            xnatmod = [[x[i][j] for i in range(N)] for j in range(3)]
            y = geny(N, m, f_x1_x2_x3)
            y_average = [sum(y[i])/m for i in range(N)]
            condition_cohren = cohren(y, y_average)
            if not condition_cohren:
                m += 1
        b0 = calcb(y_average)
        print('Коефіцієнти регресії:')
        print(b0)
        d = sum(student(y, y_average))
        print(f'Кількість значущих коефіцієнтів:{d}')
        condition_fisher = fisher(b0, N, m, d, y, y_average)
        if condition_fisher:
            print('Отримана математична модель адекватна експериментальним даним')