import mysql.connector

# membuat sebuah class yang akan terhubung ke database


class Db_cart:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_cart"
        )
        self.mycursor = self.mydb.cursor()
    # untuk membuat table di database

    def create(self, sql):
        self.mycursor.execute(sql)

    # untuk mengambil data dari database
    def get(self, sql):
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        return myresult

    # untuk merubah data dari database
    def post(self, sql):
        self.mycursor.execute(sql)
        self.mydb.commit()

    # untuk insert banyak data ke database
    def insert_banyak(self, sql, value):
        self.mycursor.executemany(sql, value)
        self.mydb.commit()


# membuat table barang
def create_table_menu():
    Id = "id int auto_increment primary key"
    nama = "nama varchar(45)"
    harga = "harga int(12)"
    sql = f"create table menu ({Id},{nama},{harga})"
    Db_cart().create(sql)
    perintah = "insert into menu (nama, harga) values (%s, %s)"
    value = [
        ("Bakso", "20000"),
        ("Ayam Geprek", "15000"),
        ("Nasi Goreng", "12000"),
        ("Sate Taichan", "18000"),
        ("Pizza", "25000"),
        ("Teh Poci", "5000"),
        ("Teh Tawar", "3000"),
        ("Kopi Hitam", "8000"),
        ("Cappucino Cincau", "7000"),
        ("Pop Ice", "6000")
    ]
    Db_cart().insert_banyak(perintah, value)
    print("\nBerhasil Membuat Table Menu & isinya")
