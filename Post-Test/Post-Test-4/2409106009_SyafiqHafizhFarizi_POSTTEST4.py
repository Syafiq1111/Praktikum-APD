batas_max_login = 3
username = input("Masukkan nama depan anda= ")
password = int(input("Masukkan 3 digit nim terakhir (Tanpa 0)= "))

while batas_max_login > 0:
    if username == "syafiq" and password == 9:
        print("berhasil login")
        break
    else:
        batas_max_login -= 1
        print("login gagal, coba lagi") 
        
        if batas_max_login > 0: 
            username = input("masukkan nama depan/belakang= ")
            password = int(input("masukkan 3 digit nim terakhir= "))

if batas_max_login == 0:
    print("gagal login karena anda telah gagal login sebanyak 3x")
else:

    while True:
        print("Pilih jenis kelamin")
        print("1 Pria")
        print("2 Wanita")

        jenis_kelamin = int(input("Pilih 1/2= "))
        berat_badan = float(input("Masukkan berat badan dalam hitungan gram tanpa koma= "))
        tinggi_badan = float(input("Masukkan tinggi badan dalam hitungan kilometer= "))
        umur = int(input("Masukkan umur anda= "))

        berat_badan_konv = berat_badan / 1000
        tinggi_badan_konv = tinggi_badan * 100000

        aktivitas_harian = int(input("Masukkan jenis aktivitas harian, 1 Aktivitas minimal (Jarang bergerak), 2 Aktivitas sedang (Olahraga 1-3x Seminggu), 3 Aktivitas tinggi (Olahraga 4-7x Seminggu)= "))
        if aktivitas_harian == 1:
            level_aktivitas_harian = 1.25
        elif aktivitas_harian == 2:
            level_aktivitas_harian = 1.36
        elif aktivitas_harian == 3:
            level_aktivitas_harian = 1.72
        else:
            print("Invalid")

        bmr_pria = (10 * berat_badan_konv) + (6.25 * tinggi_badan_konv) - (5 * umur) + 5
        bmr_wanita = (10 * berat_badan_konv) + (6.25 * tinggi_badan_konv) - (5 * umur) - 161

        if jenis_kelamin == 1:
            bmr_p = bmr_pria * level_aktivitas_harian
            print(f"Jumlah kalori yang dibutuhkan adalah {bmr_p} kalori")
        elif jenis_kelamin == 2:
            bmr_w = bmr_wanita * level_aktivitas_harian
            print(f"Jumlah kalori yang dibutuhkan adalah {bmr_w} kalori")
        else:
            print("Invalid")

        berhenti = input("apakah ingin memulai lagi? (iya/tidak): ")
        if berhenti != 'iya':
            print("Terima kasih!")
            break