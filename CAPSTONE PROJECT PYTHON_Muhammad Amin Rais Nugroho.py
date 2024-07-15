# CAPSTONE PROJECT 1. PYTHON
# Membuat program sederhana penjualan barang

# List Fungsi 
# 1. Beli barang
# 2. Tampilkan daftar belanja
# 3. Hapus dari daftar belanja
# 4. Pembayaran
# 5. Top up
# 6. Update Stock
# 7. Hapus Stock
# 8. Tampilkan inventory
# 9. Tambah barang baru
# 10. Main / Menu utama

# Program ini dibuat untuk 2 user ( customer dan staff )

# CODE :
#Data Dumy
inventory = {
    '001': {'name': 'Keyboard', 'price': 500000, 'stock': 15},
    '002': {'name': 'Mouse', 'price': 250000, 'stock': 15},
    '003': {'name': 'Monitor', 'price': 1500000, 'stock': 15},
    '004': {'name': 'Headset', 'price': 700000, 'stock': 15},
    '005': {'name': 'Printer', 'price': 1200000, 'stock': 15},
    '006': {'name': 'Speaker', 'price': 900000, 'stock': 15},
    '007': {'name': 'Laptop', 'price': 8000000, 'stock': 15},
    '008': {'name': 'Tablet', 'price': 3000000, 'stock': 15},
    '009': {'name': 'External Hard Drive', 'price': 1000000, 'stock': 15},
    '010': {'name': 'Graphics Card', 'price': 4000000, 'stock': 15}
}

# Variable daftar belanja untuk menampung data belanja yang akan dibeli
daftar_belanja = []

# Variable saldo pelanggan untuk menampung data uang customer
saldo_pelanggan = 0

# Fungsi 1 Pembelian Barang
def beli_barang():
    tampilkan_inventory() # Menampilkan stock inventory yang tersedia
    
    while True: # Loop untuk memvalidasi ketersediaan stok barang dengan kode barang
        kode = input("\nMasukkan kode barang yang ingin dibeli: ").strip() # Menggunakan strip untuk validasi character blank
        if kode in inventory and inventory[kode]['stock'] > 0: # Memeriksa apakah kode ada di inventory dan stok tersedia
            break
        elif kode in inventory and inventory[kode]['stock'] == 0: # Memeriksa apakah stok habis
            print(f"Maaf, {inventory[kode]['name']} tidak tersedia saat ini.")
            return
        else:
            print("Masukkan kode barang yang valid dan tersedia.")

    while True: # Loop untuk memvalidasi jumlah stok yang diinput
        jumlah = input(f"Masukkan jumlah {inventory[kode]['name']} yang ingin dibeli: ").strip()
        if jumlah.isdigit() and int(jumlah) > 0 and int(jumlah) <= inventory[kode]['stock']: # Memeriksa apakah jumlah valid
            break
        else:
            print("Masukkan jumlah yang valid (harus angka, lebih dari 0, dan tidak lebih dari stok yang tersedia).")

    total_harga = inventory[kode]['price'] * int(jumlah) # Menghitung total harga pembelian
    print(f"Total harga: Rp {total_harga}")
    inventory[kode]['stock'] -= int(jumlah) # Mengurangi jumlah stok yang telah dibeli
    print(f"{jumlah} {inventory[kode]['name']} telah dibeli.")
    daftar_belanja.append({'kode': kode, 'jumlah': int(jumlah)}) # Menambah item ke daftar belanja

    # Memeriksa apakah stok habis setelah pembelian
    if inventory[kode]['stock'] == 0:
        print(f"Stok {inventory[kode]['name']} habis.")
    else:
        print(f"Sisa stok {inventory[kode]['name']}: {inventory[kode]['stock']}")

# Fungsi 2 Menampilkan Daftar Belanja
def tampilkan_daftar_belanja():
    print("Daftar Belanja :\n")
    if daftar_belanja: # Memeriksa apakah daftar belanja tidak kosong
        total = 0
        print("{:<10} {:<20} {:<10} {:<10}".format("Kode", "Nama Barang", "Harga", "Jumlah"))
        print("=" * 50)
        for item in daftar_belanja: # Loop untuk menghitung total harga dari setiap item yang dibeli
            kode = item['kode']
            nama = inventory[kode]['name']
            harga = inventory[kode]['price']
            jumlah = item['jumlah']
            total_item = harga * jumlah
            total += total_item
            print("{:<10} {:<20} {:<10} {:<10}".format(kode, nama, harga, jumlah)) # Menampilkan item dalam bentuk tabel
        print("=" * 50)
        print(f"Total Belanja: Rp {total}\n")
    else:
        print("Belum ada barang yang dibeli.")

