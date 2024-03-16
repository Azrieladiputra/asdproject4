class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Perabot:
    def __init__(self, nomor, nama, harga, stok, kualitas):
        self.nomor = nomor
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kualitas = kualitas

class CRUD:
    def __init__(self):
        self.head = None

    def tambah_barang_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_barang_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_barang_antara(self, prev_data, data):
        new_node = Node(data)
        if prev_data is None:
            print("Data sebelumnya tidak ditemukan.")
            return
        new_node.next = prev_data.next
        prev_data.next = new_node

    def hapus_barang(self, nomor):
        temp = self.head
        prev = None
        if temp is not None and temp.data['nomor'] == nomor:
            self.head = temp.next
            temp = None
            return
        while temp is not None and temp.data['nomor'] != nomor:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Barang tidak ditemukan.")
            return
        prev.next = temp.next
        temp = None

    def lihat_barang(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def update_stok(self, nomor, stok):
        temp = self.head
        while temp:
            if temp.data['nomor'] == nomor:
                temp.data['stok'] = stok
                return
            temp = temp.next
        print("Barang tidak ditemukan.")

    def _quick_sort(self, arr, low, high, key):
        if low < high:
            pi = self._partition(arr, low, high, key)
            self._quick_sort(arr, low, pi - 1, key)
            self._quick_sort(arr, pi + 1, high, key)

    def _partition(self, arr, low, high, key):
        i = (low - 1)
        pivot = arr[high][key]

        for j in range(low, high):
            if arr[j][key] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def sort_barang_by_nomor_asc(self):
        self._sort_barang_by_key('nomor', reverse=False)

    def sort_barang_by_nomor_desc(self):
        self._sort_barang_by_key('nomor', reverse=True)

    def sort_barang_by_nama_asc(self):
        self._sort_barang_by_key('nama', reverse=False)

    def sort_barang_by_nama_desc(self):
        self._sort_barang_by_key('nama', reverse=True)

    def _sort_barang_by_key(self, key, reverse=False):
        data_list = self._convert_to_list()
        if data_list:  # Check if list is not empty
            self._quick_sort(data_list, 0, len(data_list) - 1, key=key)
            if reverse:
                data_list.reverse()
            self._update_from_list(data_list)
        else:
            print("Tidak ada barang dalam daftar.")

    def _convert_to_list(self):
        data_list = []
        temp = self.head
        while temp:
            data_list.append(temp.data)
            temp = temp.next
        return data_list

    def _update_from_list(self, data_list):
        self.head = None
        for data in data_list:
            self.tambah_barang_akhir(data)
    def fibonacci_search_by_id(self, arr, x):
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib_m = fib_m_minus_1 + fib_m_minus_2

        while fib_m < len(arr):
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib_m
            fib_m = fib_m_minus_1 + fib_m_minus_2

        offset = -1
        while fib_m > 1:
            i = min(offset + fib_m_minus_2, len(arr) - 1)
            if arr[i]['nomor'] < x:
                fib_m = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib_m - fib_m_minus_1
                offset = i
            elif arr[i]['nomor'] > x:
                fib_m = fib_m_minus_2
                fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                fib_m_minus_2 = fib_m - fib_m_minus_1
            else:
                return i
        if fib_m_minus_1 and arr[offset + 1]['nomor'] == x:
            return offset + 1
        return -1

    def fibonacci_search_by_name(self, arr, x):
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib_m = fib_m_minus_1 + fib_m_minus_2

        while fib_m < len(arr):
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib_m
            fib_m = fib_m_minus_1 + fib_m_minus_2

        offset = -1
        while fib_m > 1:
            i = min(offset + fib_m_minus_2, len(arr) - 1)
            if arr[i]['nama'] < x:
                fib_m = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib_m - fib_m_minus_1
                offset = i
            elif arr[i]['nama'] > x:
                fib_m = fib_m_minus_2
                fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                fib_m_minus_2 = fib_m - fib_m_minus_1
            else:
                return i
        if fib_m_minus_1 and arr[offset + 1]['nama'] == x:
            return offset + 1
        return -1
    

def main_menu():
    crud_instance = CRUD()
    while True:
        print("==== Menu ====")
        print("1. Tambah barang di awal")
        print("2. Tambah barang di akhir")
        print("3. Tambah barang di antara")
        print("4. Lihat barang")
        print("5. Hapus barang")
        print("6. Update stok")
        print("7. Sorting")
        print("8. Searching")
        print("8. Keluar")

        menu = int(input("Pilih 1/2/3/4/5/6/7/8: "))

        if menu == 1:
            tambah_barang_awal_menu(crud_instance)
        elif menu == 2:
            tambah_barang_akhir_menu(crud_instance)
        elif menu == 3:
            tambah_barang_antara_menu(crud_instance)
        elif menu == 4:
            lihat_barang_menu(crud_instance)
        elif menu == 5:
            hapus_barang_menu(crud_instance)
        elif menu == 6:
            update_stok_menu(crud_instance)
        elif menu == 7:
            sorting_menu(crud_instance)
        elif menu == 8:
            searching_menu(crud_instance)
        elif menu == 9:
            print("Terima kasih")
            break

def tambah_barang_awal_menu(crud_instance):
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    crud_instance.tambah_barang_awal(data)
    print("Barang telah ditambahkan di awal.")

def tambah_barang_akhir_menu(crud_instance):
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    crud_instance.tambah_barang_akhir(data)
    print("Barang telah ditambahkan di akhir.")

def tambah_barang_antara_menu(crud_instance):
    nomor_sebelumnya = int(input("Nomor barang sebelumnya: "))
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    temp = crud_instance.head
    while temp:
        if temp.data['nomor'] == nomor_sebelumnya:
            crud_instance.tambah_barang_antara(temp, data)
            print("Barang telah ditambahkan di antara.")
            return
        temp = temp.next
    print("Nomor barang sebelumnya tidak ditemukan.")

def lihat_barang_menu(crud_instance):
    print("Daftar Barang:")
    crud_instance.lihat_barang()

def hapus_barang_menu(crud_instance):
    nomor = int(input("Nomor barang yang akan dihapus: "))
    if not crud_instance.head:
        print("Tidak ada barang dalam daftar.")
        return
    crud_instance.hapus_barang(nomor)
    print("Barang telah dihapus.")

def update_stok_menu(crud_instance):
    nomor = int(input("Nomor barang yang akan diupdate stok: "))
    if not crud_instance.head:
        print("Tidak ada barang dalam daftar.")
        return
    stok_baru = int(input("Stok baru: "))
    crud_instance.update_stok(nomor, stok_baru)
    print("Stok barang telah diupdate.")

def sorting_menu(crud_instance):
    print("Pilihan Sorting:")
    print("1. Sort by Nomor (Ascending)")
    print("2. Sort by Nomor (Descending)")
    print("3. Sort by Nama (Ascending)")
    print("4. Sort by Nama (Descending)")

    option = int(input("Pilih 1/2/3/4: "))
    if option == 1:
        crud_instance.sort_barang_by_nomor_asc()
        print("Data berhasil diurutkan berdasarkan Nomor secara Ascending.")
    elif option == 2:
        crud_instance.sort_barang_by_nomor_desc()
        print("Data berhasil diurutkan berdasarkan Nomor secara Descending.")
    elif option == 3:
        crud_instance.sort_barang_by_nama_asc()
        print("Data berhasil diurutkan berdasarkan Nama secara Ascending.")
    elif option == 4:
        crud_instance.sort_barang_by_nama_desc()
        print("Data berhasil diurutkan berdasarkan Nama secara Descending.")
    else:
        print("Pilihan tidak valid.")

def searching_menu(self):
    print("Pilih Searching berdasarkan : ")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan nama")
    

    pilihan = int(input("Pilih 1/2: "))

    if pilihan == 1:
            nomor = int(input("Masukkan nomor barang yang akan dicari: "))
            data_list = self._convert_to_list()
            index = self.fibonacci_search_by_id(data_list, nomor)
            if index != -1:
                print("Barang ditemukan pada indeks:", index)
                print("Detail barang:", data_list[index])
            else:
                print("Barang tidak ditemukan.")
    elif pilihan == 2:
            nama = input("Masukkan nama barang yang akan dicari: ")
            data_list = self._convert_to_list()
            index = self.fibonacci_search_by_name(data_list, nama)
            if index != -1:
                print("Barang ditemukan pada indeks:", index)
                print("Detail barang:", data_list[index])
            else:
                print("Barang tidak ditemukan.")
    else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()
