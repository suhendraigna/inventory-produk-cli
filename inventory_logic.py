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

def list_barang(data):
    if not data:
        print("Inventory kosong")
        return
    
    print("\nData Barang:")
    for item in data:
        print(
            f"- [{item['kode']}] {item['nama']} | Stok: {item['stok']} | Harga: Rp{item['harga']}"
        )
    
def add_barang(data, kode, nama, stok, harga):
    data.append({
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga,
    })
    save_data(data)

def update_stok(data, kode, stok_baru):
    for item in data:
        if item["kode"] == kode:
            item["stok"] = stok_baru
            save_data(data)
            return True
    return False

def update_harga(data, kode, harga_baru):
    for item in data:
        if item["kode"] == kode:
            item["harga"] = harga_baru
            save_data(data)
            return True
    return False

def delete_barang(data, kode):
    awal = len(data)
    data[:] = [i for i in data if i["kode"] != kode]
    if len(data) < awal:
        save_data(data)
        return True
    return False