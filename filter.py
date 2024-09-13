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

data_filter = {
  1 : "Nasi",
  2 : "Mie"
}

if data_filter:
    print("Pilih filter sesuai dengan nomor dibawah ini:")
    print("No\t| Nama")
    for key, value in data_filter.items():
      print(f"{key}\t| {value}")
    
cari_filter = int(input("Masukkan pilhan nomor yang ingin dicari: "))
value_filter = data_filter[cari_filter]
print(value_filter)

nilai_cari = False
for key, item in data.items():
  if value_filter.lower() in item['Nama'].lower():
    print(f"{key}\t| {item['Nama']}\t\t| {item['Harga']}\t\t| {item['Stok']}\t\t| {item['Terjual']}")
    nilai_cari = True
  
if not nilai_cari:
    print("Data Tidak Ditemukan")