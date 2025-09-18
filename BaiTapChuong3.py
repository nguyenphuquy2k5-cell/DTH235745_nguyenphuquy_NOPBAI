#Câu 1
print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời Thím nhập vào 1 năm:"))
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
 print("Năm ", year, " là năm nhuần")
else:
 print("Năm ", year, " không nhuần")

#Câu 2
print("Chương trình đếm số ngày trong tháng")
month=int(input("Nhập vào 1 tháng:"))
if month in (1,3,5,7,8,10,12):
 print("Tháng ", month, " có 31 ngày")
elif month in (4,6,9,11):
 print("Tháng ", month, " có 30 ngày")
elif month==2:
 year=int(input("Mời bạn nhập vào năm:"))
 if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print("Tháng ",month, " có 29 ngày")
 else:
    print("Tháng ", month, " có 28 ngày")
else:
    print("Tháng ", month, " không hợp lệ")

#Câu 3
from math import sqrt
print("Chương trình Giải Phương trình bậc 2")
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
if a == 0:
 #bx+c=0
 if b == 0 and c ==0:
    print("Vô số nghiệm")
 elif b==0 and c !=0:
    print("Vô nghiệm")
 else:
    x=-c/b
 print("No x=",x)
else:
 delta=b**2-4*a*c
 if delta <0 :
    print("Vô No")
 elif delta ==0:
    x=-b/(2*a)
    print("No kép x1=x2=",x)
 else:
    x1=(-b-sqrt(delta))/(2*a)
    x2=(-b+sqrt(delta))/(2*a)
    print("x1=",x1)
    print("x2=",x2)

#Câu 4
x = 3
y = 5
z = 7
print("a)", x == 3)
print("b)", x < y)
print("c)", x >= y)
print("d)", x <= y)
print("e)", x != y - 2)
print("f)", x <  10)
print("g)", x >= 0 and x <10)
print("h)", x < 0 or x <10)
print("i)", x >= 0 or x < 2)
print("j)", x < 0 or x < 10)
print("k)", x >0 or x < 10)
print("l)", x < 0 or x > 10)

#Câu 5
cases = [
    (3, 5, 7),   # (a)
    (3, 7, 5),   # (b)
    (5, 3, 7),   # (c)
    (5, 7, 3),   # (d)
    (7, 3, 5),   # (e)
    (7, 5, 3)    # (f)
]

for idx, (i, j, k) in enumerate(cases, start=1):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j < k:
            j = k
        else:
            i = k
    
    print("i = ", i, " j = ", j, " k = ", k)

#Câu 6
print("Chương trình đọc số có tối đa 2 chữ số")

n = int(input("Nhập một số (0–99): "))

so = ["", "một", "hai", "ba", "bốn", "năm",
      "sáu", "bảy", "tám", "chín"]

if n < 0 or n > 99:
    print("Số không hợp lệ")

elif n < 10:
    print("Cách đọc:", so[n].capitalize())

elif n == 10:
    print("Cách đọc: Mười")

elif 10 < n < 20:
    donvi = n % 10
    if donvi == 5:
        print("Cách đọc: Mười lăm")
    else:
        print("Cách đọc: Mười", so[donvi])

else:  # từ 20 đến 99
    chuc = n // 10
    donvi = n % 10
    if donvi == 0:
        print("Cách đọc:", so[chuc].capitalize(), "mươi")
    elif donvi == 1:
        print("Cách đọc:", so[chuc].capitalize(), "mươi mốt")
    elif donvi == 5:
        print("Cách đọc:", so[chuc].capitalize(), "mươi lăm")
    else:
        print("Cách đọc:", so[chuc].capitalize(), "mươi", so[donvi])

#Câu 7
print("Chương trình tìm ngày kế tiếp")

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    max_day = 31
elif month in (4, 6, 9, 11):
    max_day = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_day = 29
    else:
        max_day = 28
else:
    print("Tháng không hợp lệ!")
    exit()

if day < max_day:
    day += 1
else:  
    day = 1
    if month == 12:  
        month = 1
        year += 1
    else:
        month += 1

print("Ngày kế tiếp là: {}/{}/{}".format(day, month, year))

#Câu 8
print("Chương trình xuất kết quả theo phép tính đã nhập: ")
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
operator = input("Nhập phép tính (+, -, *, /): ")
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        print("Lỗi: Không thể chia cho 0.")
        exit()
else:
    print("Phép tính không hợp lệ.")
    exit()

print("Kết quả: {} {} {} = {}".format(a, operator, b, result))

