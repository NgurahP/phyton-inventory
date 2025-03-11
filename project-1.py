import random
import numpy as np

def kalkulator():
    angka1 = input("Masukkan angka = ")
    angka2 = input("Masukkan angka = ")

    
    if angka1.isdigit() and angka2.isdigit():
        operator = input("masukan operator \n (+,-,*,/) \n =>")
        if(operator == "+"):
            hitung = int(angka1) + int(angka2)
        elif (operator == "-"):
            hitung = int(angka1) - int(angka2)
        elif (operator == "*"):
            hitung = int(angka1) * int(angka2)
        elif (operator == "/"):
            hitung = int(angka1) / int(angka2)
        else:
            hitung = "error"
        print ("Hasil nya = ", hitung)
    else :
        print("input hanya menerima angka")
    
def genapGanjil():
    inputUser = input("masukkan sebuah angka = ")
    
    if inputUser.isdigit():
        cek_angka = inputUser%2
        if (cek_angka == 0):
            hasil_cek="angka genap"
        elif (cek_angka == 1):
            hasil_cek="angka ganjil"
    else :
        hasil_cek="hanya menerima angka"
    
    print(inputUser," adalah ", hasil_cek)

def cekHuruf() :
    inputUser = input("Masukan sebuah huruf = ")
    cekInput = inputUser.lower()
    if len(cekInput) == 1:
        if cekInput.isalpha():
            if cekInput in "aiueo" :
                print ("huruf ", inputUser, " adalah huruf Vokal")
            else :
                print("huruf ", inputUser, " adalah huruf Konsonan")
        else:
            print("yang anda masukan bukan huruf")
    else :
        print ("hanya menerima 1 huruf saja")


# function rumus
def konversiDariCelcius(suhuAwal, konversi):
    if konversi == "r":
        hasil = float(0.8*suhuAwal)
        print("hasil konversi  suhu = ", hasil)
    elif konversi == "k":
        hasil = float(suhuAwal+273.15)
        print("hasil konversi suhu = ", hasil)
    elif konversi == "f":
        hasil = (1.8*suhuAwal+32)
        print("hasil konversi suhu = ", hasil)
    else:
        print("aku pergi")

def koversiDariReamur(suhuAwal, konversi):
    if konversi == "c":
        hasil = 1.25*suhuAwal
        print("hasil konversi suhu = ", hasil)
    elif konversi == "k":
        hasil = 1.25*suhuAwal+273.15
        print("hasil konversi suhu = ", hasil)
    elif konversi == "f":
        hasil = 2.25*suhuAwal+32
        print("hasil konversi suhu = ", hasil)
    else:
        print("aku pergi")

def konversiDariKelvin(suhuAwal, konversi):
    if konversi == "c":
        hasil = suhuAwal-273.15
        print("hasil konversi suhu = ", hasil)
    elif konversi == "r":
        hasilKurang= suhuAwal - 273.15
        hasil = 0.8*hasilKurang
        print("hasil konversi suhu = ", hasil)
    elif konversi == "f":
        hasilKurang= suhuAwal - 273.15
        hasil = 1.8*hasilKurang+32
        print("hasil konversi suhu = ", hasil)
    else:
        print("aku pergi")

def konversiDariFarenheit(suhuAwal, konversi):
    hasilKurang = suhuAwal - 32
    if konversi == "c":
        hasil = 5/9*hasilKurang
        print("hasil konversi suhu = ", hasil)
    elif konversi == "r":
        hasil = 4/5*hasilKurang
        print("hasil konversi suhu = ", hasil)
    elif konversi == "k":
        hasil = 5/9*hasilKurang+273.15
        print("hasil konversi suhu = ", hasil)
    else:
        print("aku pergi")

def konversiSuhu() :
    print("pilih satuan suhu yang ingin di konversi \n =>(C, F, R, K)<= \n")
    satuanSuhu = input("satuan suhu awal : ")
    konversiSatuan = input("konversi ke satuan :")
    cekKonversi = konversiSatuan.lower()
    cekSuhu=satuanSuhu.lower()
    if cekSuhu in "cfrk" and cekKonversi in "cfkr":
        if cekSuhu == cekKonversi :
            print("pilih satuan yang berbeda")
        else:
            suhuAwal = input("masukan angka suhu yang ingin di konversi : ")
            if suhuAwal.isdigit():
                suhuAwal = float(suhuAwal)
                if cekSuhu == "c":
                    konversiDariCelcius(suhuAwal=suhuAwal, konversi=cekKonversi)
                elif cekSuhu == "r":
                    koversiDariReamur(suhuAwal=suhuAwal, konversi=cekKonversi)
                elif cekSuhu == "k":
                    konversiDariKelvin(suhuAwal=suhuAwal, konversi=cekKonversi)
                elif cekSuhu == "f":
                    konversiDariFarenheit(suhuAwal=suhuAwal, konversi=cekKonversi)
                else:
                    print("kok lewat jir")
            else:
                print("masukin angka aja dawg")
    else:
        print("masukkan satuan suhu yang benar")
    
def tabelPerkalian():
    for i in range(1,1001):
        for j in range(1,11):
            print(i ," x ", j ," = ", i * j, "\n")
        print(i,"\n")
    
# def Gacha():
#     fate = input(int("Masukan angka = "))
#     pull = random.sample(range(1, 101), fate)
#     char = random.randint(1,100)
#     while pull != char:

