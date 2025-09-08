import math

try:
    r = float(input("Nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    dt = math.pi * r ** 2
    print(f"Chu vi hình tròn: {cv}")
    print(f"Diện tích hình tròn: {dt}")
except:
    print("Nhập sai dư liệu")