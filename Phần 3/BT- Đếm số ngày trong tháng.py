# Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
# 1,3,5,7,8,10,12 -> 31 ngày
# 4,6,9,11 -> 30 ngày
# Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày, không nhuần có 28 ngày.

month = int(input("Nhập vào một tháng bất kỳ: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("Tháng", month, "có 31 ngày")
elif month == 2:
    year = int(input("Nhập vào năm: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(" Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
elif month in (4, 6, 9, 11):
    print("Tháng", month, "có 30 ngày")
else:
    print("Tháng không hợp lệ!!")
