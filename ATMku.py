saldo = 1000000;

while True:
    pin = int(input("SILAHKAN MASUKKAN PIN ANDA : "));
    print()
    if pin == 12345:
        print('''MENU ATM
1. Penarikan
2. Setoran
3. Pengiriman
4. Cek Saldo''')
        print()
        pilihan = input("Silahkan Masukkan Pilihan Anda : ")
        print() 
        if pilihan == "1":
            penarikan = int(input("Masukkan Jumlah Penarikan : "))
            if penarikan > saldo:
                print("Saldo Anda Tidak Cukup")
            else:
                if penarikan > 200000:
                    admin = 5000;
                else:
                    admin = 0;
                saldo = saldo - penarikan - admin;
                print("Informasi Penarikan")
                print("Jumlah Penarikan : ", penarikan)
                print("Biaya Admin      : ", admin)
                
        elif pilihan == "2":
            setoran = int(input("Masukkan Jumlah Setoran : "))
            if setoran > 200000:
                admin = 5000;
            else:
                admin = 0;
            saldo = (saldo + setoran) - admin;
            print("Informasi Setoran")
            print("Jumlah Setoran : ", setoran)
            print("Biaya Admin    : ", admin)
            

        elif pilihan == "3":
            tujuan = int(input("Masukkan Rekening Tujuan : "))
            pengiriman = int(input("Masukkan Jumlah Pengiriman : "))
            if pengiriman > saldo:
                print("Saldo Anda Tidak Cukup")
            else:
                if pengiriman > 200000:
                    admin = 5000;
                else:
                    admin = 0;
                saldo = saldo - pengiriman - admin;
                print("Informasi Pengiriman")
                print("Jumlah Pengiriman : ", pengiriman)
                print("Rekening Tujuan  : ", tujuan)
                print("Biaya Admin      : ", admin)

        elif pilihan == "4":
            print("Saldo Anda : ", saldo)

        else:
            print("Periksa Kembali Menu Anda")
    else:
        print("Silahkan Periksa Kembali PIN Anda")

    print()
    tl = input("Tekan y untuk Melanjutkan Program : ")
    print()
    if tl == "y":
        print();
    else:
        print("Terimah Kasih")
        print("Selamat Datang Kembali")
        break
        
