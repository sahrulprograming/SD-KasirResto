def garis():
    print("+"+"-"*4+"+"+"-"*25+"+"+"-"*10+"+"+"-"*5+"+"+"-"*12+"+")


def struk(keranjang):
    # ====================================================
    # Print judul Kolom
    garis()
    print("|{:^4}|{:^25}|{:^10}|{:^5}|{:^12}|".format(
        "No", "Nama Pesanan", "Harga", "Qty", "SubTotal"))
    garis()
    nomer = 0
    # =====================================================
    total = 0
    # Loping sesuai jumlah data di keranjang index ke 0
    for x in range(len(keranjang[0])):
        nomer += 1
        # Mengambil Nama Pesanan Di dalam Keranjang 3 Dimensi
        nama = keranjang[0][x][0]
        # Mengambil Harga Pesanan Di dalam Keranjang 3 Dimensi
        harga = keranjang[0][x][1]
        # Mengambil subtotal Pesanan Di dalam Keranjang 2 Dimensi
        subtotal = keranjang[2][x]
        # Mengambil jumlah Pesanan Di dalam Keranjang 2 Dimensi
        jumlah = keranjang[1][x]
        total += subtotal

        print("|{:^4}| {:<24}|{:^10}|{:^5}|{:^12}|".format(
            nomer, nama, harga, jumlah, subtotal))
    garis()
    print("{:^48}|{:^12}|".format("", "TOTAL"))
    print("{:^48}+{:^12}+".format("", "-"*12))
    print("{:^48}|{:^12}|".format("", total))
    print("{:^48}+{:^12}+".format("", "-"*12))
    print("\n")
    while True:
        uang_bayar = int(input("Masukan Uang Bayar Anda : "))
        if uang_bayar < total:
            print(" Uang Bayar Kurang ")
        else:
            if uang_bayar > total:
                kembalian = uang_bayar - total
                if kembalian != 0:
                    print("Uang Kembalian Anda :", kembalian)
            print("\n")
            print("{:^62}".format("Terima Kasih"))
            print("{:^62}".format("Selamat Pesan Kembali"))
            break
