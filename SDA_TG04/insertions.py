#Program mengurutkan data dengan metode insertion sort
def asc_insertion(data_list): #mengurutkan data secara ascending / menaik
    print("\n== Pengurutan Data Secara Ascending ==")
    print("Tahapan pengurutan data secara ascending : ")
    for i in range(0, len(data_list)):
        current = i
        while current > 0 and data_list[current - 1] > data_list[current]:
            data_list[current-1], data_list[current] = data_list[current], data_list[current-1]
            current -=1
        print(f"Langkah {i+1} : {str(clean_num(data_list))}")
    return data_list

def des_insertion(data_list): #mengurutkan data secara descending / menurun
    print("\n== Pengurutan Data Secara Descending ==")
    print("Tahapan pengurutan data secara descending : ")
    for i in range(0, len(data_list)):
        current = i
        while current > 0 and data_list[current - 1] < data_list[current]:
            data_list[current-1], data_list[current] = data_list[current], data_list[current-1]
            current -=1
        print(f"Langkah {i+1} : {str(clean_num(data_list))}")
    return data_list

def add_data():
    new_num = float(input("\nTambahkan angka ke dalam list : "))
    if new_num == "":
        print("Input tidak boleh kosong")
    data_list.append(new_num)
    print(f"{new_num} ditambahkan ke list!")

def rm_data():
    if len(data_list) != 0 :
        key = input("\nData mana yang ingin dihapus [Ketik all untuk menghapus semua, kosongkan untuk menghapus data paling akhir]: ")
        if key == "all":
            data_list.clear()
            print(f"semua data telah dihapus")
        elif key == "":
            removed_data = data_list.pop()
            print(f"{removed_data} telah dihapus")
        else:
            removed_data = float(key)
            if removed_data in data_list :
                data_list.remove(removed_data)
                print(f"{removed_data} telah dihapus")
            else:
                print(f"{removed_data} tidak ditemukan!")
    else :
        print("Baris data kosong, tidak dapat menghapus data")

def clean_num(data_list):
    c_data_list = list()
    for data in data_list:
        if data % 1 == 0 :
            c_data_list.append(int(data))
        else:
            c_data_list.append(data)
    return c_data_list

def data_menu(): #menu untuk melakukan perubahan pada data seperti menambah dan menghapus
    while True:
        try: 
            print("\n| Menu Pengeditan Data |")
            print("[1] Menambah data")
            print("[2] Menghapus data")
            print("[3] Mengecek data terkini [belum terurut]")
            print("[4] Keluar dari menu pengeditan data")
            menu_data = int(input("Pilih opsi [1/2/3/4] : "))
            
            if menu_data == 1:
                add_data()
            elif menu_data == 2:
               rm_data()
            elif menu_data == 3 :
                print(f"\nData terkini [belum teurut] : {clean_num(data_list)}")
            elif menu_data == 4 :
                print("Keluar dari menu pengeditan data...")
                break
            else :
                print("input tidak valid pilih 1 s.d 4")
        except ValueError:
            print("Input tidak valid, input hanya berupa angka 1 s.d 4")

def sort_menu(): # menu untuk pengurutan data, jenis apa yang diinginkan ascending, descending atau keduanya
    while True:
        try:
            print("\n| Menu Sorting |")
            print("[1] Ascending (Menaik)")
            print("[2] Descending (Menurun)")
            print("[3] Ascending & Descending (Keduanya)")
            print("[4] Keluar dari menu sorting")
            menu_sort = int(input("Pilih opsi [1/2/3/4] : "))

            if menu_sort == 1:
                print(f"\nData yang telah diurutkan secara ascending (menaik) : {str(asc_insertion(clean_num(data_list.copy())))}\n")
            elif menu_sort == 2:
                print(f"\nData yang telah diurutkan secara descending (menurun) : {str(des_insertion(clean_num(data_list.copy())))}\n")
            elif menu_sort == 3:
                print(f"\nData yang telah diurutkan secara ascending (menaik) : {str(asc_insertion(clean_num(data_list.copy())))}\n")
                print(f"\nData yang telah diurutkan secara descending (menurun) : {str(des_insertion(clean_num(data_list.copy())))}\n")
            elif menu_sort == 4 :
                print("Keluar dari menu...")
                break
            else :
                print("Input tidak valid pilih hanya 1 s.d 4")
                continue
        except ValueError:
            print("Input harus berupa angka [ 1 s.d 4]")
            
while True: #main program
    
    while True:
        try:
            print("\n| Program Pengurutan Data Menggunakan Insertion Sort |")
            data = input("Masukan data yang diinginkan [pisahkan dengan spasi] : ").split() #penginputan data, bisa sekaligus
            if not data :
                print("Input tidak boleh kosong")
                continue
            data_list = list(map(float, data))
            break
        except ValueError:
            print("Input tidak boleh mengandung karakter non-angka")
            
    while True:
        try:
            print("\n| Main Menu Insertion Sort|")
            print("[1] Edit Data [Mengedit list data]")
            print("[2] Sort options [Opsi menampilkan urutan data]")
            print("[3] Keluar dari main menu [Mengakhiri program]")
            main_menu = int(input("Pilih opsi [1/2/3] : "))
        
            if main_menu == 1 :   #opsi menu untuk mengubah data
                data_menu()
            elif main_menu == 2 : #opsi untuk melihat perubahan data yang telah diurutkan
                sort_menu()
            elif main_menu == 3:
                print("Keluar dari main menu...")
                print("Program selesai, terima kasih")
                quit()
            else:
                print("input tidak valid! [pilih 1/2/3]")
        
        except ValueError:
            print("input tidak valid! [input hanya berupa angka 1/2/3]")
