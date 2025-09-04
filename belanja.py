print("\n")
print(10*'=', "Program Daftar Belanja", 10*'=')
print(44*'-')

# teks
t_invalid = "Input tidak valid"
t_view = "ketik 'view' untuk melihat list belanja"
t_exit = "ketik 'exit' untuk"
t_file = "Daftar belanja anda"

barang = [] # list belanja

# flag
is_menu = True
is_one_valid = False
is_ones_valid = True

# loop menu utama
while is_menu:
    print(19*'*', "Menu", 19*'*')
    print("1. Tambah Barang")
    print("2. Tampilkan File Saved")
    print("3. Keluar")
    print(44*'-')
    try:
        menu = int(input("Pilih menu (1-3): ")) # Input menu pilihan user
        if menu not in (1,2,3):
            print(t_invalid, "\n")
            continue

        elif menu == 1: # input menu 1
            n = 0
            is_price_valid = False # flag

            # loop menu 1 (hingga valid)
            while not is_one_valid:
                n += 1
                print(t_view)
                print(44*'-')

                tambah = input(f"Masukkan nama barang ke-{n}: ") # input nama barang
                if tambah == 'view'.lower(): # jika melihat list
                    print(44*'-')
                    is_price_valid = True
                    is_one_valid = True

                # loop harga (hingga valid)
                while not is_price_valid:
                    harga = input(f"Masukkan harga barang ke-{n} (*masukkan tanpa simbol!): ") # input harga barang

                    if harga == 'exit'.lower(): # jika keluar
                        n -= 1
                        print(44*'-')
                        break
                    else:
                        # coba eksekusi variabel harga
                        try:
                            harga = float(harga) # casting ke float
                            barang.append({"nama": tambah, "harga": harga}) # menambah barang ke list
                            print(44*'-')
                            print(f"Barang {tambah} berhasil ditambahkan.")
                            print(44*'-')
                            break
                        except ValueError:
                            print(44*'-')
                            print(f"{t_invalid},\n{t_exit} kembali")
                            print(44*'-')

                if not barang: # jika barang kosong
                    print(f"{t_file} masih kosong.")
                    print(44*'-')
                    is_one_valid = False
                    is_price_valid = False
                    n -= 1
                    continue

                if tambah == 'view'.lower(): # jika melihat list
                    print(7*'-', "Berikut daftar  belanja anda", 7*'-')
                    for i, item in enumerate(barang, start=1):
                        print(f"{i}. {item['nama']} - Rp. {item['harga']}")

                    print(44*'-')

                    is_again_valid = False # flag

                    # loop tambah lagi (hingga valid)
                    while not is_again_valid:
                        again = input("Ingin menambahkan barang lagi? (y/n): ")
                        if again == 'y':
                            n -= 1
                            is_again_valid = True
                            is_one_valid = False
                            is_price_valid = False
                            continue
                        elif again == 'n':
                            is_ones_valid = False
                            print(44*'-')
                            break
                        else:
                            print(t_invalid)
                            print(44*'-')
                            continue

        elif menu == 2: # Input menu 2
            with open("list_belanja.txt", "r") as f:
                isi = f.read()
                print(isi)

        elif menu == 3: # Input menu 3
            print(44*'-')
            print("Sampai jumpa!")
            break

        else: # Input menu tidak valid
            print(44*'-')
            print(t_invalid)
            continue
    
    except ValueError:
        print(t_invalid)
        continue

    is_remove_valid = False # flag
    is_quit_valid = False # flag

    # loop menu 1 1 (hingga valid)
    while not is_ones_valid:                        
        print("Hapus barang atau keluar?:")
        print("1. Hapus barang")
        print("2. Keluar")
        print(44*'-')
        opsi = int(input("Pilih opsi: "))
        print(44*'-')
        
        if opsi not in (1,2):
            print(t_invalid)
            continue
        elif opsi == 1: # jika input 1 1

            # loop hapus barang (hingga valid)
            while not is_remove_valid:

                if len(barang) > 0:
                    print(7*'-', "Berikut daftar  belanja anda", 7*'-')
                    for i, item in enumerate(barang, start=1):
                        print(f"{i}. {item['nama']} - Rp. {item['harga']}")
                
                    print(44*'-')
                    remove = input("Masukkan angka yang ingin dihapus / ('exit'): ")
                    if remove == 'exit'.lower():
                        print(44*'-')
                        break
                    elif not remove.isdigit(): # ganti selain positif juga
                        print(f"{t_exit} keluar")
                        print(44*'-')
                        continue
                    else:
                        remove = int(remove)
                        if 1 <= remove <= len(barang):
                            removed = barang.pop(remove-1)
                            print(44*'-')
                            print(f"Barang {removed['nama']} berhasil dihapus.")
                            print(44*'-')
                            continue
                        elif remove > len(barang) or remove < 1:
                            print("Barang tidak ditemukan!")
                            print(44*'-')
                            continue
                else:
                    print(f"{t_file} masih kosong")
                    print(44*'-')
                    print("Jika anda ingin menambahkan barang,\nSilahkan jalankan kembali program ini:)")
                    is_ones_valid = True
                    is_menu = False
                    break

        elif opsi == 2:

            # loop quit (hingga valid)
            while not is_quit_valid:
                print("Pilih opsi berikut sebelum keluar:")
                print("1. Simpan file dan keluar")
                print("2. Hapus file dan keluar")
                print(44*'-')
                quit = int(input("Pilih opsi: "))
                print(44*'-')

                if quit not in (1,2):
                    print(t_invalid)
                    print(44*'-')
                    continue
                elif quit == 1:

                    # eksekusi file
                    with open("list_belanja.txt", "w") as f:
                        f.write("<List Belanja anda>\n\n")

                    for i, item in enumerate(barang, start=1):
                        with open("list_belanja.txt", "a") as f:
                            f.write(f"\t{i}. {item['nama']} - Rp. {item['harga']}\n")

                    with open("list_belanja.txt", "a") as f:
                        f.write("\n")

                    print(f"{t_file} telah disimpan di file\n'list_belanja.txt'.")
                    print(44*'-')
                    is_quit_valid = True
                    is_ones_valid = True
                    is_menu = False
                    break

                elif quit == 2:
                    print(f"{t_file} telah dihapus.")
                    print(44*'-')
                    is_quit_valid = True
                    is_ones_valid = True
                    is_menu = False
