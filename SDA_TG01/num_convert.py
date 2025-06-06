#Program konversi bilangan

credit = "y"
while credit.lower() == "y" :
    while True : #bagian input
        try :
            print("\n============= Program Konversi Bilangan ===========")
            num = float(input("Masukan bilangan yang ingin anda konversikan (input dalam bentuk desimal) : "))
            break
        except ValueError :
            print("Input harus dalam bentuk sistem bilangan desimal")
    
    def konversi(num, basis):

        bilbul = abs(int(num))
        bilkoma = (abs(num) - abs(int(num)))

        stack_bilbul = []
        stack_bilkoma = []
        hasil = ""

        basis_key = {2 : "biner", 8 : "oktal", 16 : "heksadesimal"}
        heksa_key = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
        
        if num < 0 :
            hasil += "-"

        if bilbul == 0 :
            stack_bilbul.append(0)
        
        print(f"\n====== Konversi {basis_key[basis]} ======")
        print("Operasi bilangan bulat")
        while bilbul > 0 :
            sisa_bagi = bilbul % basis
            if basis == 16 and sisa_bagi >= 10 :
                heksa_char = heksa_key[sisa_bagi]
                print(f"{bilbul}\t / {basis} = {int(bilbul/basis)} \t sisa = {sisa_bagi} -> {heksa_char}")
                stack_bilbul.append(heksa_char)
            else :
                print(f"{bilbul}\t / {basis} = {int(bilbul/basis)} \t sisa = {sisa_bagi}")
                stack_bilbul.append(sisa_bagi)
            bilbul //= basis
        print(f"Isi stack dari operasi bilangan bulat : {stack_bilbul}\n")
        
        print("Operasi bilangan koma")
        if bilkoma > 0 :
            count = 0
            while bilkoma > 0 and count < 4:
                bilkoma *= basis
                angka_bulat = int(bilkoma)
                if basis == 16 and angka_bulat >= 10 :
                    heksa_char = heksa_key[angka_bulat]
                    print(f"{round(bilkoma, 2)/basis}\t * {basis} = {round(bilkoma, 2)} \t diambil = {angka_bulat} -> {heksa_char}")
                    stack_bilkoma.append(heksa_char)
                else :
                    print(f"{round(bilkoma, 2)/basis}\t * {basis} = {round(bilkoma, 2)} \t diambil = {angka_bulat}")
                    stack_bilkoma.append(angka_bulat)
                bilkoma -= angka_bulat
                count += 1
        print(f"Isi stack dari operasi bilangan koma : {stack_bilkoma}\n")
        
        while len(stack_bilbul) > 0 :
            hasil += str(stack_bilbul.pop())
        if len(stack_bilkoma) > 0 :
            hasil += "."
            for item in stack_bilkoma :
                hasil += str(item)

        return hasil
                 
    print(f"Hasil konversi dari {num} desimal ke biner adalah {konversi(num,2)}")
    print(f"\nHasil konversi dari {num} desimal ke oktal adalah {konversi(num,8)}")
    print(f"\nHasil konversi dari {num} desimal ke heksadesimal adalah {konversi(num,16)}")
        
    print("\n=============================================")
    while True :
        credit = input("Apakah Anda ingin menjalankan program kembali? [y/n]: ") #konfirmasi loop program
        if credit.lower() in ["y", "n"]:
            break
        else:
            print("Input tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    if credit.lower() == "n":
        print("=================================\nProgram selesai, terima kasih!")