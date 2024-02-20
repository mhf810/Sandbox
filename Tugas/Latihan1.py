# variable, syarat adalah
# 1. hanya diawali dengan huruf
# 2. tidak boleh diawali dengan angka
# 3. bersifat case sensitive
# 4. tidak boleh menggunakan kata kunci yang sudah di python
a = 1
b = 2
print(a)

# tipe data
# 1. integer ==> bilangan bulat cth. 1 
angka = 1

# 2. float ==> desimal atau pecahan, cth. 1.2
pecahan = 3.2

# 3. string ==> kumpulan karakter yang ditandai dengan apit tanda petik satu maupun dua
kata = "Ini adalah semua kalimat"

# 4. boolean ==> True atau False
is_flag = True

# data structure
# 1. list => berisi data bisa int, bisa string, bisa boolean dengan ditandai tanda kurung siku [ ]
isi_list = ['kucing', 'tikus', 'burung', 1, True]

# 2. tuple => berisi data bisa int, bisa string, bisa boolean dengan ditandai tanda kurung ( )
ini_tuple = (2, True, False, 'Saya', 1.5)

# 3. set => berisi himpunan, artinya tidak bisa double data
ini_set = {1, 5, 7, 8}

# 4. dictionary ==> yang terdiri dari key dan value dengan format tanda kurung kurawal { }
ini_dict = {'nama' : 'Erwin', 'alamat': 'Jakarta', 'nomor_rumah': 3}


# control flow
# comparison operations
# 1. equal dengan tanda == , contoh a == b
# 2. less than atau greater than dengan tanda < atau >
# 3. less than and equal dengan tanda <= atau greater than and equal dengan >= 
# 4. tidak sama dengan pakai tanda !=

# condisional (if)
biaya_awal = 2000
biaya_akhir = 2000

if biaya_awal < biaya_akhir:
    print('Biaya awal lebih kecil dari biaya akhir')
elif biaya_awal == biaya_akhir:
    print('Biaya Awal sama dengan biaya akhir')
elif biaya_awal > biaya_akhir:
    print('Bangkrut')
else:
    print('Tidak kondisi diatas terpenuhi')


# looping (perulangan)
# for loop

list_nama = ['Erwin', 'Sudarmadi', 'Aldo']
#indexing      0          1           2  

# cara manual
print(list_nama[0])
print(list_nama[1])
print(list_nama[2])

# cara looping
for i in list_nama:
    print(i)

# next materi : function dan class