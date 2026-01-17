# Inventory Produk CLI (Python)

A simple inventory management application built with Python.
This project stores data in a JSON file and can be used via command line.

## Features
- View product list
- Add new product
- Update product stock
- Update product price
- Delete product

## Tech Stack
- Python 3
- JSON file storage
- CLI using argparse
- No framework

## Project Structure

inventory-produk/
├── inventory.py          # Interactive menu version
├── inventory_cli.py      # CLI (argparse) version
├── inventory_logic.py    # Shared business logic
├── inventory.json        # Data storage
└── README.md

## Usage

1. List all products
   python3 inventory_cli.py list

2. Add a product
   python3 inventory_cli.py add --kode B01 --nama Buku --stok 5 --harga 12000

3. Update product stock
   python3 inventory_cli.py update-stok --kode B01 --stok 10

4. Update product price
   python3 inventory_cli.py update-harga --kode B01 --harga 15000

5. Delete a product
   python3 inventory_cli.py delete --kode B01

## Notes
- Data is stored locally in inventory.json
- This project is intended for learning and practice purposes