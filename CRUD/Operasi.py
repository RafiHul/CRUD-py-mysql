import time
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'crudpy',
    password = 'crudd',
    database = 'tes_py'
)
mycursor = mydb.cursor()


def Read():
    mycursor.execute("SELECT * FROM buku")
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)

    while True:
        ex = input("Ketik (Y) Untuk Kembali Ke Menu: ")
        if ex in ["y","Y"]:
            break

def Create():
    print("===Masukkan data===")
    while True:
        try:
            id_kolom = int(input("Masukkan id kolom : "))
            break
        except:
            print("Masukkan format angka yang benar")
    nama_buku = input("Nama nama buku : ")
    penulis = input("Nama penulis : ")
    while True:
        try:
            jumlah = int(input("Jumlah :"))
            break
        except:
            print("Masukkan format angka yang benar")
    try:     
        sql = "INSERT INTO buku(id_kolom,nama_buku,penulis,jumlah) VALUES (%s,%s,%s,%s)"
        val = (id_kolom,nama_buku,penulis,jumlah)
        mycursor.execute(sql,val)
    except:
        print("gagal membuat database")
        mydb.rollback()
    else:
        print("database berhasil di buat")
        mydb.commit()
    while True:
        ex = input("Ketik (Y) Untuk Kembali Ke Menu: ")
        if ex in ["y","Y"]:
            break

def Update():
    mycursor.execute("SELECT * FROM buku")
    myresult = mycursor.fetchall()
    t = 0
    for i in myresult:
        print(i)
        t += 1
    while True:
        try:
            pilih_data = int(input("Pilih nomor data yang ingin di update : "))
            if pilih_data > t:
                print("Nomer data tidak ada di dalam tabel")
            else:
                break
        except:
            print("masukkan id_kolom yang benar")

    while True:
        pilih_data2 = input("Data mana yang akan di update (nama buku,penulis,jumlah) : ")
        if pilih_data2 == "nama buku":
            nama_buku_baru = input("Masukkan nama data buku yang baru : ")
            sql = "UPDATE buku SET nama_buku = %s WHERE id_kolom = %s"
            val = (nama_buku_baru,pilih_data)
            break
        if pilih_data2 == "penulis":
            penulis_baru = input("Masukkan nama data penulis yang baru : ")
            sql = "UPDATE buku SET penulis = %s WHERE id_kolom = %s"
            val = (penulis_baru,pilih_data)
            break
        if pilih_data2 == "jumlah":
            while True:
                try:
                    jumlah_baru = int(input("Masukkan data jumlah yang baru : "))
                    sql = "UPDATE buku SET jumlah = %s WHERE id_kolom = %s"
                    val = (jumlah_baru,pilih_data)
                    break
                except:
                    print("Masukkan nilai angka bukan huruf")
        else:
            print("Masukkan pilihan yang benar")

    try:
        mycursor.execute(sql,val)
    except:
        print("Database gagal di update")
        mydb.rollback()
    else:
        print("Database berhasil di update")
        mydb.commit()
    
    while True:
        ex = input("Ketik (Y) Untuk Kembali Ke Menu: ")
        if ex in ["y","Y"]:
            break

def Delete():
    mycursor.execute("SELECT id_kolom,nama_buku,penulis,jumlah FROM buku")
    myresult = mycursor.fetchall()
    t = 0
    for i in myresult:
        print(i)
        print(i[2])
        t += 1

    while True:
        try:
            pilih_data = int(input("Pilih nomor data yang ingin di delete : "))
            if pilih_data > t:
                print("Nomer data tidak ada di dalam tabel")
            else:
                break
        except:
            print("masukkan id_kolom yang benar")

    sql = "DELETE FROM buku WHERE id_kolom = %s"
    val = (pilih_data,)

    try:
        mycursor.execute(sql,val)
    except:
        print("Database gagal di hapus")
        mydb.rollback()
    else:
        print("Database berhasil di hapus")
        mydb.commit()