# Fungsi 3 Menghapus Daftar Belanja
def hapus_dari_daftar_belanja():
    tampilkan_daftar_belanja() # Menampilkan daftar belanja
    while True: # Loop untuk memvalidasi isi daftar belanja
        if not daftar_belanja: # Memeriksa apakah daftar belanja kosong
            print("Daftar belanja kosong.")
            return 
        
        kode = input("Masukkan kode barang yang ingin dihapus dari daftar belanja: ").strip()
        if kode.isdigit() and any(item['kode'] == kode for item in daftar_belanja): # Memeriksa apakah kode valid dan ada di daftar belanja
            break
        else:
            print("Masukkan kode barang yang valid (harus angka dan sudah ada di dalam daftar belanja).")

    while True: # Loop untuk memvalidasi jumlah yang diinput
        jumlah = input(f"Masukkan jumlah {inventory[kode]['name']} yang ingin dihapus: ").strip()
        if jumlah.isdigit() and int(jumlah) > 0: # Memeriksa apakah jumlah valid
            jumlah = int(jumlah)
            break
        else:
            print("Masukkan jumlah yang valid (harus angka dan lebih dari 0).")

    for item in daftar_belanja: # Loop untuk mencari kode di daftar belanja dan menghapus jumlah barang yang sesuai
        if item['kode'] == kode:
            if item['jumlah'] > jumlah:
                item['jumlah'] -= jumlah
            else:
                daftar_belanja.remove(item)
                inventory[kode]['stock'] += item['jumlah']
                print(f"{item['jumlah']} {inventory[kode]['name']} berhasil dihapus dari daftar belanja.")
            break

# Fungsi 4 Pembayaran
def pembayaran():
    global saldo_pelanggan # Menggunakan variable global
    tampilkan_daftar_belanja() # Menampilkan total belanja dari daftar belanja
    total_pembayaran = 0
    if daftar_belanja: # Memeriksa apakah daftar belanja tidak kosong
        for item in daftar_belanja:
            kode = item['kode']
            jumlah = item['jumlah']
            total_pembayaran += inventory[kode]['price'] * jumlah
        
        print(f"Total pembayaran: Rp {total_pembayaran}")
        
        while True: # Loop untuk konfirmasi pembayaran
            konfirmasi = input("Anda ingin melanjutkan pembayaran? (ya/tidak): ").strip().lower()
            if konfirmasi == 'ya':
                break
            elif konfirmasi == 'tidak':
                print("Pembayaran dibatalkan.")
                return
            else:
                print("Masukkan 'ya' atau 'tidak'.")

        if total_pembayaran <= saldo_pelanggan: # Memeriksa apakah saldo mencukupi
            saldo_pelanggan -= total_pembayaran
            print(f"Pembayaran berhasil. Sisa saldo: Rp {saldo_pelanggan}")
            daftar_belanja.clear() # Mengosongkan daftar belanja setelah pembayaran berhasil
        else:
            print("Maaf, saldo tidak mencukupi untuk melakukan pembayaran.")
    else:
        print("Belum ada barang yang dibeli.")

# Fungsi 5 Top Up Saldo
def top_up(jumlah):
    global saldo_pelanggan
    saldo_pelanggan += jumlah
    print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp {saldo_pelanggan}")

# Fungsi 6 Update Stok
def update_stok():
    tampilkan_inventory() # Menampilkan inventory
    while True: # Loop untuk memvalidasi input kode barang
        kode = input("Masukkan kode barang yang ingin diupdate stoknya: ").strip()
        if kode.isdigit() and kode in inventory:
            break
        else:
            print("Masukkan kode barang yang valid (harus angka dan terdaftar).")

    while True: # Loop untuk memvalidasi tambahan stok yang diinput
        tambahan_stok = input(f"Masukkan tambahan stok untuk {inventory[kode]['name']}: ").strip()
        if tambahan_stok.isdigit() and int(tambahan_stok) > 0:
            break
        else:
            print("Masukkan jumlah stok yang valid (harus angka dan lebih dari 0).")

    stok_sekarang = inventory[kode]['stock']
    inventory[kode]['stock'] = stok_sekarang + int(tambahan_stok)
    print(f"Stok barang {inventory[kode]['name']} berhasil diupdate menjadi {inventory[kode]['stock']}.")

# Fungsi 7 Hapus Stok
def hapus_stok():
    tampilkan_inventory() # Menampilkan inventory
    while True: # Loop untuk memvalidasi input kode barang
        kode = input("Masukkan kode barang yang ingin dihapus dari inventaris: ").strip()
        if kode.isdigit() and kode in inventory:
            break
        else:
            print("Masukkan kode barang yang valid (harus angka dan terdaftar).")

    while True: # Loop untuk memvalidasi jumlah stok yang diinput
        jumlah = input(f"Masukkan jumlah {inventory[kode]['name']} yang ingin dihapus: ").strip()
        if jumlah.isdigit() and int(jumlah) > 0 and int(jumlah) <= inventory[kode]['stock']:
            break
        else:
            print("Masukkan jumlah yang valid (harus angka, lebih dari 0, dan tidak lebih dari stok yang tersedia).")

    inventory[kode]['stock'] -= int(jumlah)
    print(f"{jumlah} {inventory[kode]['name']} berhasil dihapus dari inventaris.")

