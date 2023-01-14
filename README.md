# UAS-PEMROGRAMAN
## ✓ daftar_nilai.py berisi modul untuk:tambah_data, ubah_data, hapus_data,dan cari_data
## def menu_dosen():

## system('cls')

## print('=====================================')

## print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('| 1. Tambah Data                    |')
    print('| 2. Lihat Data Mahasiswa           |')
    print('| 3. Ubah Data Mahasiswa            |')
    print('| 4. Hapus Data Mahasiswa           |')
    print('| 5. Selesai                        |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        ubah()
    elif pilih2 == '4':
        hapus()
    elif pilih2 == '5':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu_dosen()


## ✓ view_nilai.py berisi modul untuk:cetak_daftar_nilai, cetak_hasil_pencarian



## ✓ input_nilai.py berisi modul untuk:input_data yang meminta pengguna memasukkan data




## ✓ main.py berisi program utama (menu pilihan yang memanggil semua menu yang ada)
