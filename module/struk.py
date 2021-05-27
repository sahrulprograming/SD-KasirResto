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
        # untuk menampung semua subtotal menjadi total
        total += subtotal
        # print isi Dari data yang ada di dalam keranjang
        print("|{:^4}| {:<24}|{:^10}|{:^5}|{:^12}|".format(
            nomer, nama, harga, jumlah, subtotal))
    garis()
    # Print Total harga
    print("{:^48}|{:^12}|".format("", "TOTAL"))
    print("{:^48}+{:^12}+".format("", "-"*12))
    print("{:^48}|{:^12}|".format("", total))
    print("{:^48}+{:^12}+".format("", "-"*12))
    print("\n")

    # looping Uang bayar
    while True:
        uang_bayar = int(input("Masukan Uang Bayar Anda : "))
        # ketika uang bayar kurang maka akan mengembalikan while true
        if uang_bayar < total:
            print(" Uang Bayar Kurang ")
        # ketika uang bayar tidak kurang masuk ke else
        else:
            # Jika uang bayar melebihi Total maka akan ada Print kembalian
            if uang_bayar > total:
                kembalian = uang_bayar - total
                if kembalian != 0:
                    print("Uang Kembalian Anda :", kembalian)
            print("\n")
            print("{:^62}".format("Terima Kasih"))
            print("{:^62}".format("Selamat Pesan Kembali"))
            # Memberhentikan while True
            break
