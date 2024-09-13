import sys

data = {
  1 : {
      'Nama' : 'Nasi Goreng',
      'Harga' : 12000,
      'Stok' : 10,
      'Terjual' : 0
  },
  2 : {
      'Nama' : 'Mie Ayam',
      'Harga' : 7000,
      'Stok' : 10,
      'Terjual' : 0
  },
  3 : {
      'Nama' : 'Nasi Kuning',
      'Harga' : 10000,
      'Stok' : 10,
      'Terjual' : 0
  },
  4 : {
      'Nama' : 'Mie Campur',
      'Harga' : 10000,
      'Stok' : 10,
      'Terjual' : 0
  },
}

def cariData(data):
  cari_nama = input("Masukkan nama yang ingin dicari: ")
  print("No\t| Nama \t\t\t|Harga \t\t|Stok \t\t|Terjual")
  nilai_cari = False
  for key, item in data.items():
    if cari_nama.lower() in item['Nama'].lower():
      print(f"{key}\t| {item['Nama']}\t\t| {item['Harga']}\t\t| {item['Stok']}\t\t| {item['Terjual']}")
      nilai_cari = True
  
  if not nilai_cari:
    print("Data Tidak Ditemukan")
    
  pilihan = input("Apakah ingin mencari data lagi? (y/n): ")
  while True:
    if pilihan.lower() == "y":
      cariData(data)
    elif pilihan.lower() == "n":
      sys.exit()
    else:
      print("Masukkan pilihan yang sesuai")
      
cariData(data)