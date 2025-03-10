#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Fungsi untuk membalikkan proses enkripsi
void reverseCrack(char *message)
{
    int length = strlen(message);

    // 1. Pembalikan Urutan String (reverse)
    for (int i = 0; i < length / 2; i++)
    {
        char temp = message[i];
        message[i] = message[length - 1 - i];
        message[length - 1 - i] = temp;
    }

    // 2. Menggeser Huruf Kembali (2 mundur untuk huruf)
    for (int i = 0; i < length; i++)
    {
        if (isalpha(message[i]))
        {
            message[i] = message[i] - 2;
        }
    }

    // 3. Menggeser Berdasarkan Angka (mengurangi berdasarkan angka pada posisi sebelumnya)
    for (int i = 0; i < length; i++)
    {
        if (isdigit(message[i]))
        {
            int shift = message[i] - '0'; // Mengambil nilai angka
            if (i + 1 < length)
            {
                message[i + 1] = message[i + 1] - shift;
            }
        }
    }
}

int main()
{
    // Pesan terenkripsi yang diberikan oleh program C
    char message[] = "}C1y3u_ww1_j@uWu_ip@{_,ip@rs4i_It4r3o_e_@y4n4d{tgdkncM";

    // Menampilkan pesan terenkripsi
    printf("Pesan terenkripsi: %s\n", message);

    // Membalikkan proses enkripsi
    reverseCrack(message);

    // Menampilkan pesan yang telah didekripsi
    printf("Pesan asli: %s\n", message);

    return 0;
}
