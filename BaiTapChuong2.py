#Câu1
import math

try:
    r = float(input("Nhập bán kính hình tròn: "))
    if r < 0:
        print("Bán kính không được âm, nhập lại!")
    else:
        cv = 2 * math.pi * r
        dt = math.pi * r * r
        print(f"Chu vi hình tròn: {cv}")
        print(f"Diện tích hình tròn: {dt}")
except :
    print("Nhập sai dữ liệu")
#Câu2
try:
    second = int(input("Nhập số giây: "))
    if second <= 0:
        print("Số giây không được âm, nhập lại!")
    else:
        t=int(input("Nhập số giây:"))
        hour=(t//3600)%24
        minute=(t%3600)//60
        second=(t%3600)%60
        print(hour,":",minute,":",second)
except:
    print("Nhập sai dữ liệu")
#Câu3
try:
    diem1 = float(input("Nhập điểm môn thứ nhất: "))
    diem2 = float(input("Nhập điểm môn thứ hai: "))
    diem3 = float(input("Nhập điểm môn thứ ba: "))
    if (0 <= diem1 <= 10) and (0 <= diem2 <= 10) and (0 <= diem3 <= 10):
        dtb = (diem1 + diem2 + diem3) / 3
        print(f"Điểm trung bình: {dtb:.2f}")
    else:
        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
except:
    print("Nhập sai dữ liệu")
#Câu4
#Python hỗ trợ các kiểu dữ liệu cơ bản sau:
#int: Số nguyên (ví dụ: 1, -5, 100)
#float: Số thực (ví dụ: 3.14, -2.5)
#bool: Kiểu logic (True, False)
#str: Chuỗi ký tự (ví dụ: "Hello", 'Python')
#list: Danh sách (ví dụ: [1, 2, 3])
#tuple: Bộ giá trị (ví dụ: (1, 2, 3))
#dict: Từ điển (ví dụ: {"a": 1, "b": 2})
#set: Tập hợp (ví dụ: {1, 2, 3})

#Câu5
# Còn lệnh # dùng để ghi chú  1 dòng
'''
Đây là ghi chú
nhiều dòng
'''
# Hoặc:
"""
Ghi chú nhiều dòng
bằng dấu nháy kép
"""
# Câu6
#/ : Chia thực
#// : Chia lấy phần nguyên 
#% : Chia lấy phần dư
#** : Lũy thừa
#and : Phép toán logic "và"
#or : Phép toán logic "hoặc"
#is : Kiểm tra hai đối tượng có cùng tham chiếu hay không

#Câu7
# 1: Sử dụng hàm input()
#ví dụ:
ten = input("Nhập tên của bạn: ")
print("Xin chào,", ten)
# 2: Chuyển đổi kiểu dữ liệu
#ví dụ:
tuoi = int(input("Nhập tuổi của bạn: "))
diem = float(input("Nhập điểm: "))
# 3: Sử dụng phương thức split() để tách chuỗi
#ví dụ:
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
a = int(a)
b = int(b)
# 4: Nhập danh sách các số
#ví dụ:
ds = [int(x) for x in input("Nhập các số, cách nhau bởi dấu cách: ").split()]
print(ds)

#Câu8
# 1: Sai cú pháp (Syntax Error)
#print("Hello"  # Thiếu dấu đóng ngoặc
# 2: Lỗi chia cho 0 (ZeroDivisionError)
a = 5 / 0  # Lỗi chia cho 0
# 3: Lỗi logic (Logical Error)
if 2 > 3:
    print("Đúng")
else:
    print("Sai")  # Kết quả sai vì 2 không lớn hơn 3
# 4: Lỗi kiểu dữ liệu (TypeError)
result = '2' + 3  # Không thể cộng chuỗi với số nguyên
# 5: Lỗi tên biến (NameError)
print(x)  # Biến x chưa được định nghĩa
# 6: Lỗi nhập dữ liệu (ValueError)
num = int(input("Nhập một số nguyên: "))  # Nhập chuỗi thay vì số nguyên
# 7: Lỗi chỉ mục (IndexError)
lst = [1, 2, 3]
print(lst[5])  # Chỉ mục 5 không tồn tại trong danh sách
# 8: Lỗi thuộc tính (AttributeError)
text = "Hello"
text.append('!')  # Chuỗi không có phương thức append
# 9: Lỗi nhập xuất (IOError)
file = open("non_existent_file.txt", "r")  # Tệp không tồn tại
# 10: Lỗi nhập xuất (ImportError)
import non_existent_module  # Thư viện không tồn tại
#Cách bắt lỗi trong Python:
#Sử dụng khối try...except để bắt và xử lý lỗi khi chạy:
#ví dụ:
try:
    x = int(input("Nhập số: "))
    y = 10 / x
except ValueError:
    print("Bạn phải nhập số nguyên!")
except ZeroDivisionError:
    print("Không được chia cho 0!")
except Exception as e:
    print("Lỗi khác:", e)
else:
    print("Kết quả:", y)
finally:
    print("Kết thúc chương trình.")
#try: Đặt các lệnh có thể gây lỗi.
#except: Xử lý lỗi nếu xảy ra.
#else: Thực hiện khi không có lỗi.
#finally: Luôn thực hiện, dù có lỗi hay không.
#Câu9
#(a) i1 + (i2 * i3)
#= 2 + (5 * -3) = 2 + (-15) = -13
#Giải thích: Nhân trước, cộng sau.

#(b) i1 * (i2 + i3)
#= 2 * (5 + -3) = 2 * 2 = 4
#Giải thích: Cộng trong ngoặc trước, nhân sau.

#(c) i1 / (i2 + i3)
#= 2 / (5 + -3) = 2 / 2 = 1.0
#Giải thích: Chia thực.

#(d) i1 // (i2 + i3)
#= 2 // (5 + -3) = 2 // 2 = 1
#Giải thích: Chia lấy phần nguyên

#(e) i1 / i2 + i3
#= 2 / 5 + (-3) = 0.4 + (-3) = -2.6
#Giải thích: Chia trước, cộng sau.

#(f) i1 // i2 + i3
#= 2 // 5 + (-3) = 0 + (-3) = -3
#Giải thích: 2 // 5 = 0 (vì 2 < 5).

#(g) 3 + 4 + 5 / 3
#= 3 + 4 + (5 / 3) = 3 + 4 + 1.666... = 8.666...
#Giải thích: Chia trước, cộng sau.

#(h) 3 + 4 + 5 // 3
#= 3 + 4 + (5 // 3) = 3 + 4 + 1 = 8
#Giải thích: Chia lấy nguyên trước, cộng sau.

#(i) (3 + 4 + 5) / 3
#= (3 + 4 + 5) / 3 = 12 / 3 = 4.0
#Giải thích: Cộng trong ngoặc trước, chia sau.

#(j) (3 + 4 + 5) // 3
#= (3 + 4 + 5) // 3 = 12 // 3 = 4
#Giải thích: Cộng trong ngoặc trước, chia lấy nguyên.

#(k) d1 + (d2 * d3)
#= 2.0 + (5.0 * -0.5) = 2.0 + (-2.5) = -0.5
#Giải thích: Nhân trước, cộng sau.

#(l) d1 + d2 * d3
#= 2.0 + 5.0 * -0.5 = 2.0 + (-2.5) = -0.5
#Giải thích: Nhân trước, cộng sau.

#(m) d1 / d2 - d3
#= 2.0 / 5.0 - (-0.5) = 0.4 - (-0.5) = 0.4 + 0.5 = 0.9
#Giải thích: Chia trước, trừ sau.

#(n) d1 / (d2 - d3)
#= 2.0 / (5.0 - (-0.5)) = 2.0 / 5.5 ≈ 0.3636
#Giải thích: Trừ trong ngoặc trước, chia sau.
#(o) d1 + d2 + d3 / 3
#= 2.0 + 5.0 + (-0.5 / 3) = 2.0 + 5.0 + (-0.1666...) = 7.0 - 0.1666... = 6.833...
#Giải thích: Chia trước, cộng sau.

#(p) (d1 + d2 + d3) / 3
#= (2.0 + 5.0 + -0.5) / 3 = (6.5) / 3 ≈ 2.166...
#Giải thích: Cộng trong ngoặc trước, chia sau.

#(q) d1 + d2 + (d3 / 3)
#= 2.0 + 5.0 + (-0.5 / 3) = 2.0 + 5.0 + (-0.1666...) = 6.833...
#Giải thích: Giống câu (o).

#(r) 3 * (d1 + d2) * (d1 - d3)
#= 3 * (2.0 + 5.0) * (2.0 - (-0.5)) = 3 * 7.0 * 2.5 = 21.0 * 2.5 = 52.5
#Giải thích: Cộng và trừ trong ngoặc trước, nhân sau.

#Câu10
# (a)
x += 1

# (b)
x /= 2

# (c)
x -= 1

# (d)
x += y

# (e)
x -= (y + 7)

# (f)
x *= 2

# (g)
number_of_closed_cases += 2 * ncc