# Fungsi 8 Tampilkan Inventory
def tampilkan_inventory():
    print("\nInventaris:")
    print("{:<10} {:<20} {:<10} {:<10}".format("Kode", "Nama Barang", "Harga", "Stok"))
    print("=" * 50)
    for kode, barang in inventory.items(): # Loop untuk menampilkan setiap barang di inventory
        status_stok = "Tersedia" 
        if barang['stock'] > 0: 
            print("{:<10} {:<20} {:<10} {:<10}".format(kode, barang['name'], barang['price'], f"{barang['stock']} ({status_stok})"))
        else:
            print("Stok Habis")

# Fungsi 9 Tambah Barang Baru
def tambah_barang_baru():
    global inventory
    tampilkan_inventory() # Menampilkan inventory
    while True: # Loop untuk memvalidasi input nama barang
        nama = input("Masukkan nama barang baru: ").strip()
        if not nama:
            print("Nama barang tidak boleh kosong.")
            continue
        elif any(char.isdigit() for char in nama):
            print("Nama barang tidak boleh mengandung angka.")
            continue
        else:
            break

    while True: # Loop untuk memvalidasi input harga barang
        harga = input("Masukkan harga barang baru (angka): ").strip()
        if harga.isdigit() and int(harga) > 0:
            break
        else:
            print("Harga barang harus dalam angka dan lebih dari 0.")

    # Mencari kode barang baru berikutnya
    if inventory:
        last_code = max(inventory.keys(), key=int)
        new_code = str(int(last_code) + 1).zfill(3)
    else:
        new_code = '001'

    inventory[new_code] = {'name': nama, 'price': int(harga), 'stock': 0}
    print(f"Barang baru '{nama}' dengan kode '{new_code}' dan harga Rp {int(harga)} telah ditambahkan ke inventory.")

# Fungsi 10 Menu Utama
def main():
    while True: # Loop untuk menampilkan menu utama
        print('''
        === Selamat Datang Di R'Store ===

        Silahkan pilih Users :
        1. Customer
        2. Staff
        3. Keluar

        =================================
        ''')
        try: # Blok try untuk memvalidasi input pilihan user
            pilih_user = int(input('\tPilih User : ').strip())
            if pilih_user not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print('\tMasukkan pilihan yang valid (1, 2, atau 3).\n')
            continue

        if pilih_user == 1: # Menu untuk Customer
            while True: # Loop untuk menampilkan menu customer
                print('''
                ========= Menu R'Store =========

                Hallo Customer

                1. Pembelian Barang
                2. List Belanja
                3. Hapus Belanjaan
                4. Pembayaran
                5. Top Up Saldo
                6. Cek Saldo
                7. Menu Utama

                =================================
                ''')
                try: # Blok try untuk memvalidasi input pilihan menu customer
                    menu_cust = int(input('\tSilahkan Pilih Menu : ').strip())
                    if menu_cust not in [1, 2, 3, 4, 5, 6, 7]:
                        raise ValueError
                except ValueError:
                    print('\tMasukkan pilihan yang valid (1-7).\n')
                    continue

                if menu_cust == 1:
                    beli_barang()
                elif menu_cust == 2:
                    tampilkan_daftar_belanja()
                elif menu_cust == 3:
                    hapus_dari_daftar_belanja()
                elif menu_cust == 4:
                    pembayaran()
                elif menu_cust == 5: # Loop untuk memvalidasi jumlah top up saldo
                    while True:
                        jumlah_topup = input("Masukkan jumlah saldo yang ingin ditambahkan: ").replace(' ', '')
                        if jumlah_topup.isdigit() and int(jumlah_topup) > 0:
                            break
                        else:
                            print("Masukkan jumlah saldo yang valid (harus angka dan lebih dari 0).")
                    top_up(int(jumlah_topup))
                elif menu_cust == 6:
                    print(f"Saldo Anda saat ini: Rp {saldo_pelanggan}")
                elif menu_cust == 7:
                    break
                else:
                    print('\tPilihan anda tidak valid\n')
                    print('\tPilih menu yang tersedia\n')

        elif pilih_user == 2: # Menu untuk Staff
            while True: # Loop untuk menampilkan menu staff
                print('''
                ========= Menu R'Store =========

                Hallo Staff

                1. Update Stok
                2. Hapus Stok
                3. Tampilkan Stok
                4. Tambah Barang Baru
                5. Menu Utama

                =================================
                ''')
                try: # Blok try untuk memvalidasi input pilihan menu staff
                    menu_staff = int(input('\tSilahkan Pilih Menu : ').strip())
                    if menu_staff not in [1, 2, 3, 4, 5]:
                        raise ValueError
                except ValueError:
                    print('\tMasukkan pilihan yang valid (1-5).\n')
                    continue

                if menu_staff == 1:
                    update_stok()
                elif menu_staff == 2:
                    hapus_stok()
                elif menu_staff == 3:
                    tampilkan_inventory()
                elif menu_staff == 4:
                    tambah_barang_baru()
                elif menu_staff == 5:
                    break
                else:
                    print('\tPilihan anda tidak valid\n')
                    print('\tPilih menu yang tersedia\n')

        elif pilih_user == 3: # Keluar dari program
            print('\tAnda Keluar Program\n')
            return

if __name__ == "__main__":
    main()
