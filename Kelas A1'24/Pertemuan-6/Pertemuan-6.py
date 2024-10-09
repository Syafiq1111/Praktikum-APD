# daftar_buku = {
#     #key      #value
#     "Buku1" : "Harry Postter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twilight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# games = dict(Sekiro = "Action", Pokemon ="Adventure", valorant = "FPS")

# print (games)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra", #STRING
#     "NIM" : 2109106079, #INTEGER
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #LIST
#     "Mahasiswa_Aktif" :True, #BOOLEAN
#     "Social Media" : { #DICTIONARY
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# # print (Biodata["KRS"])
# # print (Biodata.get("Nama"))

# # print (Biodata.get("Alamat", "Kosong bang")) #PRINT YG LAIN

# for i,j in Biodata.items():                #KELUARIN KEY/ VALUE MENGGUNAKAN .items
#     print(f"Key = {i} dan value = {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# #Sebelum Ditambah
# # Film["ZombieLand"] = "Comedy"
# print(Film)
# #Setelah
# Film.update({"Hour" : "Thriller"}) 
# print(Film)

# del Film["The Conjuring"]
# print(Film)

# hapus = Film.pop("The Conjuring")
# print (Film)
# print (f"Key yang dihapus = {hapus}")

# Film.clear()
# print(Film)

# print ("Jumlah data dalam dict Biodata =", len(Biodata))
# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print (buah)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# print (Film)
# print("Film : ", Film.setdefault("Oldbook", "Horror"))
# print(Film)

# for i in Film.values():
#     print (i, end=" ")

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# print(f" sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] = 2023
# print(f" sesudah : {mahasiswa}")

# print(f"sebelum : {mahasiswa}")
# del mahasiswa[111]["Umur"]
# print(f"sesudah : {mahasiswa}")

# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     for keynested, valuenested in j.items():
#         print(f"{keynested} : {valuenested}")

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")