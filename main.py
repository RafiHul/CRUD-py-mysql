import os
import CRUD as CRUD

check_os = os.name
match check_os:
    case "posix": os.system("clear")
    case "nt": os.system("cls")

if __name__ == "__main__":
    while True:
        match check_os:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("====","Selamat datang di perpustakaan","====")
        print("==========","Pilih menu","============")
        print("""
        1. Tambah Data Buku
        2. Lihat Data Buku
        3. Update Data Buku
        4. Hapus Data Buku 
        """)

        user_option = input("Masukkan piihan anda = ")
        if user_option == "1":
            CRUD.create()
        elif user_option == "2":
            CRUD.read()
        elif user_option == "3":
            CRUD.update()
        elif user_option == "4":
            CRUD.delete()
        else:
            print("Masukkan pilihan dengan benar")

        is_done = input("apakah anda ingin keluar dari program (y/n) ? ")
        if is_done in ["y","Y"]:
            print("sukses keluar dari program")
            break
