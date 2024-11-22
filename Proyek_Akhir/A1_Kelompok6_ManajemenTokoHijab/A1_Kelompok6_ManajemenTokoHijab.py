import pandas as pd #Mengimport pustaka pandas untuk mengelola data dalam format dataframe
import csv #Mengimport pustaka csv untuk membaca dan menulis file CSV
from colorama import init, Fore, Style #Mengimport pustaka calorama untuk memberikan warna pada teks di terminal
import os
import platform
from prettytable import PrettyTable #Mengimpor Prettytabel untuk membuat table pada tampilan menu
from pathlib import Path

#LIST
akun_admin = [['admin', 'admin', 'admin']] #Menyimpan data akun admin 

#TUPLE
users = [] #Daftar untuk menyimpan data users
pesanan = [] #Daftar untuk menyimpan data pesanan
kritik_saran = [] #Daftar untuk menyimpan data kritik dan saran

# Path file relatif terhadap lokasi script
dataproduk_path = Path(__file__).parent / 'dataproduk.csv'
data_pengguna_path = Path(__file__).parent / 'data_pengguna.csv'
kritik_saran_path = Path(__file__).parent / 'kritik_saran.csv'
pesanan_path = Path(__file__).parent / 'pesanan.csv'

def clear_terminal():
    current_os = platform.system().lower()    #Mengecek sistem operasi

    if current_os == "windows":
        os.system('cls')  #Untuk Windows
    else:
        os.system('clear')  #Untuk Linux/MacOS

clear_terminal() #Memanggil fungsi untuk membersihkan terminal

