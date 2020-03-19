import random as rand

n = 8
a0 = 1
a1 = 1
a2 = 1
a3 = 1

x1 = []
x2 = []
x3 = []

y = []
f = []

xn1 = []
xn2 = []
xn3 = []

if input("random? ").lower() == "random":
    flag = True
else:
    flag = False

if flag:
    for i in range(n):
        x1.append(rand.randint(0, 20))                          #значення для 1 фактору
        x2.append(rand.randint(0, 20))                          #значення для 2 фактору
        x3.append(rand.randint(0, 20))                          #значення для 3 фактору
        y.append(a0 + a1 * x1[i] + a2 * x2[i] + a3 * x3[i])     #значення функції відгуків
else:
    for i in range(n):
        x1.append(int(input(f"X1[{i}] = ")))                    #значення для 1 фактору
        x2.append(int(input(f"X2[{i}] = ")))                    #значення для 2 фактору
        x3.append(int(input(f"X3[{i}] = ")))                    #значення для 3 фактору
    for i in range(n):
        y.append(a0 + a1 * x1[i] + a2 * x2[i] + a3 * x3[i])     #значення функції відгуків

max1 = max(x1)                                                  #Xmax для 1 фактора
max2 = max(x2)                                                  #Xmax для 2 фактора
max3 = max(x3)                                                  #Xmax для 3 фактора

min1 = min(x1)                                                  #Xmin для 1 фактора
min2 = min(x2)                                                  #Xmin для 2 фактора
min3 = min(x3)                                                  #Xmin для 3 фактора

x01 = (max1 + min1) / 2                                         #X0 для 1 фактора
x02 = (max2 + min2) / 2                                         #X0 для 2 фактора
x03 = (max3 + min3) / 2                                         #X0 для 3 фактора

yet = a0 + a1 * x01 + a2 * x02 + a3 * x03                       #Y еталонне

dx1 = x01 - min1                                                #інтервал зміни 1 фактора
dx2 = x02 - min2                                                #інтервал зміни 2 фактора
dx3 = x03 - min3                                                #інтервал зміни 3 фактора

for i in range(n):
    xn1.append((x1[i] - x01) / dx1)                             #нормоване значення для 1 фактора
    xn2.append((x2[i] - x02) / dx2)                             #нормоване значення для 2 фактора
    xn3.append((x3[i] - x03) / dx3)                             #нормоване значення для 3 фактора
    f.append((y[i] - yet) ** 2)                                 #критерій вибору (Y-Yєт)²
res = max(f)                                                    #max (Y-Yєт)²

print(f"\nA0 =  {a0};   A1 =  {a1};   A2 = {a2};   A3 = {a3}")
print("\nMatrix X:")
print("____________________")
for i in range(n):
    print("| {0:<5}  {1:<5}  {2:<3} |".format(x1[i], x2[i], x3[i]))
print("____________________\n")
print("X01 = {0:<5}  X02 = {1:<5}  X03 = {2:<5}\n".format(x01, x02, x03))
print("Xd1 = {0:<5}  Xd2 = {1:<5}  Xd3 = {2:<5}\n".format(dx1, dx2, dx3))
print(f"Y = {y}")
print("\nMatrix Xn:")
print("______________________")
for i in range(n):
    print("| {0:<5.2f}  {1:<5.2f}  {2:<5.2f} |".format(xn1[i], xn2[i], xn3[i]))
print("______________________\n")
print(f"Yet = {yet}\n\n(Y-Yэт)² = {f}\n\nmax((Y-Yэт)²) = {res}")