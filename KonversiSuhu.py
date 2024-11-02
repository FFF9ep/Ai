#Rumus Celcius ke Reamur
def konversi_reamur(celcius):
    konversi_reamur = 4 * celcius / 5
    return konversi_reamur

#Rumus Celcius ke Farenheit
def konversi_farenheit(celcius):
    konversi_farenheit = 9 * celcius / 5 + 32
    return konversi_farenheit

#Rumus Celcius ke Kelvin
def konversi_kelvin(celcius):
    konversi_kelvin = celcius + 273
    return konversi_kelvin

print("=" * 30)
print("    Program Konversi Suhu    ")
print("=" * 30)
temperatur_suhu = int(input("Masukkan Skala Celcius : "))
print("=" * 46)
print(f"Hasil Konversi Suhu {temperatur_suhu} C Adalah {konversi_reamur(temperatur_suhu)} Reamur")
print(f"Hasil Konversi Suhu {temperatur_suhu} C Adalah {konversi_farenheit(temperatur_suhu)} Farenheit")
print(f"Hasil Konversi Suhu {temperatur_suhu} C Adalah {konversi_kelvin(temperatur_suhu)} Kelvin")