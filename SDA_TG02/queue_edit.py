#program penginputan data ke antrian

credit = "y"
while credit.lower() == "y" :
    print("=== Program Penginputan data tipe antrian ===")
    while True :
        try :
            size = int(input("Tentukan ukuran ruang yang akan digunakan untuk menyimpan data : "))
            if size <= 0 :
                print("ukuran tidak boleh kurang dari 1")
            else:
                break
        except ValueError :
            print("Input tidak valid, masukan kembali dalam bilangan bulat")

    queue = []
    limit = size

    def sort(): #algorima sorting antrian sesuai abjad
        if len(queue) > 0:
            sorted_queue = queue.copy()
            n = len(sorted_queue)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if sorted_queue[j].lower() > sorted_queue[j + 1].lower():
                        sorted_queue[j], sorted_queue[j + 1] = sorted_queue[j + 1], sorted_queue[j]
            for item in range(len(sorted_queue) - 1) :
                print(f"{sorted_queue[item]} - ", end = '')
            print(sorted_queue[-1])
        else :
            print("Antrian masih kosong")

    #input data di awal program
    print("\nMasukan item yang diinginkan ke dalam antrian, ketik [esc] untuk berhenti menginput ")
    while len(queue) < limit:
        item = input("Masukkan item : ")
        if item == "":
            print("item tidak boleh kosong")
        elif item == "esc" :
            break
        else :
            queue.append(item)
            print(f"{item} ditambahkan ke antrian")
            if len(queue) == limit :
                print("\nAntrian penuh!")
                    
    #menampilkan item setelah input awal
    print("\n== Menampilkan isi antrian ==")
    print("Tampilan urutan sesuai input pengguna : ")
    if len(queue) < 1 :
        print("Antrian masih kosong")
    else :
        for item in range(len(queue) - 1) :
            print(f"{queue[item]} - ", end = '')
        print(queue[-1])
    print("\nTampilan yang telah diurutkan sesuai abjad : ")
    sort()
                    
    def tambah(): #menambah item ke antrian indeks paling akhir
        print("\n== Menambahkan data ke antrian ==")
        if len(queue) < limit :
            item = input("Masukkan item : ")
            if item == "":
                print("input tidak boleh kosong")
            else :
                queue.append(item)
                print(f"{item} ditambahkan ke antrian")
        else :
            print("Antrian penuh, hapus data terlebih dahulu jika ingin menambahkan data")
    
    def hapus(): #menghapus item di antrian indeks paling awal
        print("\n== Menghapus data ==")
        if len(queue) > 0 :
            item = queue.pop(0) #hapus item di urutan awal
            print(f"{item} dihapus dari antrian")
        else :
            print("Antrian kosong, tidak ada data yang dihapus")

    def tampil():
        print("\n== Menampilkan isi antrian ==")
        print("Tampilan urutan sesuai input pengguna : ")
        if len(queue) < 1 :
            print("Antrian masih kosong")
        else :
            for item in range(len(queue)-1) :
                print(f"{queue[item]} - ", end = '')
            print(queue[-1])
        print("\nTampilan yang telah diurutkan sesuai abjad : ")
        sort()


    while True :
        try : 
            opsi = int(input(f"\nMenu : \n[1]Menambahkan data\n[2]Menghapus data [data paling awal, sesuai input]\n[3]Menampilkan data\n[4]Selesai\nPilih opsi 1,2,3, atau 4 kemudian tekan [enter] : "))
            if opsi == 1 :
                tambah()
            elif opsi == 2 :
                hapus()
            elif opsi == 3 :
                tampil()
            elif opsi == 4 :
                break
            else :
                print("pilih input sesuai yang tertera pada opsi")
        except ValueError :
            print("input tidak valid, pilih opsi yang tertera")
    
    while True :
        credit = input("\nApakah anda ingin menjalankan program kembali? [y/n]: ")
        if credit.lower() in ['y', 'n']:
            break
        else :
            print("Masukan tidak valid, coba lagi")
    if credit.lower() == "n" :
        print("=======================\nProgram selesai, terima kasih")