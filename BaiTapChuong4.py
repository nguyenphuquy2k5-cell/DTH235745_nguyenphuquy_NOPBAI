#Câu1
print("Chương trình tính diện tích hình chữ nhật")
from math import sqrt
print("Chương trình tính diện tích Tam Giác")
a=float(input("Nhập cạnh a>0:"))
b=float(input("Nhập cạnh b>0:"))
c=float(input("Nhập cạnh c>0:"))
if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a:
 print("Tam giác không hợp lệ")
else:
 cv=a+b+c
 p=cv/2
 dt=sqrt(p*(p-a)*(p-b)*(p-c))
 print("Diện tích =",dt)
#Câu2
print("Chương trình chơi trò chơi đoán số")
from random import randrange
while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
        solandoan+=1
    songuoi=int(input("Máy đoán [1..100], mời bạn đoán:"))
    print("Bạn đoán lần thứ ",solandoan)
    if somay==songuoi:
        print("Chúc mừng bạn đoán đúng, số máy là=",somay)
    win=True
    break
    if somay>songuoi:
        print("Bạn đoán sai, số máy > số bạn")
    elif somay<songuoi:
        print("Bạn đoán sai, số máy < số bạn")
    if win==False:
        print("GAME OVER!, số máy =",somay)
    hoi=input("Tiếp không?")
    if hoi=="k":
        break
    print("Cám ơn bạn đã chơi Game!")
#Câu3
print("Chương trình tính BMI")
def BMI(Cao,CanNang):
 return CanNang/(Cao**2)
def PhanLoai(bmi):
 if bmi<18.5:
    return "Gầy"
 elif bmi<=24.9:
    return "Bình thường"
 elif bmi<=29.9:
    return "Hơi Béo"
 elif bmi<=34.9:
    return "Béo Phì Cấp Độ 1"
 elif bmi<=39.9:
    return "Béo Phì Cấp Độ 2"
 else:
    return "Béo Phì Cấp độ 3"
def NguyCoBenh(bmi):
 if bmi<18.5:
    return "Thấp"
 elif bmi<=24.9:
    return "Trung Bình"
 elif bmi<=29.9:
    return "Cao"
 elif bmi<=34.9:
    return "Cao"
 elif bmi<=39.9:
    return "Rất Cao"
 else:
    return "Nguy Hiểm"
print("Nhập vào chiều cao:")
Cao=float(input())
print("Nhập vào cân nặng:")
CanNang=float(input())
bmi=BMI(Cao,CanNang)
print("BMI của bạn=",bmi)
print("Phân loại bạn=",PhanLoai(bmi))
print("Nguy cơ bệnh của bạn=",NguyCoBenh(bmi))

#Câu4
print("Chương trình tính ROI")
def ROI(dt,cp):
 return (dt-cp)/cp
def GoiYDauTu(roi):
 if roi>=0.75:
    return "Nên đầu tư"
 else:
    return "Không nên đầu tư"
print("Chương trình tính ROI")
dt=int(input("Nhập Doanh Thu:"))
cp=int(input("Nhập chi phí:"))
roi=ROI(dt,cp)
print("Tỉ Lệ ROI=",roi)
print("==>",GoiYDauTu(roi))
#Câu5
print("Chương trình tính đệ qui Fibonacci")
def fibonacci(n):
 if n<=2 :
    return 1
 return fibonacci(n-1)+fibonacci(n-2)
def listfibo(n):
 for i in range(1,n+1):
    print(fibonacci(i),end='\t')
print(fibonacci(9))
listfibo(9)
#Câu6
print("Chương trình tính giá trị nào có thể xuất hiện trong randrange(0,100)")
def giaTriXuatHien():
    s=set()
    for i in range(100000):
        s.add(randrange(0,100))
    return s
print(giaTriXuatHien())
#Câu7
print("Chương trình tính độ dài đoạn AB")
import math
def doDaiAB(x1,y1,x2,y2):
 return math.sqrt((x2-x1)**2+(y2-y1)**2)
x1=float(input("Nhập x1:"))
y1=float(input("Nhập y1:"))
x2=float(input("Nhập x2:"))
y2=float(input("Nhập y2:"))
print("Độ dài đoạn AB=",doDaiAB(x1,y1,x2,y2))
#Câu8
print("Chương trình tính log cơ số a của x")
import math
def loga(x,a):
 return math.log(x,a)
x=float(input("Nhập x>0:"))
a=float(input("Nhập a>0 và a!=1:"))
if x<=0 or a<=0 or a==1:
    print("Không hợp lệ")
else:
    print("log cơ số",a,"của",x,"là:",loga(x,a))
#Câu9
print("Chương trình tính căn bậc hai lồng nhau")
import math
def canBacHaiLongNhau(n):
 if n==0:
    return 0
 return math.sqrt(n+canBacHaiLongNhau(n-1))
n=int(input("Nhập n>0:"))
if n<0:
    print("Không hợp lệ")
else:
    print("Kết quả là:",canBacHaiLongNhau(n))
#Câu10
print("Chương trình vẽ hình dùng Sleep")
import time
# Hình 1
print("Hình 1:")
print("      *")
print("      * *")
print("      * * *")
print("* * * * * * *")
print("* * *")
print("* *")
print("* ")

# Dừng 5 giây
time.sleep(5)

# Hình 2
print("\nHình 2:")
print("      *")
print("      * *")
print("      *   *")
print("* * * * * * *")
print("*   *")
print("* *")
print("* ")
time.sleep(5)

# Hình 3
print("\nHình 3:")
print("      * * * *")
print("      * * *")
print("      * *")
print("      *")
print("      *")
print("    * *")
print("  * * *")
print("* * * *")

time.sleep(5)

# Hình 4
print("\nHình 4:")
print("      * * * *")
print("      *   *")
print("      * *")
print("      *")
print("      *")
print("    * *")
print("  *   *")
print("* * * *")
#Câu11
print("Chương trình kiểm tra kết quả thực thi")
def sum1(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s = s + val
        val = val - 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s = s + i
    return s

# TRƯỜNG HỢP 1

def main1():
    global val
    val = 5
    print("Trường hợp 1:")
    print(sum1(5))
    print(sum2())
    print(sum3())
    print("----------------")

# TRƯỜNG HỢP 2

def main2():
    global val
    val = 5
    print("Trường hợp 2:")
    print(sum3())
    print(sum2())
    print(sum1(5))
    print("----------------")


# TRƯỜNG HỢP 3

def main3():
    global val
    val = 5
    print("Trường hợp 3:")
    print(sum2())
    print(sum1(5))
    print(sum3())
    print("----------------")

# CHẠY TOÀN BỘ
main1()
main2()
main3()

#Câu12
print("Chương trình hàm oscillate chạy từ -3 đến 5")
def oscillate(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + oscillate(n - 1)
    else:
        return n + oscillate(n + 1)
for i in range(-3, 5):
    print("oscillate(", i, ") =", oscillate(i))
#Câu13
print("Chương trình kiểm tra số hoàn thiện, số thịnh vượng")
def soHoanThien(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def soThinhVuong(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong > n
n = int(input("Nhập một số nguyên dương: "))
if n <= 0:
    print("Số không hợp lệ")
else:
    if soHoanThien(n):
        print(n, "là số hoàn thiện")
    else:
        print(n, "không phải là số hoàn thiện")
    if soThinhVuong(n):
        print(n, "là số thịnh vượng")
    else:
        print(n, "không phải là số thịnh vượng")
    
