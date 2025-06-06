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
    rejected = []
    limit = size

    #input data di awal program
    print("\nMasukan item yang diinginkan ke dalam antrian, ketik [esc] untuk berhenti menginput ")
    while len(queue) < limit:
        item = input("Masukkan item : ")
        if item == "":
            print("item tidak boleh kosong")
        elif item in queue :
            print(f"{item} sudah ada di dalam antrian")
        elif item == "esc" :
            break
        else :
            queue.append(item)
            print(f"{item} ditambahkan ke antrian\n")

    while len(queue) >= limit :
        item = input("Masukkan item : ")
        if item == "":
            print("item tidak boleh kosong")
        elif item == "esc" :
            break
        else :
            rejected.append(item)
            print(f"{item} tidak dapat ditambahkan ke antrian\n")
    
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

    if len(rejected) > 0 :
        print("\nData yang tidak dapat masuk ke antrian : ")
        for item in range(len(rejected) - 1) :
            print(f"{rejected[item]} - ", end = "")
        print(rejected[-1])
                    
    def tambah(): #menambah item ke antrian indeks paling akhir
        print("\n== Menambahkan data ke antrian ==")
        if len(queue) < limit :
            item = input("Masukkan item : ")
            if item == "":
                print("input tidak boleh kosong")
            elif item in queue :
                print(f"{item} sudah ada di dalam antrian")
            else :
                queue.append(item)
                print(f"{item} ditambahkan ke antrian")
        else :
            print("Antrian penuh, hapus data terlebih dahulu jika ingin menambahkan data")
    
    def hapus(): #menghapus item di antrian indeks paling awal
        print("\n== Hapus data [FIFO] ==")
        if len(queue) > 0 :
            item = queue.pop(0) #hapus item di indeks awal
            print(f"{item} dihapus dari antrian")
        else :
            print("Antrian kosong, tidak ada data yang dihapus")

    def s_hapus():
        print("\n== Hapus data spesfifik ==")
        if len(queue) > 0 :
            target = input("Item apa yang ingin dihapus? : ")
            if target in queue :
                    if target == queue[0] :
                        queue.remove(target) #hapus item spesifik
                        print(f"{target} dihapus dari antrian")
                    else :
                        print(f"{target} tidak berada di urutan awal, data tidak dapat dihapus")
            else :
                print(f"{target} tidak terdapat di dalam antrian!")
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

    def cari():
        target = input("\nCari item yang diinginkan : ")
        if target in queue :
            print(f"{target} terdapat di dalam antrian di urutan ke {queue.index(target) + 1}")
        else :
            print(f"{target} tidak terdapat dalam antrian")


    while True :
        try : 
            opsi = (input(f"\nMenu : \n[1]Menambahkan data\n[2]Menghapus data [data paling awal, sesuai input]\n[2a]Menghapus data [spesifik]\n[3]Menampilkan data\n[4]Cari item di antrian\n[5]Selesai\nPilih opsi 1,2,2a,3,4, atau 5 kemudian tekan [enter] : "))
            if opsi == "1" :
                tambah()
            elif opsi == "2" :
                hapus()
            elif opsi == "2a" :
                s_hapus()
            elif opsi == "3" :
                tampil()
            elif opsi == "4" :
                cari()
            elif opsi == "5" :
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