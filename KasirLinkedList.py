import os


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Data_Kasir:
    def __init__(self, id, nama, password):
        self.id = id
        self.nama = nama
        self.password = password


class LL_Admin:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def check_id_dan_password(self, id, password):
        temp = self.head
        while temp is not None:
            if temp.value.id == id:
                if temp.value.password == password:
                    return True
                else:
                    return False
            temp = temp.next
        else:
            return False

    def Tambah_Kasir(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_data_kasir(self):
        temp = self.head
        while temp is not None:
            print(
                f"ID\t: {temp.value.id}\nNAMA\t: {temp.value.nama}\nPASSWORD: {temp.value.password}\n", "="*19)
            temp = temp.next

    def upadate_data_kasir(self, id, value):
        temp = self.head
        while temp is not None:
            if temp.value.id == id:
                temp.value.nama = value.nama
                temp.value.id = value.id
                temp.value.password = value.password
                break
            temp = temp.next
        else:
            os.system('cls')
            print("="*20)
            print(f"ID {id} Tidak Di Temukan")

    def hapus_data_kasir(self, id):
        temp = self.head
        while temp is not None:
            if temp.value.id == id:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                elif temp == self.head:
                    self.head = temp.next
                    temp.next = None
                elif temp == self.tail:
                    self.tail = pre
                    pre.next = None
                else:
                    pre.next = temp.next
                self.length -= 1
                break
            pre = temp
            temp = temp.next
        else:
            os.system('cls')
            print("="*20)
            print(f"ID {id} Tidak Di Temukan")


class Barang:
    def __init__(self, id, nama, jumlah, harga):
        self.id = id
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga


class LL_kasir:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def tambah_barang(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_barang(self):
        temp = self.head
        while temp is not None:
            print(
                f"ID\t: {temp.value.id}\nNAMA\t: {temp.value.nama}\nJUMLAH\t: {temp.value.jumlah}\nHARGA\t: {temp.value.harga}\n", "="*24)
            temp = temp.next

    def update_barang(self, id, value):
        temp = self.head
        while temp is not None:
            if temp.value.id == id:
                temp.value.nama = value.nama
                temp.value.jumlah = value.jumlah
                temp.value.harga = value.harga
                break
            temp = temp.next

    def hapus_barang(self, id):
        temp = self.head
        while temp is not None:
            if temp.value.id == id:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                elif temp == self.head:
                    self.head = temp.next
                    temp.next = None
                elif temp == self.tail:
                    self.tail = pre
                    pre.next = temp.next
                else:
                    pre.next = temp.next
                self.length -= 1
                break
            pre = temp
            temp = temp.next

    def print_barang_in_menu(self):
        if self.length == 0:
            print("Tidak Ada Barang".center(20))
        temp = self.head
        no = 1
        while temp is not None:
            print(
                f"NO\t: {no}\nNAMA\t: {temp.value.nama}\nHARGA\t: {temp.value.harga}\n")
            no += 1
            temp = temp.next


global data_bar
data_bar = LL_kasir()

global data
data = LL_Admin()


def menu_admin():
    print("="*25)
    print("LOGIN ADMIN".center(25))
    print("="*25)
    password = input("Masukan Password: ")
    if password == "ADMIN":
        os.system('cls')
        while True:
            print("="*20)
            print("MENU ADMIN".center(20))
            print("="*20)
            print("1. Tambah Data Kasir")
            print("2. Tampilkan Data Kasir")
            print("3. Update Data Kasir")
            print("4. Hapus Data Kasir")
            print("5. Keluar Menu Admin")
            print("="*20)
            pilihan = input("Masukan Pilihan\t: ")
            try:
                if int(pilihan) == 1:
                    os.system('cls')
                    print("="*20)
                    id = input("ID\t: ")
                    nama = input("NAMA\t: ").upper()
                    password = input("PASSWORD: ")
                    data_kasir = Data_Kasir(id, nama, password)
                    data.Tambah_Kasir(data_kasir)
                    os.system('cls')
                    print("Data Berhasil Ditambah".center(20))
                elif int(pilihan) == 2:
                    os.system('cls')
                    print("="*20)
                    if data.length == 0:
                        print("Data Kasir Kosong".center(20))
                    else:
                        data.print_data_kasir()
                elif int(pilihan) == 3:
                    os.system('cls')
                    print("="*20)
                    if data.length == 0:
                        print("Data Kasir Kosong".center(20))
                    else:
                        id = input("Masukan ID\t: ")
                        os.system('cls')
                        id_new = input("ID\t: ")
                        nama = input("NAMA\t: ")
                        password = input("PASSWORD: ")
                        data_kasir = Data_Kasir(id_new, nama, password)
                        data.upadate_data_kasir(id, data_kasir)
                        os.system('cls')
                        print("="*20)
                        print("Data Kasir Berhasil Di Update".center(20))
                    pass
                elif int(pilihan) == 4:
                    os.system('cls')
                    print("="*20)
                    if data.length == 0:
                        print("Data Kasir Kosong".center(20))
                    else:
                        id = input("Masukan ID\t: ")
                        data.hapus_data_kasir(id)
                        os.system('cls')
                        print("="*20)
                        print("Data Berhasil Di Hapus".center(20))
                elif int(pilihan) == 5:
                    os.system('cls')
                    return False
                else:
                    os.system('cls')
                    print("="*20)
                    print(f"Tidak Ada Menu {pilihan}".center(20))
            except:
                os.system('cls')
                print("="*20)
                print("Error".center(20))
    else:
      os.system('cls')
      print("Gagal Login".center(20))


def menu_kasir():
    print("="*25)
    print("LOGIN KASIR".center(25))
    print("="*25)
    id = input("Masukan ID\t: ")
    password = input("Masukan Password: ")
    if data.check_id_dan_password(id, password):
        os.system('cls')
        print("Login Berhasil".center(25))
        while True:
            print("="*25)
            print("MENU KASIR".center(25))
            print("="*25)
            print("1. Tambah Data Barang")
            print("2. Tampilkan Data Barang")
            print("3. Update Data Barang")
            print("4. Hapus Data Barang")
            print("5. Keluar Menu Kasir")
            print("="*25)
            pilihan = input("Masukan Pilihan\t: ")
            try:
                if int(pilihan) == 1:
                    os.system('cls')
                    print("="*25)
                    id = input("ID\t:").upper()
                    nama = input("NAMA\t:").upper()
                    jumlah = input("JUMLAH\t:").upper()
                    harga = input("HARGA\t:").upper()
                    data_barang = Barang(id, nama, jumlah, harga)
                    data_bar.tambah_barang(data_barang)
                    os.system('cls')
                    print("="*25)
                    print("Data Berhasil Di Tambah".center(25))
                elif int(pilihan) == 2:
                    if data_bar.length == 0:
                        os.system('cls')
                        print("="*25)
                        print("Data Barang Kosong".center(25))
                    else:
                        os.system('cls')
                        print("="*25)
                        data_bar.print_barang()
                elif int(pilihan) == 3:
                    if data_bar.length == 0:
                        os.system('cls')
                        print("="*25)
                        print("Data Barang Kosong".center(25))
                    else:
                        os.system('cls')
                        print("="*25)
                        id = input("Masukan ID\t:")
                        os.system('cls')
                        print("="*25)
                        id_new = input("ID\t:")
                        nama = input("NAMA\t:")
                        jumlah = input("JUMLAH\t:")
                        harga = input("HARGA\t:")
                        data_barang = Barang(id_new, nama, jumlah, harga)
                        data_bar.update_barang(id, data_barang)
                        os.system('cls')
                        print("="*25)
                        print("Data Berhasil Di Upadate".center(25))
                elif int(pilihan) == 4:
                    if data_bar.length == 0:
                        os.system('cls')
                        print("="*25)
                        print("Data Barang Kosong".center(25))
                    else:
                        os.system('cls')
                        print("="*25)
                        id = input("Masukan ID\t:")
                        os.system('cls')
                        print("="*25)
                        print("Data Berhasil Di Hapus".center(25))
                elif int(pilihan) == 5:
                    os.system('cls')
                    return False
                else:
                    os.system('cls')
                    print("="*25)
                    print(f"Tidak Ada Menu {pilihan}".center(25))
            except:
                os.system('cls')
                print("="*25)
                print("Error Kasir".center(25))
    else:
        os.system('cls')
        print("Login Gagal".center(20))


def menu_pembeli():
    while True:
        print("="*20)
        print("Daftar Barang".center(20))
        print("="*20)
        data_bar.print_barang_in_menu()
        print("="*20)
        pilihan = input("Pilih Barang\t: ")
        try:
            if int(pilihan) == 1:
                pass
        except:
            print("Eror Pembeli".center(20))


while True:
    print("="*20)
    print("MENU".center(20))
    print("="*20)
    print("1. Menu Admin")
    print("2. Menu Kasir")
    print("3. Menu Pembeli")
    print("="*20)
    pilihan = input("Masukan Pilihan\t: ")
    try:
        if int(pilihan) == 1:
            os.system('cls')
            menu_admin()
        elif int(pilihan) == 2:
            os.system('cls')
            menu_kasir()
        elif int(pilihan) == 3:
            os.system('cls')
            menu_pembeli()
        else:
            os.system('cls')
            print("="*20)
            print(f"Tidak Ada Menu {pilihan}".center(20))
    except:
        os.system('cls')
        print("="*20)
        print("Error".center(20))
