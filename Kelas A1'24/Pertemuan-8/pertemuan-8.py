# if

# list = [1,2,3]

# print(list[0])

# x = 0
# assert x != 0

# x - 12
# x.append(10)

# import os

# os.system("PAUSE")

# dict = {
# 'key' : 1
# }

#print(dict['lele'])

#x ?

# print (x)

# num = 10
#  print('hello' + num)

# if num == 10:
#     print(num)

# x = 1
# y = 0
# print (x/y) #error

# try:
#     angka = int(input("Masukkan angka : "))
# except ValueError:
#     print ("Input salah") #jika error
# else:
#     print("selesai") #selebihnya
# finally:
#     print("finale") #selalujalna setelah blok try

# try:
#     nama = str(input("nama anda: .."))
#     if len(nama) > 5:
#         raise ValueError ("Nama tidak bisa lebih dari 5 karakter")
# except ValueError as e:
#     print(e)

# try:
#     nim = input("Masukkan nim anda: ")

#     if not nim:
#         raise ValueError("Nim tidak boleh kosong")
    
#     if not nim.isdigit():
#         raise TypeError ("Nim harus berupa angka")
#     if len(nim) != 10:
#         raise ValueError ("Nim harus 10 digit")
    
# except TypeError as T:
#     print(T)
# except ValueError as E:
#     print(E)

# else:
#     print(f'NIM Anda adalah {nim}')

# finally:
#     print("Program selesai")

path = 'D:\Praktikum-APD\Kelas A124'
# file = open(path, 'w')

# with open(path, 'r') as file:
#     konten = file.read()
#     print(konten)
#     for i in file:
#         print(i, end='')

with open(path, 'w') as file:
    file.write('Shandy,20,pria')
    file.write('yuyun,19,wanita')

with open(path, 'r') as file:
    konten = file.read()
    print(konten)