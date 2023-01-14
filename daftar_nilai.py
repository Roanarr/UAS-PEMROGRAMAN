def ubah():
    rubah = input('Ubah Biodata/Nilai [B/N] : ')
    if rubah == 'B' or rubah == 'b':
        i = int(input('Inputkan ID : '))
        if (i > len(d_nim[i])):
            print('ID Salah')
        else:
            jurusanb = input('Prodi [TI/SI] : ')
            if jurusanb == 'TI' or jurusanb == 'ti':
                jbaru = 'Teknik Informatika'
                d_jurusan[i] = jbaru
            elif jurusanb == 'SI' or jurusanb == 'si':
                jbaru = 'Sistem Informasi'
                d_jurusan[i] = jbaru
            else:
                kembali = input('Pilihan tidak ada')
                ubah()

            namabaru = input('Nama : ')
            d_nama[i] = namabaru

            nimbaru = input('Nim : ')
            d_nim[i] = nimbaru

            kelasbaru = input('Kelas : ')
            d_kelas[i] = kelasbaru


    else:
        i = int(input('Inputkan ID : '))
        if (i > len(d_nim[i])):
            print('ID Salah')
        else:
            hadirb = float(input('Jumlah Hadir : '))
            j_hadirb = ((hadirb / 16) * 20 / 100) * 100
            d_hadir[i] = j_hadirb

            tugasb = float(input('Nilai Tugas : '))
            j_tugasb = tugasb * (25 / 100)
            d_tugas[i] = j_tugasb

            utsb = float(input('Nilai UTS : '))
            j_utsb = utsb * (25 / 100)
            d_uts[i] = j_utsb

            uasb = float(input('Nilai UAS : '))
            j_uasb = uasb * (30 / 100)
            d_uas[i] = j_uasb

            totalb = j_hadirb + j_tugasb + j_utsb + j_uasb
            d_akhir[i] = totalb
    kembali = input('Kembali Tekan [enter]')
    menu_dosen()
