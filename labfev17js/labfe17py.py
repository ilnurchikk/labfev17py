###############################1 функции
# def pow1(chis, step):
#     if step == 1:
#         return chis
#     return chis ** step
# chis = int(input("Введите число: "))
# step = int(input("Введите степень: "))
# print(pow1(chis, step))

############################2

# def pow1(a, b):
#     c = 0
#     for i in range(a, b + 1):
#         c += i
#     return c
#
# a = int(input("Введите число в диапозонеA: "))
# b = int(input("Введите число в диапозонеБ: "))
# print(pow1(a, b))
#####################3

# def zvezda(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0:
#                 print("*", end=" ")
#
# n = int(input("Введите число для кол-во звезд:"))
# print(zvezda(n))

####################4
##################5
# import random
# a = [random.randint(1, 10) for i in range(100)]
# print(a)
# def cpisik(lsti:list,buk1 = 0, buk2 = 10):
#
#     if len(lsti) == 10:
#         return sum(min(lsti))
#     if sum(lsti[buk1:buk2]):
#         return sum(lsti[buk1:buk2])
#     else:
#         return cpisik(min((lsti[buk1 + 1:])))
# print("результат суммы:")
# print(cpisik(a))

##########################6

from datetime import datetime
import calendar

date1 = datetime(2000, 1, 1)
date2 = datetime(2000, 10, 1)
a = (date2 - date1).days
def god():
    if calendar.isleap(year=2000):
        print("Год високосный")
    else:
        print("Год не високосный")
print(f"Разница:{a} дня.")
print(god())
