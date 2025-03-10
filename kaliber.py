def decrypt(message):
    # Langkah 1: Membalikkan string
    message = message[::-1]

    # Langkah 2: Mengurangi 2 pada setiap karakter alfabet
    decrypted = []
    for char in message:
        if char.isalpha():  # hanya untuk huruf
            decrypted.append(chr(ord(char) - 2))  # Mengurangi 2 untuk huruf
        else:
            decrypted.append(char)

    # Langkah 3: Menggeser karakter setelah angka
    i = 0
    while i < len(decrypted) - 1:
        if decrypted[i].isdigit():  # jika karakter adalah angka
            shift = int(decrypted[i])  # mengambil angka
            # menggeser karakter setelah angka
            decrypted[i + 1] = chr(ord(decrypted[i + 1]) - shift)
        i += 1

    return ''.join(decrypted)


# Pesan terenkripsi yang diberikan oleh fungsi crackMe
encrypted_message = "}C1y3u_ww1_j@uWu_ip@{_,ip@rs4i_It4r3o_e_@y4n4d{tgdkncM"

# Menjalankan dekripsi
decrypted_flag = decrypt(encrypted_message)
print("Pesan asli yang didekripsi:", decrypted_flag)