def muat_data_hijab():
    try:
        with open(dataproduk_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return {row["kode_produk"]: row for row in reader}
    except FileNotFoundError:
        print("File 'dataproduk.csv' tidak ditemukan. Mulai dengan data kosong.")
        return {}
data_hijab = muat_data_hijab() #Menyimpan data produk hijab

def simpan_data_hijab():
    if not data_hijab: #Jika data_hijab kosong
        with open(dataproduk_path, mode='w', newline='') as file: #Membuka file CSV untuk ditulis
            writer = csv.writer(file)
            writer.writerow(['kode_produk', 'nama', 'warna', 'stok', 'harga'])  # Menulis header CSV
    else:
        df = pd.DataFrame([{
            'kode_produk': code,
            'nama': item['nama'],
            'warna': item['warna'],
            'stok': item['stok'],
            'harga': item['harga']
        } for code, item in data_hijab.items()]) #Mengubah dictionary data_hijab menjadi DataFrame
        df.to_csv(dataproduk_path, index=False) #Menyimpan DataFrame ke dalam file CSV

def simpan_data_pengguna():
    if users:
        df = pd.DataFrame(users)
        df.to_csv(data_pengguna_path, index=False)

def muat_data_pengguna():
    try:
        df = pd.read_csv(data_pengguna_path)
        for _, row in df.iterrows():
            users.append({
                'username': row['username'],
                'password': row['password'],
                'role': row['role']
            })
    except FileNotFoundError:
        pass

def registrasi_user(username, password):
    if not username.strip():
        raise ValueError("Username tidak boleh kosong")
    if not password.strip():
        raise ValueError("Password tidak boleh kosong")

    for user in users:
        if user["username"] == username:
            raise ValueError("Username telah terdaftar!")

    users.append({
        "username": username,
        "password": password,
        "role": "pengguna biasa"
    })
    simpan_data_pengguna()
    print(f"Registrasi berhasil, {username} telah ditambahkan sebagai pengguna biasa.")


def login():
    try:
        # Membaca data pengguna dari file CSV
        df = pd.read_csv(data_pengguna_path)  
    except FileNotFoundError:
        raise ValueError("Data pengguna belum ada. Silakan registrasi terlebih dahulu.")

    # Meminta username dan password dari pengguna
    global username, password
    username = input("Username: ")
    password = input("Password: ")

    # Memeriksa data di dalam file CSV
    for _, row in df.iterrows():
        if row["username"] == username and row["password"] == password:
            return row["role"]  # Mengembalikan peran pengguna jika cocok

    # Memeriksa kredensial admin
    for akun in akun_admin:
        if username == akun[0] and password == akun[1]:
            return akun[2]

    # Jika tidak cocok, login gagal
    raise ValueError("Login gagal!! Username atau password salah.")


def tampilkan_daftar_pengunjung():
    # Muat data dari file CSV
    pengguna_csv = []
    try:
        df = pd.read_csv(data_pengguna_path)
        for _, row in df.iterrows():
            pengguna_csv.append({
                'username': row['username'],
                'role': row['role']
            })
    except FileNotFoundError:
        print("File 'data_pengguna.csv' tidak ditemukan. Memuat data hanya dari memori.")

    # Gabungkan data dari CSV dan dari variabel users
    semua_pengguna = {user['username']: user for user in pengguna_csv}  # Hindari duplikasi dengan dictionary
    for user in users:
        if user['username'] not in semua_pengguna:  # Tambahkan hanya jika belum ada
            semua_pengguna[user['username']] = user

    # Tampilkan data pengguna
    if not semua_pengguna:
        print("Tidak ada pengguna yang terdaftar.")
    else:
        print("Daftar Pengguna:")
        for username, data in semua_pengguna.items():
            print(f"Username: {username}, Role: {data['role']}")

def tampilkan_produk():
    # Muat data produk dari file CSV
    data_hijab = muat_data_hijab()  # Memuat data terbaru dari CSV

    if not data_hijab:  # Jika tidak ada produk hijab yang tersedia
        print("Tidak ada produk hijab yang tersedia.")
        return

    table = PrettyTable()  # Membuat tabel dengan header
    table.field_names = ["Kode Produk", "Nama", "Warna", "Stok", "Harga (Rp)"]

    for kode_produk, item in data_hijab.items():
        try:
            # Pastikan harga dan stok adalah integer
            stok = int(item["stok"])
            harga = int(item["harga"])
            table.add_row([
                kode_produk,
                item["nama"],
                item["warna"],
                stok,
                f"{harga:,}"  # Format harga dengan pemisah ribuan
            ])
        except ValueError as e:
            print(f"Data tidak valid untuk produk {kode_produk}: {e}")

    print(table)

def tambah_produk():
    try:
        nama = input("Nama: ").strip() #Meminta input nama produk dan validasi agar hanya berisi huruf
        if not nama or not nama.isalpha():
            raise ValueError("Nama harus berupa huruf dan tidak boleh kosong!")

        warna = input("Warna: ").strip()  #Meminta input warna produk dan validasi agar hanya berisi huruf
        if not warna or not warna.isalpha():
            raise ValueError("Warna harus berupa huruf dan tidak boleh kosong!")

        stok_input = input("Stok: ").strip() #Meminta input stok produk dan validasi agar berupa angka positif
        if not stok_input.isdigit() or int(stok_input) <= 0:
            raise ValueError("Stok harus berupa angka positif dan tidak boleh kosong!")
        stok = int(stok_input)

        harga_input = input("Harga: ").strip() #Meminta input harga produk dan validasi agar berupa angka positif
        if not harga_input.isdigit() or int(harga_input) <= 0:
            raise ValueError("Harga harus berupa angka positif dan tidak boleh kosong!")
        harga = int(harga_input)

        kode_produk = str(len(data_hijab) + 1)   #Membuat kode produk berdasarkan jumlah produk yang ada
        
        data_hijab[kode_produk] = {  #Menambahkan produk baru ke dalam data_hijab
            "nama": nama,
            "warna": warna,
            "stok": stok,
            "harga": harga
        }

        simpan_data_hijab()  #Menyimpan data produk hijab
        print(f"\nHijab {nama} berhasil ditambahkan.")  #Menampilkan pesan sukses
    except ValueError as e:
        print(f"Input tidak valid: {e}")  #Menangkap dan menampilkan pesan error untuk input tidak valid


def ubah_produk():
    try:
        if not data_hijab:  # Mengecek apakah tidak ada produk dalam data_hijab
            print("Tidak ada produk hijab yang tersedia.")
            return False

        tampilkan_produk()  # Menampilkan semua produk hijab yang tersedia

        kode_produk = input("Masukkan kode produk yang ingin diubah: ").strip() 
        if kode_produk not in data_hijab:  # Mengecek apakah kode produk valid
            print("Kode produk tidak ditemukan!")
            return False

        # Menampilkan data produk yang akan diubah
        produk_lama = data_hijab[kode_produk]
        print("\nData produk saat ini:")
        print(f"Nama: {produk_lama['nama']}, Warna: {produk_lama['warna']}, Stok: {produk_lama['stok']}, Harga: {produk_lama['harga']}")

        # Meminta input data baru
        nama_baru = input("Nama baru (kosongkan untuk tidak mengubah): ").strip()
        warna_baru = input("Warna baru (kosongkan untuk tidak mengubah): ").strip()
        stok_baru_input = input("Stok baru (kosongkan untuk tidak mengubah): ").strip()
        harga_baru_input = input("Harga baru (kosongkan untuk tidak mengubah): ").strip()

        # Gunakan data lama jika input kosong
        nama_baru = nama_baru if nama_baru else produk_lama['nama']
        warna_baru = warna_baru if warna_baru else produk_lama['warna']
        stok_baru = int(stok_baru_input) if stok_baru_input.isdigit() else int(produk_lama['stok'])
        harga_baru = int(harga_baru_input) if harga_baru_input.isdigit() else int(produk_lama['harga'])

        # Validasi input
        if not nama_baru.isalpha():
            raise ValueError("Nama harus berupa huruf!")
        if not warna_baru.isalpha():
            raise ValueError("Warna harus berupa huruf!")
        if stok_baru <= 0:
            raise ValueError("Stok harus berupa angka positif!")
        if harga_baru <= 0:
            raise ValueError("Harga harus berupa angka positif!")

        # Perbarui data produk
        data_hijab[kode_produk] = {
            "nama": nama_baru,
            "warna": warna_baru,
            "stok": stok_baru,
            "harga": harga_baru
        }

        # Simpan perubahan ke file CSV
        simpan_data_hijab()
        print(f"\nProduk {kode_produk} berhasil diperbarui.")
        return True

    except ValueError as e:  # Menangani error jika input tidak valid
        print(f"Input tidak valid: {e}")
        return False



def hapus_produk():
    try:
        # Mengecek apakah ada produk
        if not data_hijab:
            print("Tidak ada produk hijab yang tersedia.")
            return

        # Menampilkan daftar produk
        tampilkan_produk()

        # Meminta input kode produk untuk dihapus
        kode_produk = input("Masukkan kode produk yang ingin dihapus: ").strip()

        # Mengecek apakah produk ada
        if kode_produk in data_hijab:
            nama_produk = data_hijab[kode_produk]["nama"]
            # Hapus produk dari dictionary
            del data_hijab[kode_produk]
            # Simpan data yang diperbarui ke CSV
            simpan_data_hijab()
            # Perbarui data_hijab dari CSV
            muat_data_hijab()
            print(f"\nHijab '{nama_produk}' berhasil dihapus.")
        else:
            print("\nKode produk tidak valid atau tidak ditemukan!")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def muat_data_kritik_saran():
    try:
        df = pd.read_csv(kritik_saran_path) #Mencoba untuk membaca file CSV 'kritik_saran.csv'
        for index, row in df.iterrows(): #Uterasi setiap baris dalam DataFrame
            kritik_saran.append({ 
                'username': row['username'], #Menambahkan data username 
                'kritik': row['kritik'] #Menambahkan data kririk/saran
            })
    except FileNotFoundError: #Jika file tidak ditemukan
        pass #Tidak melakukan apa-apa, cukup lewatkan

def simpan_data_kritik_saran():
    if kritik_saran: #Mengecek apakah kritik atau saran yang tersimpan dalam list
        df = pd.DataFrame(kritik_saran) #Mengubah list kritik_saran menjadi DataFrame
        df.to_csv(kritik_saran_path, index=False) #Menyimpan DataFrame ke file CSV
    else:
        print("Tidak ada kritik atau saran untuk disimpan.") #Menampilkan pesan jika tidak ada kritik/saran

def masukkan_kritik(username):
    kritik = input("Masukkan kritik atau saran Anda: ") #Meminta pengguna untuk menginputbkritik atau saran
    kritik_saran.append({ #Menambahkan kritik atau saran ke dalam list kritik_saran
        'username': username, #Menyimpan username pengguna yang memberikan kritik
        'kritik': kritik #Menyimpan kritik atau saran dari pengguna
    })
    simpan_data_kritik_saran() #Memanggil fungsi untuk menyimpan kritik dan saran ke file
    print("Terima kasih atas kritik dan sarannya!") #Menampilkan pesan konfirmasi
    menu_pengguna_biasa() #Kembali ke menu pengguna biasa

def tampilkan_kritik_saran():
    if not kritik_saran: #Mengecek apakah list kritik_saran kosong
        print("Belum ada kritik atau saran yang masuk.") #Menampilkan pesan jika tidak ada kritik/saran
    else:
        print("Daftar Kritik dan Saran:") #Menampilkan header daftar kritik dan saran
        for entry in kritik_saran: #Iterasi setiap kritik yang ada dalam list kritik_saran
            print(f"Pengguna: {entry['username']}, Kritik/Saran: {entry['kritik']}") #Menampilkan username dan kritik/saran

def simpan_data_pesanan():
    df = pd.DataFrame(pesanan) #Mengubah list pesanan menjadi DataFrame
    df.to_csv(pesanan_path, index=False) #Menyimpan DataFrame ke file CSV 'pesanan.csv'

# Misalkan username sudah didefinisikan pada proses login sebelumnya

def buat_pesanan():
    try:
        # Memuat data produk dari file CSV ke dalam dictionary
        df = pd.read_csv(dataproduk_path)
        data_hijab = {
            row['kode_produk']: {
                'nama': row['nama'],
                'warna': row['warna'],
                'stok': int(row['stok']),
                'harga': int(row['harga'])
            }
            for _, row in df.iterrows()
        }

        if not data_hijab:  # Mengecek apakah data_hijab kosong
            print("Tidak ada produk hijab yang tersedia.")
            menu_pengguna_biasa()
            return

        # Menampilkan produk hijab yang tersedia
        tampilkan_produk()

        # Meminta input kode produk
        kode_produk = int(input("Masukkan kode produk yang ingin Anda pesan: ").strip())

        if kode_produk in data_hijab:  # Memeriksa apakah kode produk valid
            try:
                # Meminta input jumlah produk yang ingin dipesan
                jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
                if jumlah > data_hijab[kode_produk]['stok']:  # Memeriksa stok
                    print("Jumlah stok tidak mencukupi!")
                    menu_pengguna_biasa()
                    return

                # Mengurangi stok produk
                data_hijab[kode_produk]['stok'] -= jumlah

                # Menyimpan data produk kembali ke CSV
                updated_df = pd.DataFrame([{
                    'kode_produk': kode,
                    'nama': item['nama'],
                    'warna': item['warna'],
                    'stok': item['stok'],
                    'harga': item['harga']
                } for kode, item in data_hijab.items()])
                updated_df.to_csv(dataproduk_path, index=False)

                # Meminta input username di sini
                username = input("Masukkan username Anda: ").strip()

                # Menambahkan pesanan ke dalam daftar pesanan
                pesanan.append({
                    'username': username,  # Menggunakan username yang baru dimasukkan
                    'kode_produk': kode_produk,
                    'nama_produk': data_hijab[kode_produk]['nama'],
                    'jumlah': jumlah,
                    'harga_total': jumlah * data_hijab[kode_produk]['harga']
                })
                simpan_data_pesanan()

                print("Pesanan berhasil dibuat.")
                menu_pengguna_biasa()
            except ValueError:
                print("Jumlah harus berupa angka!")
                menu_pengguna_biasa()
        else:
            print("Kode produk tidak valid!")
            menu_pengguna_biasa()
    except FileNotFoundError:
        print("File produk tidak ditemukan. Silakan tambahkan produk terlebih dahulu.")
        menu_pengguna_biasa()

def tampilkan_pesanan():
    if not pesanan: #Memeriksa apakah list pesanan kosong
        print("Belum ada pesanan yang masuk.") #Menampilkan pesan jika pesanan kosong
    else:
        print("Daftar Pesanan:") #Jika ada pesana, tampilkan header "Daftar Pesanan"
        for order in pesanan: 
            print(f"Pengguna: {order['username']}, Produk: {order['nama_produk']}, Jumlah: {order['jumlah']}, Total Harga: Rp{order['harga_total']}") #Menampilkan informasi pesanan

def tambah_akun_admin():
    username = input("Username baru untuk admin: ") #Meminta input username
    password = input("Password untuk admin: ") #Meminta input password
    akun_admin.append([username, password, "admin"])
    print(f"Akun admin {username} berhasil ditambahkan.") #Menampilkan pesan konfirmasi


def hapus_akun_pengunjung():
    try:
        # Membaca file CSV ke dalam DataFrame
        df = pd.read_csv(data_pengguna_path)

        # Menampilkan daftar pengguna biasa untuk memudahkan
        pengguna_biasa = df[df['role'] == 'pengguna biasa']
        if pengguna_biasa.empty:
            print("Tidak ada akun pengunjung biasa yang terdaftar.")
            return

        print("\nDaftar Pengguna Biasa:")
        print(pengguna_biasa[['username']])

        # Meminta input username dari pengguna yang ingin dihapus
        username = input("Masukkan username pengunjung yang ingin dihapus: ").strip()

        # Memeriksa apakah username ada dan merupakan pengguna biasa
        if not ((df['username'] == username) & (df['role'] == 'pengguna biasa')).any():
            print("Akun tidak ditemukan atau bukan akun pengunjung biasa.")
            return

        # Menghapus baris dari DataFrame
        df = df[~((df['username'] == username) & (df['role'] == 'pengguna biasa'))]

        # Menyimpan DataFrame kembali ke file CSV
        df.to_csv(data_pengguna_path, index=False)
        print(f"Akun {username} berhasil dihapus.")

    except FileNotFoundError:
        print("File 'data_pengguna.csv' tidak ditemukan. Pastikan file tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def menu_pengguna_biasa():
    print(Fore.BLUE + """ 
    ==========================================================================     
                    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗                                 
                    ████╗ ████║██╔════╝████╗  ██║██║   ██║                                 
                    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║                                 
                    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║                                 
                    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝                                 
                    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                                  
                                                                       
      ██████╗ ███████╗███╗   ██╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗ █████╗ 
      ██╔══██╗██╔════╝████╗  ██║██╔════╝ ██╔════╝ ██║   ██║████╗  ██║██╔══██╗
      ██████╔╝█████╗  ██╔██╗ ██║██║  ███╗██║  ███╗██║   ██║██╔██╗ ██║███████║
      ██╔═══╝ ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██║   ██║██║╚██╗██║██╔══██║
      ██║     ███████╗██║ ╚████║╚██████╔╝╚██████╔╝╚██████╔╝██║ ╚████║██║  ██║
      ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                       
                        ██████╗ ██╗ █████╗ ███████╗ █████╗                                     
                        ██╔══██╗██║██╔══██╗██╔════╝██╔══██╗                                    
                        ██████╔╝██║███████║███████╗███████║                                    
                        ██╔══██╗██║██╔══██║╚════██║██╔══██║                                    
                        ██████╔╝██║██║  ██║███████║██║  ██║                                    
                        ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                    
    ============================================================================                                                                 

                        ====================================
                        |     1. TAMPILKAN PRODUK HIJAB    |  
                        |     2. BUAT PESANAN              |
                        |     3. BERIKAN KRITIK/SARAN      |
                        |     4. KELUAR                    |
                        ====================================
    """)
    pilihan_pengguna_biasa = input("Pilih menu: ") #Meminta input dari pengguna untuk memilih menu
    if pilihan_pengguna_biasa == '1': #Jika pilihan adalah 1
        clear_terminal()
        tampilkan_produk() #Menampilkan daftar produk hijab
        menu_pengguna_biasa() #Kembali ke menu pengguna biasa
    elif pilihan_pengguna_biasa == '2': #Jika pilihan adalah 2
        clear_terminal()
        buat_pesanan() #Pengguna akan membuat pesanan
    elif pilihan_pengguna_biasa == '3': #Jika pilihan adalah 3
        clear_terminal()
        masukkan_kritik(username) #Pengguna akan memberikan kritik/saran
    elif pilihan_pengguna_biasa == '4': #Jika pilihan adalah 4
        clear_terminal()
        print("Terimakasih") #Pengguna akan keluar dari menu pengguna biasa dan menampilkan pesan konfirmasi
    else:
        print("Pilihan tidak valid!!") #Jika pilihan tidak valid dan menampilkan pesan kesalahan
        menu_pengguna_biasa() #Kembali ke menu pengguna biasa

def menu_admin():
    print(Fore.BLUE + """
    ======================================
``███╗   ███╗███████╗███╗   ██╗██╗   ██╗            
``████╗ ████║██╔════╝████╗  ██║██║   ██║  
``██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║  
``██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║  
``██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝  
``╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   
                                        
  █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
==========================================                                        
                                        
    ======================================
    |     1. TAMBAHKAN PRODUK            |
    |     2. TAMPILKAN PRODUK            |
    |     3. TAMBAHKAN AKUN ADMIN        |
    |     4. TAMPILKAN DAFTAR PENGUNJUNG |
    |     5. HAPUS AKUN PENGUNJUNG       |
    |     6. UBAH PRODUK                 |
    |     7. HAPUS PRODUK                |
    |     8. LIHAT KRITIK/SARAN          |
    |     9. KELUAR                      |
    ======================================
    """)
    pilihan_admin = input("Pilih menu: ") #Meminta input dari admin untuk memilih menu
    if pilihan_admin == '1': #Jika pilihan adalah 1
        clear_terminal()
        tambah_produk() #Admin akan menambahkan produk
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '2': #Jika pilihan adalah 2
        clear_terminal()
        tampilkan_produk() #Akan menampilkan daftar produk hijab
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '3': #Jika pilihan adalah 3
        clear_terminal()
        tambah_akun_admin() #Akan menambahkan akun admin
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '4': #Jika pilihan adalah 4
        clear_terminal()
        tampilkan_daftar_pengunjung() #Akan menampilkan daftar pengunjung
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '5': #Jika pilihan adalah 5
        clear_terminal()
        hapus_akun_pengunjung() #Admin akan menghapus akun pengunjung
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '6': #Jika pilihan adalah 6
        clear_terminal()
        ubah_produk() #Admin akan mengubah produk hijab
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '7': #Jika pilihan adalah 7
        clear_terminal()
        hapus_produk() #Admin akan menghapus produk hijab
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '8': #Jika pilihan adalah 8
        clear_terminal()
        tampilkan_kritik_saran() #Akan menampilkan daftar kritik/saran
        menu_admin() #Kembali ke menu admin
    elif pilihan_admin == '9': #Jika pilihan adalah 9
        clear_terminal()
        print("Terimakasih") #Admin akan keluar dari menu admin dan menampilkan pesan konfirmasi
    else:
        print("Pilihan tidak valid!!") #Jika pilihan tidak valid dan menampilkan pesan kesalahan
        menu_admin() #Kembali ke menu admin


muat_data_hijab() #Memuat data produk hijab dari file atau database
while True:
    try:
        print(Fore.BLUE + """
        ====================================================================================================================
              
        ███████╗███████╗██╗      █████╗ ███╗   ███╗ █████╗ ████████╗    ██████╗  █████╗ ████████╗ █████╗ ███╗   ██╗ ██████╗ 
        ██╔════╝██╔════╝██║     ██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██╔════╝ 
        ███████╗█████╗  ██║     ███████║██╔████╔██║███████║   ██║       ██║  ██║███████║   ██║   ███████║██╔██╗ ██║██║  ███╗
        ╚════██║██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██╔══██║   ██║       ██║  ██║██╔══██║   ██║   ██╔══██║██║╚██╗██║██║   ██║
        ███████║███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║██║ ╚████║╚██████╔╝
        ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                            
                    ██████╗ ██╗    ████████╗ ██████╗ ██╗  ██╗ ██████╗     ██╗  ██╗██╗     ██╗ █████╗ ██████╗                            
                    ██╔══██╗██║    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔═══██╗    ██║  ██║██║     ██║██╔══██╗██╔══██╗                           
                    ██║  ██║██║       ██║   ██║   ██║█████╔╝ ██║   ██║    ███████║██║     ██║███████║██████╔╝                           
                    ██║  ██║██║       ██║   ██║   ██║██╔═██╗ ██║   ██║    ██╔══██║██║██   ██║██╔══██║██╔══██╗                           
                    ██████╔╝██║       ██║   ╚██████╔╝██║  ██╗╚██████╔╝    ██║  ██║██║╚█████╔╝██║  ██║██████╔╝                           
                    ╚═════╝ ╚═╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚═╝ ╚════╝ ╚═╝  ╚═╝╚═════╝                            
        ====================================================================================================================                                                                                                      
        
                                                ===================================
                                                |          1. REGISTRASI          |
                                                |          2. LOGIN               |    
                                                |          3. KELUAR              |
                                                ===================================
        """)
        pilihan = input("Pilih menu: ") #Meminta input dari pengguna untuk memilih menu

        if pilihan == '1': #Jika pilihan adalah 1
            print("\n====REGISTRASI===")
            username = input("Username: ") #Meminta input username
            password = input("Password: ") #Meminta input password
            registrasi_user(username, password) #Fungsi registrasi untuk membuat akun pengguna
        elif pilihan == '2': #Jika pilihan adalah 2
            print("\n===LOGIN===")
            role = login() #Fungsi login untuk memverifikasi username dan password
            if role == 'pengguna biasa': #Jika rolenya adalah pengguna biasa
                menu_pengguna_biasa() #Menu pengguna biasa jika berhasil login
            elif role == 'admin': #Jika rolenya adalah admin
                menu_admin() #Menu admin jika berhasil login
        elif pilihan == '3': #Jika pilihan adalah 3
            print("Keluar dari program.") #Menampilkan pesan konfirmasi
            break #Menghentikan loop dan keluar dari program
        else:
            print("Pilihan tidak valid!!") #Menangani input yang tidak valid
    except Exception as e:
        print(f"Error: {e}") #Menangani error yang tidak terduga
