# birthYear = 2020
# currentYear = 2026
# age = currentYear - birthYear
# print("My age is:", age)
# This code to do something

# currentYear = 2026
# birthYear = input("Please enter birth year: ")
# age = currentYear - int(birthYear)
# print(age)

# name = input("Please enter your name: ")
# print("welcome " + name)

# password = input("Please enter password: ")
# pass_length = len(password)
# print(pass_length > 5)

# current_stock = int(input('Please enter current stock: '))
# min_stock = 50

# need_refill = current_stock < min_stock
# print("Need to buy more:", need_refill)

# current_temp = int(input('Please enter current temperature: '))
# min_temp = 15
# max_temp = 40

# is_danger = current_temp > max_temp or current_temp < min_temp
# is_safe = current_temp >= 15 and current_temp <= 40
# print("Is dangerous:", is_danger)
# print("Is Safe:", is_safe)

# sub1 = int(input("Subject 1: "))
# sub2 = int(input("Subject 2: "))
# sub3 = int(input("Subject 3: "))
# avg = (sub1 + sub2 + sub3) / 3
# print('--> avg:', avg)
# Cach 1
# if avg >= 0 and avg < 5:
#     print("Yeu")
# if avg >= 5 and avg < 7:
#     print("Trung Binh")
# if avg >= 7 and avg < 8:
#     print("Kha")
# if avg >= 8 and avg <= 10:
#     print("Xuat sac")

# Cach 2
# if avg >= 8:
#     print("Xuat sac")
# elif avg >= 7:
#     print("Kha")
# elif avg >= 5:
#     print('Trung Binh')
# else:
#     print('Yeu')

# buoiNao = input('Ban muon an buoi nao? Sang - Trua - Toi?')
# if buoiNao == "Sang":
#     mon = input("Nuoc hay kho? Nuoc - Kho: ")
#     if mon == "Nuoc":
#         print("Ban co the an Pho")
#     if mon == "Kho":
#         print("Hu tieu kho , banh mi, com tam")
# if buoiNao 

# secretNum = "12345"

# guess = input("Hay nhap ma so dung: ")
# while guess != secretNum:
# if guess == secretNum:
#     print("Ban da nhap dung")
# else:
#     print("Ban da nhap sai, vui long thu lai")

# score = input("Enter the score: ")
# total = 0
# count = 0
# while score != 'exit':
#     total = total + int(score)
#     count = count + 1

#     score = input("Enter the score: ")
# avg = total/count
# print("Total score:", total)
# print("Avg score", avg)
# if avg >= 7:
#     print("Pass the course")
# else:
#     print("Fail!")

# count = 1
# while count <= 10:
#     print(count)
#     count += 1

# for i in range(7):
#     print("🎃", i)

# for i in range(3, 12):
#     print(i)

# from random import randint

# secret = randint(1, 9999)
# print('secret', secret)
# count = 0
# while count < 6:
#     guess = int(input("What is your guest?: "))
#     count += 1

#     if guess == secret:
#         print("Congraze!! at attempt", count)
#         count = 7
#     else:
#         print("Wrong please enter again")
# if (guess != secret):
#     print("You out of time!")

# for i in range(6):
#     guess = int(input("What is your guest?: "))
#     if guess == secret:
#         print("Congraze!! at attempt", count)
#         break
#     else:
#         print("Wrong please enter again")

# print("======== * Chào mừng đến với Fun Fact * ========")
# print("Bạn muốn tìm hiểu về thông tin gì? Hãy chọn:")
# answer = input("1: Các quốc gia trên thế giới - 2: Các hành tinh trong hệ mặt trời - 0: Thoát chương trình: ")

# while answer != "0":
#     if answer == "1":
#         da = input("Bạn muốn hỏi về nước nào? (1: Việt Nam - 2: Mỹ - 3: Thái Lan): ")
#         if da == "1":
#             print('''🇻🇳 Việt Nam là quốc gia xuất khẩu hạt điều lớn nhất thế giới trong nhiều năm. \n☕ Việt Nam là nước xuất khẩu cà phê lớn thứ hai thế giới, chỉ sau Brazil.\n🛵 Số lượng xe máy ở Việt Nam vượt xa số lượng ô tô, với hàng chục triệu chiếc đang lưu thông. \n🌏 Việt Nam có đường bờ biển dài hơn 3.200 km. \n🐉 Hang Sơn Đoòng thuộc Sơn Đoòng Cave được xem là hang động tự nhiên lớn nhất thế giới theo thể tích.\n🍜 Phở từng được nhiều hãng từ điển quốc tế đưa trực tiếp vào từ vựng tiếng Anh dưới tên "pho". \n''')
#         if da == "2":
#             print('''🇺🇸 Mỹ có 50 bang, nhưng thủ đô Washington, D.C. không thuộc bang nào. \n🦅 Đại bàng đầu trắng là biểu tượng quốc gia của Mỹ.\n🍕 Người Mỹ ăn khoảng hàng tỷ lát pizza mỗi năm. \n🌎 Alaska là bang lớn nhất nước Mỹ, lớn hơn cả diện tích của nhiều quốc gia cộng lại. \n🏞️ Grand Canyon dài khoảng 446 km và có thể nhìn thấy từ không gian ở một số điều kiện nhất định. \n🎬 Hollywood được xem là trung tâm của ngành công nghiệp điện ảnh thế giới.\n🚀 Con người lần đầu đặt chân lên Mặt Trăng trong sứ mệnh Apollo 11 Moon Landing do Mỹ thực hiện.\n💵 Tờ 1 USD là loại tiền giấy được lưu hành nhiều nhất tại Mỹ.\n🗽 Statue of Liberty thực ra là món quà từ Pháp tặng Mỹ vào năm 1886.\n🛣️ Mỹ có hệ thống đường cao tốc liên bang dài hàng chục nghìn km, thuộc hàng lớn nhất thế giới. \n''')
    
