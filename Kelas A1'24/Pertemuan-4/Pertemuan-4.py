# ulang = 15
# for i in range(ulang):
#     print(f"perulangan ke-{str(i)}")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print (i, end=' ')

# for i in range(1, 10, 2): #(awal, akhir, lompatan)
#     print(i)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print (f"{i} x {j} = {i * j}")
#         print ()

# jawab = 'ya'
# hitung = 0

# while(jawab == 'ya'): #kondisi/syarat
#     hitung += 2
#     jawab = input("ulang lagi tidak? :")
# print(f"total perulangan : {hitung}")

# jawab = 'ya'
# hitung = 0

# while True: #selalu benar
#     hitung += 1 #hitung
#     ulang = input("ulang lagi tidak? : ")
#     if ulang == "tidak" or ulang == "Tidak": #kondisi
#         break
# print (f"total perulangan : {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 3 == 0:
#         continue
#     print(i)

# bilangan = 0
# while True:
#     angka = int(input("Masukkan angka: "))
#     if angka <0:
#         break
#     bilangan += angka
#     print ("Total bilangan:" + str(bilangan))

# for i in range(1, 20, 3):
#     if i % 2 == 0:
#         continue
#     print (i)

buah = ["apel", 'pisang', 'jeruk', 'melon','semangka']
buah_baru = []

for i in buah:
    if "e" in i:
        buah_baru.append(i)
        print(buah_baru)