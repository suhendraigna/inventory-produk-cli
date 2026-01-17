import json
import os

FILE_JSON = "inventory.json"

def load_data():
    if not os.path.exists(FILE_JSON):
        return []

    with open(FILE_JSON, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(FILE_JSON, "w") as file:
        json.dump(data, file, indent=4)

def lihat_barang(data):
    if not data:
        print("Inventory kosong")
        return
    
    print("\nData Barang:")
    for item in data:
        print(
            f"- [{item['kode']}] {item['nama']} | Stok: {item['stok']} | Harga: Rp{item['harga']}"
        )

def tambah_barang(data):
    kode = input("Kode barang: ")
    nama = input("Nama barang: ")

    if not kode or not nama:
        print("Kode dan nama wajib diisi")
        return
    
    try:
        stok = int(input("Stok awal: "))
        harga = int(input("Harga: "))
    except ValueError:
        print("Stok dan harga harus angka")
        return

    data.append({
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga
    })

    save_data(data)
    print("Barang berhasil ditambahkan")

def update_stok(data):
    kode = input("Kode barang: ").strip()

    for item in data:
        if item["kode"] == kode:
            try:
                stok_baru = int(input("Stok baru: "))
            except ValueError:
                print("Stok harus angka")
                return
            
            item["stok"] = stok_baru
            save_data(data)
            print("Stok berhasil diupdate")
            return
        
    print("Barang tidak ditemukan")

def update_harga(data):
    kode = input("Kode barang: ").strip()

    for item in data:
        if item["kode"] == kode:
            try:
                harga_baru = int(input("Harga baru: "))
            except ValueError:
                print("Harga harus angka")
                return
            
            item["harga"] = harga_baru
            save_data(data)
            print("Harga berhasil diupdate")
            return
        
    print("Barang tidak ditemukan")

def hapus_barang(data):
    kode = input("Kode barang: ").strip()
    awal = len(data)

    data[:] = [item for item in data if item["kode"] != kode]

    if len(data) < awal:
        save_data(data)
        print("Barang berhasil dihapus")
    else:
        print("Barang tidak ditemukan")

def tampil_menu():
    print("""
=== INVENTORY MENU ===
1. Lihat barang
2. Tambah barang
3. Update stok
4. Update harga
5. Hapus barang
0. Keluar
""")
    
def main():
    while True:
        data = load_data()
        tampil_menu()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_barang(data)
        elif pilihan == "2":
            tambah_barang(data)
        elif pilihan == "3":
            update_stok(data)
        elif pilihan == "4":
            update_harga(data)
        elif pilihan == "5":
            hapus_barang(data)
        elif pilihan == "0":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

    