#Câu 9
print("Chương trình tìm tháng thuộc quý mấy trong năm")
month = int(input("Nhập tháng (1-12): "))
if month in [1, 2, 3]:
    quarter = 1
elif month in [4, 5, 6]:
    quarter = 2
elif month in [7, 8, 9]:
    quarter = 3
elif month in [10, 11, 12]:
    quarter = 4
else:
    print("Tháng không hợp lệ!")
    exit()
print("Tháng {} thuộc quý {}".format(month, quarter))

#Câu 10
print("Chương trình tính dãy số:")
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0
for i in range(n + 1):
    tu= x ** i
    mau=1
    for j in range(1, i + 1):
        mau *= j
    s = s + (tu / mau)
    print("s({0},{1})={2}".format(x, n,s))

#Câu 11
print("Chương trình kiểm tra số nguyên: ")
while True:
    n=int (input("Nhập số nguyên dương n: "))
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if dem==2:
        print(n,"là số nguyên tố")  
    else:
        print(n,"không là số nguyên tố")

        hoi= input("Bạn có muốn tiếp tục không? (c/k): ")
        if hoi == 'k':
            break
        print("BYE!")

#Câu 12
print("Chương tình xuất bảng cửu chương")
for i in range(1,11):
 for j in range(2,10):
    line="{0}*{1:>2}={2:>2}".format(j,i,i*j)
    print(line,end='\t')
print()

#Câu 13
#print("Chương trình tính có bao nhiêu dấu * được in ra")
#a = 0
#while a < 100:
#    print("*", end="")
#   print()
#Chương trình trên bị lỗi, vòng lập sẽ chạy vô hạn vì biến a không được tăng giá trị.
#Sửa lại như sau:
#a = 0       
#while a < 100:
#    print("*", end="")
#    a += 1
#    print()

#Câu 14
print("Chương trình cho biết có bao nhiêu dấu * được in ra")
a = 0
Tong = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print("*", end="")
            Tong += 1
        else:
            print("-", end="")
        b +=1
    print()
    a += 1
print("\nTổng cộng số dấu * được in ra là",Tong)

#Câu 15
#(a) range(5)->chạy mặc định là từ 0 đến 4
#(b) range(5, 10)->chạy từ 5 đến dừng trước 10
#(c) range(5, 20, 3)->chạy từ 5 đến trước 20 bước nhảy là 3
#(d) range(20, 5, -1)-> bắt đầu từ 20 giảm mỗi lần 1 về tới trước 5
#(e) range(20, 5, -3)->bắt đầu từ 20 giảm mỗi lần 3 về tới trước 5
#(f) range(10, 5)-> bắt đầu từ dừng trước 5 nhưng step mặc định là tăng 1 nên không chạy được số nào
#(g) range(0)-> từ 0 đến 1 không có gì rỗng
#(h) range(10, 101, 10)-> từ 10 đến 100 bước nhảy là 10
#(i) range(10, -1, -1)-> từ 10 giảm xuống 0 mỗi lần giảm 1
#(j) range(-3, 4)-> từ -3 đến 3
#(k) range(0, 10, 1)->từ 0 đến 9 bước nhảy 1

#Câu 16
for a in range(20, 100, 5):
    print('*', end='')
    print()

 #chạy từ 20 đến 99 và bước nhảy 5 sau khi chạy in ra được 16 dấu *

#Câu17
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        print("n =", n)
        break
#Câu 18
n = int(input("Nhập chiều cao của hình: "))
#hình vuông
for i in range(n):
    if i == 0 or i == n - 1:           # hàng đầu & cuối
        print("* " * n)
    else:                              # hàng giữa
        print("* " + "  " * (n - 2) + "*") #số 2 trong (n-2) là * ở đầu và cuối hàng giữa

#hình tam giác vuông
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

#hình 2 tam giác vuông chéo nhau
h = n // 2

# Tạo các dòng
lines = ['*' * i for i in range(1, h + 1)] + ['*' * n] + [' ' * (n - i) + '*' * i for i in range(h, 0, -1)]

# In ra, giữ nguyên dòng giữa
for idx, row in enumerate(lines):
    if idx == h:  # dòng giữa
        print(row)
    else:
        print(''.join(c if i == 0 or i == len(row)-1 or row[i-1] != '*' or row[i+1] != '*' else ' '
                      for i, c in enumerate(row)))

#Câu19
import math
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
for i in range(n + 1):
    mu = 2 * i + 1
    S += x**mu
    print("Giá trị S(x, n) =",S)