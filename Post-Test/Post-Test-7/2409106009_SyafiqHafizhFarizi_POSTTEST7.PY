akun = {
    "admin": {"password": "admin1", "jenis": "admin"},
    "user": {"password": "user1", "jenis": "user"}
}

kendaraan = {
    "KT 1567 DWA": {"nama": "Mobil CRV", "status": "ready"},
    "KT 9056 TGT": {"nama": "Mobil Pajero", "status": "ready"},
    "KT 4490 FIQ": {"nama": "Mobil Fortuner", "status": "ready"},
    "KT 1910 RRQ": {"nama": "Motor CBR 250", "status": "ready"},
    "KT 1109 BTR": {"nama": "Motor R15 V3", "status": "ready"}
}

rental = {}

global_akun, global_kendaraan, global_rental = akun, kendaraan, rental
username = None

#FUNGSI PAKE PARAMETER
def tambah_kendaraan(nama_kendaraan, plat_nomor):
    global global_kendaraan
    global_kendaraan[plat_nomor] = {"nama": nama_kendaraan, "status": "ready"}
    print(f"Kendaraan {nama_kendaraan} berhasil ditambahkan.")

#FUNGSI TANPA PARAMETER
def tampilkan_kendaraan():
    global global_kendaraan
    kendaraan_ready = {k: v for k, v in global_kendaraan.items() if v["status"] == "ready"}
    if kendaraan_ready:
        for plat, info in kendaraan_ready.items():
            print(f"{info['nama']} ({plat}) - Status: {info['status']}")
    else:
        print("Tidak ada kendaraan yang tersedia.")

#FUNGSI REKURSIF
def input_username():
    username_input = input("Masukkan username: ")
    if username_input not in akun:
        print("Username tidak ditemukan. Coba lagi.")
        return input_username()
    return username_input

#PROSEDUR
def login():
    global username 
    username = input_username()
    password = input("Masukkan password: ")
    if akun[username]["password"] == password:
        print(f"Login berhasil! Anda masuk sebagai {akun[username]['jenis']}.")
        return akun[username]["jenis"]
    else:
        print("Password salah! Coba lagi.")
        return login() 

#PROSEDUR
def menu_admin():
    print("""
    ===========================================
    |                Menu Admin               |
    ===========================================
    |          1. Tambah kendaraan            |           
    |          2. Melihat list kendaraan      |          
    |          3. Update kendaraan            |     
    |          4. Hapus Kendaraan             |     
    |          5. Cek status rental           |
    |          6. Logout                      |     
    ===========================================
    """)

#FUNGSI PAKE PARAMETER
def cek_rental(username, plat_nomor):
    if username in rental and plat_nomor in rental[username]:
        kendaraan_info = kendaraan[plat_nomor]
        return f"Kendaraan {kendaraan_info['nama']} ({plat_nomor}) sedang disewa oleh {username}."
    else:
        return f"Kendaraan dengan plat {plat_nomor} tidak sedang disewa oleh {username}."

#EROR HANDLING
def input_angka(output):
    try:
        return int(input(output))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
        return input_angka(output)


while True:
    print(
        """
    ===================================
    |   Manajemen Rental Kendaraan    |
    ===================================
    |          1. Register            |           
    |          2. Login               |          
    |          3. Logout              |     
    ===================================
    """
    )
    hasil_pilih = input_angka("Pilih Opsi Masukkan angka (1/2/3): ")

    if hasil_pilih == 1:
        new_username = input("Masukkan username baru: ")
        new_password = input("Masukkan password baru: ")

        if new_username in akun:
            print("Username sudah digunakan!")
        else:
            akun[new_username] = {"password": new_password, "jenis": "user"}
            print("Pendaftaran berhasil! Silakan login.")

    elif hasil_pilih == 2:
        jenis = login()

        if jenis == "admin":
            while True:
                menu_admin()
                pilih_admin = input_angka("Pilih opsi masukkan angka (1/2/3/4/5/6): ")

                if pilih_admin == 1:
                    nama_kendaraan = input("Nama Kendaraan: ")
                    plat_nomor = input("Plat Nomor: ")
                    tambah_kendaraan(nama_kendaraan, plat_nomor)

                elif pilih_admin == 2:
                    tampilkan_kendaraan()

                elif pilih_admin == 3:
                    plat_nomor = input("Masukkan plat nomor kendaraan yang akan diupdate: ")
                    if plat_nomor in kendaraan:
                        kendaraan[plat_nomor]["nama"] = input("Nama baru kendaraan: ")
                        print("Data kendaraan berhasil diupdate.")
                    else:
                        print("Plat nomor kendaraan tidak valid")

                elif pilih_admin == 4:
                    plat_nomor = input("Masukkan plat nomor kendaraan yang akan dihapus: ")
                    if plat_nomor in kendaraan:
                        del kendaraan[plat_nomor]
                        print("Kendaraan berhasil dihapus.")
                    else:
                        print("Plat nomor kendaraan tidak valid.")

                elif pilih_admin == 5:
                    user_rental = input("Masukkan username yang akan dicek: ")
                    plat_nomor = input("Masukkan plat nomor kendaraan yang akan dicek: ")
                    print(cek_rental(user_rental, plat_nomor))

                elif pilih_admin == 6:
                    print("Logout berhasil.")
                    break

                else:
                    print("Opsi tidak valid!")

        elif jenis == "user":
            while True:
                print("""
                ===========================================
                |                Menu User                |
                ===========================================
                |          1. Melihat list kendaraan      |
                |          2. Rental kendaraan            | 
                |          3. Kembaliin kendaraan         |  
                |          4. Logout                      |     
                ===========================================
                """)
                pilih_user = input_angka("Pilih opsi masukkan angka (1/2/3/4): ")

                if pilih_user == 1:
                    tampilkan_kendaraan()

                elif pilih_user == 2:
                    kendaraan_ready = {k: v for k, v in kendaraan.items() if v["status"] == "ready"}
                    if kendaraan_ready:
                        for plat, info in kendaraan_ready.items():
                            print(f"{info['nama']} ({plat}) - Status: {info['status']}")
                        plat_nomor = input("Masukkan plat nomor kendaraan untuk disewa: ")
                        if plat_nomor in kendaraan_ready:
                            kendaraan[plat_nomor]["status"] = "rental"
                            if username not in rental:
                                rental[username] = []
                            rental[username].append(plat_nomor)
                            print(f"Kendaraan {kendaraan_ready[plat_nomor]['nama']} berhasil disewa.")
                        else:
                            print("Plat nomor tidak valid.")
                    else:
                        print("Tidak ada kendaraan yang tersedia untuk disewa.")

                elif pilih_user == 3:
                    if username in rental and rental[username]:
                        for plat_nomor in rental[username]:
                            print(f"{kendaraan[plat_nomor]['nama']} ({plat_nomor})")
                        plat_nomor = input("Masukkan plat nomor kendaraan yang akan dikembalikan: ")
                        if plat_nomor in rental[username]:
                            kendaraan[plat_nomor]["status"] = "ready"
                            rental[username].remove(plat_nomor)
                            print("Kendaraan berhasil dikembalikan.")
                        else:
                            print("Plat nomor tidak valid.")
                    else:
                        print("Anda belum menyewa kendaraan.")

                elif pilih_user == 4:
                    print("Logout berhasil.")
                    break

                else:
                    print("Opsi tidak valid!")

    elif hasil_pilih == 3:
        print("Terima kasih telah merental kendaraan.")
        break

    else:
        print("Opsi tidak valid!")