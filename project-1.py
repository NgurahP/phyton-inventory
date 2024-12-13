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
def konversiDariCelcius(suhuAwal, konversi, ):
    if konversi == "r":
        hasil = 0.8*suhuAwal
        print("hasil konversi suhu = ", hasil)
    elif konversi == "k":
        hasil = suhuAwal+273.15
        print("hasil konversi suhu = ", hasil)
    elif konversi == "f":
        hasil = 1.8*suhuAwal+32
        print("hasil konversi suhu = ", hasil)
    else:
        print("aku pergi")
    
    print("gak tau mau ngisi apa")
    
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
    
    print("gak tau mau ngisi apa")

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
    
    print("gak tau mau ngisi apa")

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
    
    print("gak tau mau ngisi apa")

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
    
# cekHuruf()
# genapGanjil()
# kalkulator()
konversiSuhu()
