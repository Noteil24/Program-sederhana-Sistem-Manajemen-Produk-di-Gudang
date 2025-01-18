# Sistem Manajemen Produk Gudang
products = []  # Daftar produk
stack = []  # Stack (LIFO)
queue = []  # Queue (FIFO)

# Fungsi untuk menambah produk
def tambah_produk():
    product_id = input("Masukkan ID Produk: ")
    name = input("Masukkan Nama Produk: ")
    category = input("Masukkan Kategori Produk: ")
    stock = int(input("Masukkan Jumlah Stok: "))
    product = {"ID": product_id, "Name": name, "Category": category, "Stock": stock}
    
    products.append(product)
    stack.append(product)
    queue.append(product)
    
    print("Produk berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua produk
def tampilkan_produk():
    if not products:
        print("Tidak ada produk.\n")
        return
    print(f"{'ID':<10} {'Nama':<30} {'Kategori':<20} {'Stok':<5}")
    print("-" * 70)
    for product in products:
        print(f"{product['ID']:<10} {product['Name']:<30} {product['Category']:<20} {product['Stock']:<5}")
    print()

# Fungsi untuk menghapus produk
def hapus_produk():
    product_id = input("Masukkan ID Produk yang ingin dihapus: ")
    global products
    for product in products:
        if product['ID'] == product_id:
            products.remove(product)
            if product in stack:
                stack.remove(product)
            if product in queue:
                queue.remove(product)
            print("Produk berhasil dihapus.\n")
            return
    print("Produk tidak ditemukan.\n")

# Fungsi untuk mengupdate produk
def update_produk():
    product_id = input("Masukkan ID Produk yang ingin diupdate: ")
    for product in products:
        if product['ID'] == product_id:
            new_name = input("Masukkan Nama Baru: ")
            new_category = input("Masukkan Kategori Baru: ")
            new_stock = int(input("Masukkan Jumlah Stok Baru: "))
            product['Name'] = new_name
            product['Category'] = new_category
            product['Stock'] = new_stock
            print("Produk berhasil diupdate.\n")
            return
    print("Produk tidak ditemukan.\n")

# Fungsi untuk mengurutkan produk berdasarkan stok
def urutkan_produk():
    global products
    products.sort(key=lambda x: x['Stock'])
    print("Produk berhasil diurutkan berdasarkan stok.\n")

# Fungsi pencarian produk berdasarkan nama
def cari_produk():
    target = input("Masukkan Nama Produk yang ingin dicari: ")
    for product in products:
        if target.lower() in product['Name'].lower():
            print(f"Produk Ditemukan: {product}\n")
            return
    print("Produk tidak ditemukan.\n")

# Fungsi untuk menampilkan produk dalam stack
def tampilkan_stack():
    if not stack:
        print("Stack kosong.\n")
        return
    print("\nProduk dalam Stack (LIFO):")
    for product in reversed(stack):
        print(f"{product['ID']} - {product['Name']} ({product['Stock']})")
    print()

# Fungsi untuk menampilkan produk dalam queue
def tampilkan_queue():
    if not queue:
        print("Queue kosong.\n")
        return
    print("\nProduk dalam Queue (FIFO):")
    for product in queue:
        print(f"{product['ID']} - {product['Name']} ({product['Stock']})")
    print()

# Menu utama
def menu():
    while True:
        print("=== Manajemen Produk Gudang ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Urutkan Produk Berdasarkan Stok")
        print("6. Cari Produk")
        print("7. Tampilkan Produk di Stack (LIFO)")
        print("8. Tampilkan Produk di Queue (FIFO)")
        print("9. Keluar")
        
        choice = input("Pilih menu (1-9): ")
        print()
        if choice == "1":
            tambah_produk()
        elif choice == "2":
            tampilkan_produk()
        elif choice == "3":
            update_produk()
        elif choice == "4":
            hapus_produk()
        elif choice == "5":
            urutkan_produk()
        elif choice == "6":
            cari_produk()
        elif choice == "7":
            tampilkan_stack()
        elif choice == "8":
            tampilkan_queue()
        elif choice == "9":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# Jalankan program
if __name__ == "__main__":
    menu()
