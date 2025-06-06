# Program membalik string per baris menggunakan konsep stack

credit = "y"
while credit.lower() == "y":
    print("\n========== Program pembalik string (dengan stack) ==========")
    while True :
        try:
            lines = int(input("Masukkan berapa banyak baris yang diinginkan: "))

            if lines <= 0:
                print("Jumlah baris harus lebih dari 0. Silakan coba lagi.")
                continue
            break  # keluar dari loop jika input valid
        except ValueError:
            print("Input tidak valid! Harus berupa bilangan bulat. Silakan coba lagi.")  

    all_lines = []
    reverse_lines = []

    print("\n============= Input String ==================")
    for i in range(lines):
        line = input(f"Masukkan baris ke-{i+1}: ")
        all_lines.append(line)
    print(all_lines)

    for line in all_lines:
        stack = []
        for char in line:
            stack.append(char)  # push ke stack
        
        reversed_line = ""
        while len(stack) > 0:
            reversed_line += stack.pop()  # pop dari stack
        reverse_lines.append(reversed_line)

    print("\n============== String Awal ==================")
    for line in all_lines:
        print(line)

    print("\n========== String yang Telah Dibalik =========")
    for line in reverse_lines:
        print(line)

    print("\n=============================================")
    while True :
        credit = input("Apakah Anda ingin menjalankan program kembali? [y/n]: ")
        if credit in ["y", "n", "Y", "N"]:
            break
        else:
            print("Input tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    if credit.lower() == "n":
        print("=================================\nProgram selesai, terima kasih!")