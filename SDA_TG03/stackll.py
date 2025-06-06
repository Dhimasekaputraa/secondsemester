class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        if data.strip() == "":
            print("Input tidak boleh kosong")
        elif self.exists(data):
            print("Data sudah ada, masukkan data lain")
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.size += 1
            print(f"{data} dimasukkan ke dalam stack")

    def exists(self, data):
        current = self.top
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def pop(self):
        if self.top is None:
            print("Stack kosong, tidak dapat menghapus data")
        else:
            removed_data = self.top.data
            self.top = self.top.next
            self.size -= 1
            print(f"{removed_data} dihapus dari stack")
    
    def display(self):
        if self.top is None:
            print("Stack masih kosong")
        else:
            current = self.top
            print("\nBerikut isi dari stack:")
            while current:
                print(f"{current.data}")
                current = current.next

    def stackSize(self):
        print(f"Ukuran stack saat ini adalah : {self.size}")

    def search(self):
        if self.top is None:
            print("Stack masih kosong")
        else:
            key = input("\nData apa yang ingin Anda cari? : ")
            current = self.top
            found = False
            while current:
                if current.data == key:
                    found = True
                    break
                current = current.next
            if found:
                print(f"{key} ditemukan di dalam stack")
            else:
                print(f"{key} tidak ditemukan dalam stack")
    
    def peek(self):
        if self.top is None:
            print("Stack masih kosong")
        else:
            print(f"Data paling puncak adalah {self.top.data}")

# Program utama
while True:
    print("\n== Implementasi Stack menggunakan Linked List ==\n")
    stack = StackLinkedList()

    # Input awal
    print("Penginputan data\nMasukkan data ke dalam stack, ketik [x] jika ingin berhenti menginput\n")
    while True:
        data = input("Masukkan data ke dalam stack : ")
        if data.lower() == "x":
            break
        stack.push(data)

    # Main menu
    while True:
        print("\n== Main menu ==")
        print("[1] Menambah data")
        print("[2] Menghapus data")
        print("[3] Menampilkan data")
        print("[4] Ukuran Stack")
        print("[5] Mencari data")
        print("[6] Data puncak")
        print("[7] Keluar")
        try:
            menu = int(input("\nPilih opsi 1 s.d 7 : "))
        except ValueError:
            print("Harus berupa angka!")
            continue

        if menu == 1:
            data = input("Tambahkan data yang diinginkan: ")
            stack.push(data)
        elif menu == 2:
            stack.pop()
        elif menu == 3:
            stack.display()
        elif menu == 4:
            stack.stackSize()
        elif menu == 5:
            stack.search()
        elif menu == 6:
            stack.peek()
        elif menu == 7:
            print("Keluar dari menu...")
            break
        else:
            print("Input tidak valid!")

    while True:
        rerun = input("Apakah Anda ingin menghentikan program? [Y/N] : ").lower()
        if rerun == "y":
            print("Program selesai, terima kasih!")
            exit()
        elif rerun == "n":
            break
        else:
            print("Input tidak valid! Harap masukkan Y atau N.")