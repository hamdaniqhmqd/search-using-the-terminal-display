# Pencarian Data dengan Python

**Pencarian** adalah proses atau teknik untuk menemukan elemen atau informasi tertentu dalam sebuah struktur data, baik itu list, array, dictionary, file, atau database. Tujuannya adalah untuk menemukan apakah elemen tersebut ada di dalam kumpulan data, dan jika ada, menentukan di mana elemen tersebut berada (misalnya, indeks atau lokasi). Pencarian bisa dilakukan dengan berbagai metode, dari yang paling sederhana hingga yang paling kompleks, tergantung pada struktur data dan seberapa besar dataset yang digunakan.

### 1. Pencarian Teknik Sequence (Sequential Search)

**Pencarian sequence** atau sequential search adalah teknik pencarian paling dasar di mana setiap elemen dalam sebuah struktur data (misalnya list, array) diperiksa satu per satu secara berurutan hingga elemen yang dicari ditemukan atau hingga semua elemen telah diperiksa. Metode ini sederhana tetapi tidak efisien untuk dataset yang besar karena membutuhkan waktu linear, yaitu O(n), di mana n adalah jumlah elemen dalam struktur data.

```bash
  def seq_search(nums,x):
  for i in range(len(nums)): # mencari di seluruh elemen nums
    if x == nums[i]:
      return i # mengembalikan index elemen yang cocok dengan x

  return -1 # ketika tidak ditemukan elemen yang cocok dengan x dalam nums
```

### 2. Identifikasi Low, Mid, High (Dalam Binary Search)

Pada pencarian yang lebih efisien, seperti binary search, konsep low, mid, dan high digunakan untuk memecah masalah pencarian pada data yang sudah terurut. Berikut cara kerja identifikasi ini:

1. Low: Ini adalah batas bawah dari range data yang sedang dicari. Awalnya, ini dimulai dari indeks pertama array (biasanya 0).

2. High: Ini adalah batas atas dari range data. Awalnya, ini adalah indeks terakhir dari array (misalnya len(array) - 1).

3. Mid: Ini adalah titik tengah antara low dan high. Pada setiap langkah, pencarian akan membandingkan elemen di indeks mid dengan nilai target. Jika target lebih kecil, pencarian berlanjut ke sisi kiri (low hingga mid-1). Jika lebih besar, pencarian berlanjut ke sisi kanan (mid+1 hingga high).

```bash
  def bin_search(nums,x):
  low, high = 0, len(nums) - 1 # menginisialisasikan titik low dan high
  while low <= high:
    mid = (low + high) // 2 # mendeklarasikan titik mid
    if nums[mid] == x:
      return mid
    elif nums[mid] > x:
      high = mid -1
    else:
      low = mid + 1

  return -1 # apabila result tidak ditemukan
```

### 3. Pencarian Data dalam Nested Dictionary
