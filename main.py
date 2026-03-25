# #1
# for num in range(1,11):
#     print(num, end=' ')

# #2
# for py in "python":
#     print( '-', py)

# #3
# ismlar = ["Ali", "Vali", "Dilnoza", "Madina", "Sobir"]
#
# for indeks, ism in enumerate(ismlar, start=1):
#     print(f" {indeks}. {ism}")

# #4
# for number in range(2, 21, 2):
#      if number % 2 == 0:
#          print(number, end=' ')

# #5
# yigindi = 0
# for i in range(1,51):
#     yigindi += i
#
# print(f"1 dan 50 gacha bo'lgan sonlar yig'indisi: ", yigindi)

# #6
# sanoq = 0
# print("1 dan 100 gacha 3 ga bo'linadigan sonlar:")
#
# for son in range(1, 101):
#   if son % 3 == 0:
#     print(son ,end=' ' )
#     sanoq = sanoq + 1
# print("\nJami:", sanoq,  " ta son topildi")

# #7
# matn = input("\nMatn kiriting: ")
#
# unlilar = "aeiouаеёиоуыэюя"
# hisob = 0
#
# for belgi in matn.lower():
#     if belgi in unlilar:
#         hisob = hisob + 1
# print(f"Jami unlilar :", hisob, "ta")

# #8
# sonlar = [45, 12, 89, 34, 67, 23, 91, 56, 78]
# eng_katta_son = sonlar[0]
#
# for son in sonlar:
#     if son > eng_katta_son:
#         eng_katta_son = son
#         print(f"Yangi eng katta son: {eng_katta_son}")
# print(f"Listdagi eng katta son: {eng_katta_son}")

# #9
# sonlar = [34, 12, 89, 5, 67, 23, 91, 45]
#
#
# jami = 0
#
# maksimum = sonlar[0]
# minimum = sonlar[0]
# hisob = 0
#
# for son in sonlar:
#
#     jami += son
#
#     if son > maksimum:
#         maximum = son
#
#     if son < minimum:
#         minimum = son
#
#     hisob = hisob + 1
#
# ortacha = jami / hisob if hisob > 0 else 0
#
# print(f"Sonlar: {sonlar}")
# print(f"Yig'indi: {jami}")
# print(f"Maksimum: {maksimum}")
# print(f"Minimum: {minimum}")
# print(f"O'rtacha: {ortacha}")

#10