#     print("Bạn muốn tìm hiểu về thông tin gì? Hãy chọn:")
#     answer = input("1: Các quốc gia trên thế giới - 2: Các hành tinh trong hệ mặt trời - 0: Thoát chương trình ")


# def print_label2(name, classCode, sub):
#     print("____ Welcome to Algo ____")
#     print("Name:", name)
#     print("Class:", classCode)
#     print("Subject:", sub)

# print_label2("Steven", "8A3", "Math")

# def avgCalc(num1, num2, num3, num4, num5):
#     print("Average num:",(num1 + num2 + num3 + num4 + num5) / 5)

# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
# num3 = int(input("Enter number: "))
# num4 = int(input("Enter number: "))
# num5 = int(input("Enter number: "))
    
# avgCalc(num1, num2, num3, num4, num5)

# def sum1(a, b, c):
#     total = a + b+ c
#     return total

# total1 = sum1(1, 2, 3)
# print('total:', total1)

# a = 5
# b = 3

# def foo():
#     b = 10
# foo()
# print(a + b)

# def bmi_calc (a, b):
#     return a / (b * b)

# def heath_check(a, b):
#     bmi = bmi_calc(a, b)
#     if bmi <= 18.5:
#         return 'underweight'
#     elif bmi <= 25:
#         return 'normal'
#     else:
#         return 'overweight'

# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))
    
# result = heath_check(weight, height)
# print(result)
# count = 0
# def foo(count):
#     print("I love you", count)
#     if count >= 10:
#         return
#     count += 1
#     foo(count)

# foo(count)

# def repeat(count):
#     if count > 10:
#         return
#     print("Lan " + str(count))
#     repeat(count + 1)
# repeat(1)
# # Cách import 1
# import random
# ranNum = random.randint(-100, 10)
# print(ranNum)

# # cách import 2
# from random import randint, random
# ranNum = randint(-100, 10)
# print(ranNum)

# cách 3
# from random import *
# from time import time
# ranNum = randint(-100, 10)
# ranNum2 = random()
# print(ranNum) 
# print('ranNum2', ranNum2)

# Làm 1 game đoán số ngẫu nhiên, giới hạn 5 lần đoán. 

# count = 10
# timer = time()
# while count >= 0:
#     curr = time()
#     if curr - timer >= 1:
#         print(count)
#         count -= 1
#         timer = curr

# from random import randint
# import module1

# secret = randint(0, 1000)
# print(secret)
# num = ''
# count = 0
# while count < 3 and num != secret:
#     count += 1
#     num = int(input('Enter your number: '))
#     if secret > num:
#         print('Your guess is smaller than correct num')
#         print(f'You have {3 - count} times left to guess')
#     elif secret < num:
#         print('Your guess is greater than correct num')
#         print(f'You have {3 - count} times left to guess')

# if num == secret:
#     print(f'Congrazz, you guess at attemp {count}')
# else:
#     print('You lose the game!')

# module1.printInfo('John')
# ==================
# 1. Import module random
# 2. secret = random.randint(1, 100)
# 3. guess = Yêu cầu người dùng đoán số từ 1 - 100
# 4. Dùng vòng lặp while (kiểm tra điều kiện guess != secret)
# 4.1. Nếu guess > secret -> Báo số bạn đoán lớn hơn
# 4.2. Nếu guess < secret -> Báo số bạn đoán nhỏ hơn
# 4.3. guess = Yêu cầu người dùng đoán số từ 1 - 100
# 5. Thông báo chúc mừng bạn đã đoán đúng \
# import random
# import time
# secret = random.randint(1, 100)
# print(f"Random number {secret}")

# secondsFromEpoc = time.time()
# print(f"secondsFromEpoc: {secondsFromEpoc}")
# x = 123.45678
# print(round(x, 0))
# guess = int(input('Please guess a number from 1-100: '))
# count = 1
# while guess != secret:
#     if guess > secret:
#         print('You wrong! Your number greater than correct num')
#     elif guess < secret:
#         print("You wrong! Your number smaller than correct num")
#     guess = int(input('Please guess a number from 1-100: '))
#     count += 1

# # print(f"Congraz, your guess is correct! The correct number is: {secret} at attemp {count}")
# import time

# input('Bấm bất kỳ phím nào để bắt đầu đếm giờ: ')
# start = time.time()

# input('Bấm bất kỳ phím nào để kết thúc đếm giờ: ')
# end = time.time()

# duration = round(end - start, 2)
# print(f'Thời gian trôi qua là {duration} giây')

# import random
# import time

# ranNum = random.randint(1, 9)
# print(ranNum)

# numSeconds = time.time()
# print(numSeconds)
from turtle import *
from random import randint
setup(1000, 800)
bgcolor('black')
speed(10)
# # Vẽ sao
def star(x, y, size):
    penup()
    goto(x, y)
    dot(size, "white")

for i in range(200):
    star(randint(-480, 480), randint(0, 350), randint(2, 5))

hideturtle()
exitonclick()