def Gacha():
   # Inisialisasi probabilitas dan percobaan
    probability = 0.01  # 1%
    attempts = 0
    rate = random.randint(1,3)

    while True:
        user_input = input("Masukkan jumlah percobaan gacha (1-10) atau 'n' untuk keluar: ")
        
        if user_input.lower() == 'n':
            print("Terima kasih telah bermain!")
            break
        
        try:
            num_attempts = int(user_input)
            if num_attempts < 1 or num_attempts > 10:
                print("Silakan masukkan angka antara 1 dan 10.")
                continue
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka antara 1 dan 10.")
            continue
        
        for _ in range(num_attempts):
            attempts += 1
            
            if random.random() < probability:
                probability = 0.01
                attempts = 0
                print(f"Selamat! Anda menang pada percobaan ke-{attempts} dengan probabilitas {probability * 100:.2f}%.")
                if rate == 1:
                    print(f"You wim but at what cost")
                    rate = random.randint(2,3)
                elif rate == 2:
                    print(f"so close")
                    rate = 3
                else:
                    print(f"damn")
                    rate = random.randint(1,3)
                break
            else:
                print(f"Sayang sekali, Anda tidak menang pada percobaan ke-{attempts}.")
        
        if attempts >= 70:
            probability = min(probability + 0.01 * num_attempts, 1.0)



def asepTelat():
    nama = input(str("masukkan nama anda = "))
    if nama == "asep":
        print("kamu telat")
    else:
        while nama != "asep" :
            nama = input("masukan nama anda : ")
        if nama == "asep" :
            print("kamu telat")
    
def arrayMahasiswa():
    mahasiswa = ["Ngurah", "Putra", "Asterithon", "Andika"]
    mahasiswa.clear()
    mahasiswa.append("Ngurah Putra")
    mahasiswa.append("Amerta")
    mahasiswa.insert(0,"Gede")
    mahasiswa.remove("Gede")
    mahasiswa.sort()
    for mhs in mahasiswa:
        print(mhs)
    
def toko():
    penjualan = []
    penjualan_seminggu = 7

    for i in range (penjualan_seminggu):
        hasil_penjualan = int(input(f"hasil penjualan hari ke - {i+1} = "))
        penjualan.append(hasil_penjualan)

    penjualan_tertingi = max(penjualan)
    penjualan_terendah = min(penjualan)
    total_penjualan = sum(penjualan)
    rata_penjualan = int(total_penjualan/penjualan_seminggu)

    print(f"penjualan tertinggi = Rp.{penjualan_tertingi}.000")
    print(f"penjualan terendah = Rp.{penjualan_terendah}.000")
    print(f"total penjualan = Rp.{total_penjualan}.000")
    print(f"rata rata penjualan = Rp.{rata_penjualan}.000")

def anak_ayam():
    ayam = 10
    while ayam > 0:
        print(f"Anak ayam ada {ayam} \n turun satu tinggal {ayam-1} \n")
        ayam = ayam -1
        if ayam == 0:
            print(f"sisa induknya")
            break

def hasilTebak (coba):
    tebak=random.randint(1,9)
    tebakan = coba
    
    print(f"anda menebak {tebak} dengan {coba}")
    if tebak != tebakan:
        print("You Suck")
    else:
        print("Nice")
    
def jumlahTebakan ():
    percobaan = int(input("masukan jumlah percobaan untuk menebak angka ="))
    for i in range (percobaan):
        hasilTebak(coba=percobaan)
        i=+1

def testNumpy():
    ary = np.array([54,75,84,4,45,97,23])
    cari = int(input("cari angka pada baris ke = "))
    cariArray= cari-1
    print(ary[cariArray])

def testNumpy2Dimensi ():
    arr = np.array([
        [43,534,65],
        [76,87,83]
        ])
    cari1 = int(input("cari angka pada baris ke = "))
    cariArray1= cari1-1
    cari2 = int(input("cari angka pada baris ke = "))
    cariArray2= cari2-1
    print(arr[cariArray1][cariArray2])

def testNumpy3Dimensi ():
    arr = np.array([
            [
                [43,534,65],
                [79,92,43]
            ],
            [
                [76,87,83],
                [21,54,36]
            ]
        ])
    print("Nilai Minimal = ", arr.min())
    print("posisi Nilai Minimal = ", arr.argmin())
    print("Nilai Maksimal = ", arr.max())
      
    print("shape = ", arr.shape)
    print("Posisi Nilai Maksimal = ", arr.argmax())
    print("Nilai Rata-rata = ", int(arr.mean()))
    print("Total Nilai = ", arr.sum())
    print("Nilai Deviasi= ", int(arr.std()))
      
    # for x in arr:
    #     for y in x:
    #         for z in y:
    #             print(z)
                
    # cari1 = int(input("cari angka pada baris ke = "))
    # cariArray1= cari1-1
    # cari2 = int(input("cari angka pada baris ke = "))
    # cariArray2= cari2-1
    # cari3 = int(input("cari angka pada baris ke = "))
    # cariArray3= cari3-1
    # print(arr[cariArray1][cariArray2][cariArray3])
    
    
# testNumpy2Dimensi()
# testNumpy3Dimensi()

# ##################################  Pemanggilan Fungsi ###################################
# cekHuruf()
# genapGanjil()
# kalkulator()
# konversiSuhu()
# tabelPerkalian()
# Gacha()
# arrayMahasiswa()
# toko()
# anak_ayam()
jumlahTebakan()
