class Stack:
    def __init__(self):
        self.items = []  # Stack disimpan dalam list

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # Menambahkan item ke atas stack

    def pop(self):
        if self.is_empty():
            return None  # Stack kosong
        return self.items.pop()  # Menghapus item paling atas

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]  # Melihat item paling atas tanpa menghapus

    def size(self):
        return len(self.items)

stack = Stack()

print("Masukkan data ke stack (ketik 'n' untuk berhenti):")
while True:
    item = input("Item: ")
    if item.lower() == "n":
        break
    stack.push(item)

print("\n=== semua item dari stack ===")
if stack.is_empty():
    print("Stack kosong.")
else:
    while not stack.is_empty():
        print(stack.pop())