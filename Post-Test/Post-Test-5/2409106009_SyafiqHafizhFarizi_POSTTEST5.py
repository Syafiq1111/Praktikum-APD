akun = [["admin", "admin1", "admin"], ["user", "user1", "user"]]
kendaraan = [
    ["Mobil CRV","KT 1567 DWA", "ready"],
    ["Mobil Pajero", "KT 905 TGT", "ready"],
    ["Mobil Fortuner","KT 4490 FIQ", "ready"],
    ["Motor CBR 250","KT 1910 RRQ", "ready"],
    ["Motor R15 V3","KT 1109 BTR", "ready"],
]
rental = []

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

    # LOGIN ADMIN= USERNAME=admin PASSWORD=admin1
    # LOGIN USER= USERNAME=user PASSWORD=user1 BISA JUGA DENGAN REGISTER DULU

    if hasil_pilih == "1":
        new_username = input("Masukkan username baru: ")
        new_password = input("Masukkan password baru: ")

        if any(user[0] == new_username for user in akun):
            print("Username sudah digunakan!")
        else:
            akun.append([new_username, new_password, "user"])
            print("Pendaftaran berhasil! Silakan login.")

    elif hasil_pilih == "2":
        username = input("Username: ")
        password = input("Password: ")

        for user in akun:
            if user[0] == username and user[1] == password:
                status = user[2]
                break
        else:
            print("Login gagal! Username atau password salah.")
            continue

        print(f"Login berhasil! Anda masuk sebagai {status}.")

        if status == "admin":
            while True:
                print("""
                ===========================================
                |                Menu admin               |
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
                    kendaraan.append([nama_kendaraan, plat_nomor, "ready"])
                    print("Kendaraan berhasil ditambahkan.")

                elif pilih_admin == "2":
                    if kendaraan:
                        for i, status_kendaraan in enumerate(kendaraan):
                            print(f"{i+1}. {status_kendaraan[0]} ({status_kendaraan[1]}) - Status: {status_kendaraan[2]}")
                    else:
                        print("Belum ada kendaraan yang terdaftar.")

                elif pilih_admin == "3":
                    if kendaraan:
                        for i, status_kendaraan in enumerate(kendaraan):
                            print(f"{i+1}. {status_kendaraan[0]} ({status_kendaraan[1]}) - Status: {status_kendaraan[2]}")
                        pilih_kendaraan = int(input("Pilih nomor kendaraan yang akan diupdate: ")) - 1
                        if 0 <= pilih_kendaraan < len(kendaraan):
                            kendaraan[pilih_kendaraan][0] = input("Nama baru kendaraan: ")
                            kendaraan[pilih_kendaraan][1] = input("Plat nomor baru: ")
                            print("Data kendaraan berhasil diupdate.")
                        else:
                            print("Nomor kendaraan tidak valid.")
                    else:
                        print("Belum ada kendaraan yang terdaftar.")

                elif pilih_admin == "4":
                    if kendaraan:
                        for i, status_kendaraan in enumerate(kendaraan):
                            print(f"{i+1}. {status_kendaraan[0]} ({status_kendaraan[1]}) - Status: {status_kendaraan[2]}")
                        pilih_kendaraan = int(input("Pilih nomor kendaraan yang akan dihapus: ")) - 1
                        if 0 <= pilih_kendaraan < len(kendaraan):
                            del kendaraan[pilih_kendaraan]
                            print("Kendaraan berhasil dihapus.")
                        else:
                            print("Nomor kendaraan tidak valid.")
                    else:
                        print("Belum ada kendaraan yang terdaftar.")

                elif pilih_admin == "5":
                    print("Logout berhasil.")
                    break

                else:
                    print("Opsi tidak valid!")

        elif status == "user":
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

                if pilih_user == "1":  #Melihat kendaraan kendaraan ready
                    kendaraan_ready = [v for v in kendaraan if v[2] == "ready"]
                    if kendaraan_ready:
                        for i, status_kendaraan in enumerate(kendaraan_ready):
                            print(f"{i+1}. {status_kendaraan[0]} ({status_kendaraan[1]}) - Status: {status_kendaraan[2]}")
                    else:
                        print("Tidak ada kendaraan yang tersedia.")

                elif pilih_user == "2":  #Rental kendaraan
                    kendaraan_ready = [v for v in kendaraan if v[2] == "ready"]
                    if kendaraan_ready:
                        for i, status_kendaraan in enumerate(kendaraan_ready):
                            print(f"{i+1}. {status_kendaraan[0]} ({status_kendaraan[1]}) - Status: {status_kendaraan[2]}")
                        pilih_kendaraan = int(input("Pilih nomor kendaraan untuk disewa: ")) - 1
                        if 0 <= pilih_kendaraan < len(kendaraan_ready):
                            memilih_kendaraan = kendaraan_ready[pilih_kendaraan]
                            memilih_kendaraan[2] = "rental"
                            rental.append([username, memilih_kendaraan[0], memilih_kendaraan[1]])
                            print(f"Kendaraan {memilih_kendaraan[0]} berhasil disewa.")
                        else:
                            print("Nomor kendaraan tidak valid.")
                    else:
                        print("Tidak ada kendaraan yang tersedia untuk disewa.")

                elif pilih_user == "3":  #Mengembalikan kendaraan
                    user_rental = [r for r in rental if r[0] == username]
                    if user_rental:
                        for i, rent in enumerate(user_rental):
                            print(f"{i+1}. {rent[1]} ({rent[2]})")
                        pilih_kendaraan = int(input("Pilih nomor kendaraan untuk dikembalikan: ")) - 1
                        if 0 <= pilih_kendaraan < len(user_rental):
                            kembalikan_kendaraan = user_rental[pilih_kendaraan]
                            for v in kendaraan:
                                if v[1] == kembalikan_kendaraan[2]:
                                    v[2] = "ready"
                                    break
                            rental.remove(kembalikan_kendaraan)
                            print("Kendaraan berhasil dikembalikan.")
                        else:
                            print("Nomor kendaraan tidak valid.")
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