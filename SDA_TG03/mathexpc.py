# Program mengkonversi ekspresi matematika [prefix, infix, postfix]
import re

# Operator yang digunakan dan tingkat prioritasnya
operators = set(['+', '-', '*', '/', '^'])
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

#cek apakah token termasuk ke dalam operator
def is_operator(c):
    return c in operators

# Cek apakah token adalah operand (angka, variabel, pecahan, atau negatif)
def is_operand(token):
    return re.fullmatch(r'-?(?:\d+(?:\.\d+)?|[a-zA-Z_]\w*/[a-zA-Z_]\w*|\d+/\d+|[a-zA-Z_]\w*)', token) is not None

# Menampilkan langkah-langkah dalam bentuk tabel
def print_step_table(title, headers, steps):
    print(f"\n{title}")
    print(" | ".join(f"{h:^15}" for h in headers))
    for row in steps:
        print(" | ".join(f"{str(col):^15}" for col in row))

# Algoritma konversi dari infix ke postfix (menggunakan stack)
def infix_to_postfix(tokens, title="Langkah Infix ke Postfix"):
    output = []
    stack = []
    steps = []
    for token in tokens:
        if is_operand(token):
            output.append(token)  # Operand langsung masuk ke output
        elif token == '(':
            stack.append(token)  # Kurung buka disimpan di stack
        elif token == ')':
            # Jika kurung tutup, keluarkan semua operator dari stack sampai ketemu '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Buang '(' dari stack
        else:
            # Selama masih ada operator di stack yang prioritasnya >= token sekarang
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)  # Simpan operator ke stack
        steps.append((token, ' '.join(stack), ' '.join(output)))
    while stack:
        output.append(stack.pop())  # Keluarkan sisa operator dari stack ke output
        steps.append(("(pop stack)", ' '.join(stack), ' '.join(output)))
    print_step_table(title, ["Token", "Stack", "Output"], steps)
    return output

# Konversi dari infix ke prefix (reverse + konversi ke postfix + reverse lagi)
def infix_to_prefix(tokens):
    tokens = tokens[::-1]  # Balik urutan token
    for i in range(len(tokens)):
        # Tukar posisi '(' dengan ')' dan sebaliknya setelah dibalik
        if tokens[i] == '(':
            tokens[i] = ')'
        elif tokens[i] == ')':
            tokens[i] = '('
    # Ubah ke postfix, lalu reverse hasilnya untuk mendapatkan prefix
    postfix = infix_to_postfix(tokens, title="Langkah Infix ke Prefix [input direverse, dan hasilnya direverse kembali]")
    return postfix[::-1]

# Konversi prefix ke postfix: operator di depan, urutan operand dibalik
def prefix_to_postfix(tokens):
    stack = []
    steps = []
    for token in reversed(tokens):  # Proses dari kanan ke kiri
        if is_operand(token):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"{a} {b} {token}")  # Format postfix: operand operand operator
        steps.append((token, ' | '.join(stack)))
    print_step_table("Langkah Prefix ke Postfix [input direverse]", ["Token", "Stack"], steps)
    return stack[0]

# Konversi prefix ke infix: hasil akhir dalam tanda kurung
def prefix_to_infix(tokens):
    stack = []
    steps = []
    for token in reversed(tokens):  # Proses dari kanan ke kiri
        if is_operand(token):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a} {token} {b})")  # Format infix: (a op b)
        steps.append((token, ' | '.join(stack)))
    print_step_table("Langkah Prefix ke Infix [input direverse]", ["Token", "Stack"], steps)
    return stack[0]

# Konversi postfix ke infix: operator di belakang, operand diproses berurutan
def postfix_to_infix(tokens):
    stack = []
    steps = []
    for token in tokens:
        if is_operand(token):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a} {token} {b})")  # Format infix: (a op b)
        steps.append((token, ' | '.join(stack)))
    print_step_table("Langkah Postfix ke Infix", ["Token", "Stack"], steps)
    return stack[0]

# Konversi postfix ke prefix: operator di belakang, ubah jadi operator, operand, operand
def postfix_to_prefix(tokens):
    stack = []
    steps = []
    for token in tokens:
        if is_operand(token):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"{token} {a} {b}")  # Format prefix: op a b
        steps.append((token, ' | '.join(stack)))
    print_step_table("Langkah Postfix ke Prefix", ["Token", "Stack"], steps)
    return stack[0]

def main():
    while True:
        print("== Program Konversi Ekspresi Matematika ==")
        print("Pilih jenis ekspresi:")
        print("[1] Infix")
        print("[2] Prefix")
        print("[3] Postfix")
        try:
            jenis = int(input("Masukkan pilihan (1/2/3): "))
            if jenis not in [1, 2, 3]:
                print("Input tidak valid. Harap pilih angka 1, 2, atau 3.\n")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.\n")

    ekspresi = input("Masukkan ekspresi matematika (pisahkan dengan spasi): ")
    tokens = ekspresi.split(" ")  #ubah ke bentuk list

    if jenis == 1:
        print("Prefix :", ' '.join(infix_to_prefix(tokens)))
        print("Postfix:", ' '.join(infix_to_postfix(tokens)))
    elif jenis == 2:
        print("Infix  :", prefix_to_infix(tokens))
        print("Postfix:", prefix_to_postfix(tokens))
    elif jenis == 3:
        print("Infix :", postfix_to_infix(tokens))
        print("Prefix:", postfix_to_prefix(tokens))

    while True:
        ulang = input("\nApakah Anda ingin mengulang program? [Y/N]: ").strip().lower()
        if ulang == 'y':
            print()
            main()
            break
        elif ulang == 'n':
            print("Program selesai, terima kasih!")
            break
        else:
            print("Input tidak valid. Harap masukkan Y atau N.")

if __name__ == "__main__":
    main()