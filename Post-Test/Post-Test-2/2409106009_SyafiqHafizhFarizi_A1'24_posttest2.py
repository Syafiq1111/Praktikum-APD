nama_lengkap = input("nama lengkap= ")
nama_panggilan = input("panggilan= ")
nim = int(input("nim= "))
umur = input ("umur= ")
hobi = input("hobi= ")
asal_daerah = input("asal daerah= ")
prodi = input("prodi= ")
ipk = float(input("ipk= "))

modulus_nim = int(str(nim)[-3:]) 

print (f"Nama lengkap saya adalah {nama_lengkap}, biasanya saya dipanggil {nama_panggilan},"
        f"nim saya adalah {nim}, saya berumur {umur} pada tahun ini, "
        f"saya berasal dari {asal_daerah} pada tahun ini saya keterima di universitas mulawarman prodi {prodi},"
        f"dan target ipk saya untuk lulus dari universitas ini yaitu {ipk}.  ")
print (f" Nim terakhir saya yaitu {modulus_nim}.")