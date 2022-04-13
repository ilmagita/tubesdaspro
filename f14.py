def help():
    role = int(input("Masukkan role (Admin/User): "))
    if role == "Admin":
        print('''
        ============= HELP =============
        1. register             - Untuk melakukan registrasi user baru
        2. login                - Untuk melakukan login ke dalam sistem
        3. tambah_game          - Untuk menambah game yang dijual pada toko
        4. ubah_game            - Untuk mengubah game yang dijual pada toko
        5. ubah_stok            - Untuk mengubah stok sebuah game yang dijual pada toko
        6. list_game_toko       - Untuk melihat list game yang dijual pada toko
        7. search_game_at_store - Untuk mencari game yang dijual pada toko
        8. topup                - Untuk menambahkan saldo kepada user
        9. help                 - Untuk memberikan panduan penggunaan sistem
        10. save                - Untuk melakukan penyimpanan data ke dalam file setelah dirubah
        11. exit                - Untuk keluar dari aplikasi
        ''')
    elif role == "User":
        print('''
        ============= HELP =============
        1. login                - Untuk melakukan login ke dalam sistem
        2. list_game_toko       - Untuk melihat list game yang dijual pada toko
        3. buy_game             - Untuk membeli game pada toko
        4. list_game            - Untuk melihat daftar game yang dimiliki user
        5. search_my_game       - Untuk mendapatkan informasi game sesuai dengan query yang diminta user
        6. search_game_at_store - Untuk mencari game yang dijual pada toko
        7. riwayat              - melihat riwayat pembelian game
        8. help                 - Untuk memberikan panduan penggunaan sistem
        9. save                 - Untuk melakukan penyimpanan data ke dalam file setelah dirubah
        10. exit                - Untuk keluar dari aplikasi
        ''')