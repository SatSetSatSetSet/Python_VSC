def kalkulator():
    print("Indikator Berupa (+),(-),(*),(/),(%)")
    print("Untuk Keluar Program Ketikkan Exit")

    while True:
        indikator = input("Masukkan Indikatornya Disini = ")
        
        if indikator.lower() == "exit":
            exit()
        elif indikator not in ("+", "-", "*", "/", "%"):
            print("Indikator Yang Anda Masukkan Salah")
        else:
            break
        
    while True:
        try:
            a = int(input("Masukkan Angka Pertama = "))
            break
        except ValueError:
            print("Harus Memasukkan Angka")

    while True:
        try:
            b = int(input("Masukkan Angka Kedua = "))
            break
        except ValueError:
            print("Harus Memasukkan Angka")

    if indikator == "+":
        result = a + b
    elif indikator == "-":
        result = a - b
    elif indikator == "*":
        result = a * b
    elif indikator == "/":
        if b == 0:
            print("Tidak Boleh Membagi dengan 0")
        else:
            result = a / b
    elif indikator == "%":
        result = a % b
    print("Hasil =", result)

if __name__ == "__main__":
    kalkulator()