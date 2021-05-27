# ======================================
# inisialisasi Keranjang 3 Dimensi
# array pertama berisi nama barang & harga satuan
# array kedua berisi Quantity barang
# array ke tiga berisi subtotal harga barang
from module.database import *
from module.struk import *
keranjang = [[], [], []]


def garis():
    print("+"+"-"*4+"+"+"-"*25+"+"+"-"*10+"+")
# ======================================


def run():
    # ======================================
    # inisialisasi Variable List_menu
    list_menu = []
    # ======================================

    # ======================================
    # Query Ke database
    sql = "select nama, harga from barang"
    data = Db_cart().get(sql)
    # ======================================

    # ======================================
    # Print judul Kolom
    print("")
    print("{:^43}".format("Selamat Datang"))
    print("{:^43}".format("Di Restoran Pasti Lezat"))
    print("{:^43}".format(""))
    garis()
    print("|{:^4}|{:^25}|{:^10}|".format("NO", "List Menu", "Harga"))
    garis()
    nomer = 0
    # ======================================

    # ======================================
    # Print Baris Data
    for x in data:
        nomer += 1
        print("|{:^4}| {:<24}| {:<9}|".format(nomer, x[0], x[1]))
        list_menu.append(x)
    garis()
    # ======================================

    u1 = True
    while u1:
        # ======================================
        # Memilih Barang
        pilih = int(input("Masukan Pilihan Menu : "))
        keranjang[0].append(list_menu[pilih-1])
        # input jumlah
        jumlah = int(input("Masukan Jumlah Pesanan : "))
        keranjang[1].append(jumlah)
        # kalkulasi Subtotal
        subtotal = list_menu[pilih-1][1] * jumlah
        keranjang[2].append(subtotal)
        while True:
            ulang = input("Ingin pesan Lagi? (y/t) : ")
            if ulang == "y":
                u1 = True
                break
            elif ulang == "t":
                u1 = False
                break
            else:
                print("Pilih y/t :")
            # ======================================
    # Function Print Struk
    struk(keranjang)
