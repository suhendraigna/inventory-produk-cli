import argparse
from inventory_logic import (
    load_data,
    list_barang,
    add_barang,
    update_stok,
    update_harga,
    delete_barang
)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Inventory Produk CLI"
    )

    parser.add_argument(
        "command",
        choices=["list", "add", "update-stok", "update-harga", "delete"],
        help="Perintah inventory"
    )

    parser.add_argument("--kode", help="Kode produk")
    parser.add_argument("--nama", help="Nama produk")
    parser.add_argument("--stok", type=int, help="Stok produk")
    parser.add_argument("--harga", type=int, help="Harga produk")

    return parser.parse_args()

def main():
    args = parse_args()
    data = load_data()

    if args.command == "list":
        list_barang(data)

    elif args.command == "add":
        if not args.kode or not args.nama or args.stok is None or args.harga is None:
            print("Tambah produk butuh --kode --nama --stok --harga")
            return
        
        add_barang(data, args.kode, args.nama, args.stok, args.harga)
        print("Barang berhasil ditambahkan")
    
    elif args.command == "update-stok":
        if not args.kode or args.stok is None:
            print("Update stok butuh --kode dan --stok")
            return
        
        if update_stok(data, args.kode, args.stok):
            print("Stok berhasil diupdate")
        else:
            print("Barang tidak ditemukan")

    elif args.command == "update-harga":
        if not args.kode or args.harga is None:
            print("Update harga butuh --kode --harga")

        if update_harga(data, args.kode, args.harga):
            print("Harga berhasil diupdate")
        else:
            print("Barang tidak ditemukan")

    elif args.command == "delete":
        if not args.kode:
            print("Delete butuh --kode")

        if delete_barang(data, args.kode):
            print("Barang berhasil dihapus")
        else:
            print("Barang tidak ditemukan")

if __name__ == "__main__":
    main()