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
    hasil_pilih = input("Pilih Opsi Masukkan angka (1/2/3): ")

    if hasil_pilih == "1":
        new_username = input("Masukkan username baru: ")
        new_password = input("Masukkan password baru: ")

        if new_username in akun:
            print("Username sudah digunakan!")
        else:
            akun[new_username] = {"password": new_password, "jenis": "user"}
            print("Pendaftaran berhasil! Silakan login.")

    elif hasil_pilih == "2":
        username = input("Username: ")
        password = input("Password: ")

        if username in akun and akun[username]["password"] == password:
            jenis = akun[username]["jenis"]
            print(f"Login berhasil! Anda masuk sebagai {jenis}.")
        else:
            print("Login gagal! Username atau password salah.")
            continue

        if jenis == "admin":
            while True:
                print("""
                ===========================================
                |                Menu Admin               |
                ===========================================
                |          1. Tambah kendaraan            |           
                |          2. Melihat list kendaraan      |          
                |          3. Update kendaraan            |     
                |          4. Hapus Kendaraan             |     
                |          5. Logout                      |     
                ===========================================
                """)
                pilih_admin = input("Pilih opsi masukkan angka (1/2/3/4/5): ")

                if pilih_admin == "1":
                    nama_kendaraan = input("Nama Kendaraan: ")
                    plat_nomor = input("Plat Nomor: ")
                    kendaraan[plat_nomor] = {"nama": nama_kendaraan, "status": "ready"}
                    print("Kendaraan berhasil ditambahkan.")

                elif pilih_admin == "2":
                    if kendaraan:
                        for plat, info in kendaraan.items():
                            print(f"{info['nama']} ({plat}) - Status: {info['status']}")
                    else:
                        print("Belum ada kendaraan yang terdaftar.")

                elif pilih_admin == "3":
                    plat_nomor = input("Masukkan plat nomor kendaraan yang akan diupdate: ")
                    if plat_nomor in kendaraan:
                        kendaraan[plat_nomor]["nama"] = input("Nama baru kendaraan: ")
                        print("Data kendaraan berhasil diupdate.")
                    else:
                        print("Plat nomor kendaraan tidak valid.")

                elif pilih_admin == "4":
                    plat_nomor = input("Masukkan plat nomor kendaraan yang akan dihapus: ")
                    if plat_nomor in kendaraan:
                        del kendaraan[plat_nomor]
                        print("Kendaraan berhasil dihapus.")
                    else:
                        print("Plat nomor kendaraan tidak valid.")

                elif pilih_admin == "5":
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
                pilih_user = input("Pilih opsi masukkan angka (1/2/3/4): ")

                if pilih_user == "1":  # Melihat kendaraan ready
                    kendaraan_ready = {k: v for k, v in kendaraan.items() if v["status"] == "ready"}
                    if kendaraan_ready:
                        for plat, info in kendaraan_ready.items():
                            print(f"{info['nama']} ({plat}) - Status: {info['status']}")
                    else:
                        print("Tidak ada kendaraan yang tersedia.")

                elif pilih_user == "2":  # Rental kendaraan
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

                elif pilih_user == "3":  # Mengembalikan kendaraan
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

                elif pilih_user == "4":
                    print("Logout berhasil.")
                    break

                else:
                    print("Opsi tidak valid!")

    elif hasil_pilih == "3":
        print("Terima kasih telah merental kendaraan.")
        break

    else:
        print("Opsi tidak valid!")
