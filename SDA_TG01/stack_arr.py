#Program implementasi stack dengan array

credit = "y"
while credit.lower() == "y" :
    while True:
        try :
            print("=========== Program Stack Array ============")
            size = int(input("\nMasukan kapasitas tumpukan yang diinginkan : "))
            if size <= 0 :
                print("Ukuran tumpukan harus lebih dari 0")
                continue
            break
        except ValueError :
            print("Input tidak valid, masukan bilangan bulat")

    stack = []
    rejected_item = []
    max_capacity = size
    
    print("Masukan data ke dalam tumpukan, ketik [n] jika ingin berhenti")
    while True:
        input_item = input("Item: ")
        if input_item == "n" :
            break
    
        if len(stack) < size :
            stack.append(input_item)
        else :
            rejected_item.append(input_item)
    
    print("\n======= Isi Tumpukan =========")
    if len(stack) == max_capacity :
        print(f"Tumpukan terisi penuh, dengan isi : ")
        while len(stack) > 0 :
            stack_items = ""
            stack_items += stack.pop()
            print(stack_items)

    elif len(stack) < max_capacity :
        print(f"Tumpukan masih tersisa {max_capacity - len(stack)} slot kosong, isi dari tumpukan :  ")
        while len(stack) > 0 :
            stack_items = ""
            stack_items += stack.pop()
            print(stack_items)
    
    if len(rejected_item) > 0 :    
        print(f"\nData yang tidak dapat dimasukan : ")
        while len(rejected_item) > 0 :
            rejected_items = ""
            rejected_items += rejected_item.pop()
            print(rejected_items)
           
    print("\n=============================================")
    while True :
        credit = input("Apakah Anda ingin menjalankan program kembali? [y/n]: ")
        if credit in ["y", "n", "Y", "N"]:
            break
        else:
            print("Input tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    if credit.lower() == "n":
        print("=================================\nProgram selesai, terima kasih!") 