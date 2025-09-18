
import math
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
for i in range(n + 1):
    mu = 2 * i + 1
    S += x**mu
    print("Giá trị S(x, n) =",S)