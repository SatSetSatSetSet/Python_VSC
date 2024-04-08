import random
import sys
import time
import main_game
from welcome_exit import exit_message

def print_with_flash(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def tebak_goa():
    while True:
        bentuk_goa = ["( .. )"] * 5
        goa_beruang = random.randint(1, 5)
        bentuk_beruang = "(0.0)"
        print_with_flash("Selamat Datang Di Game Tebak Goa\n")
        print_with_flash("###################################\n")
        print_with_flash("##         Cara Bermain:         ##\n")
        print_with_flash("##  Tebak Di Mana Beruang Berada ##\n")
        print_with_flash("##         Kesempatan: 3x        ##\n")
        print_with_flash("###################################\n")
        print_with_flash("Lihat Goa Dibawah Ini:\n")
        print(" ".join(bentuk_goa))

        for kesempatan in range(3):
            try:
                tebakan = int(input("Masukkan Nomor Gua (1-5): "))
                if tebakan < 1 or tebakan > 5:
                    raise ValueError
            except ValueError:
                print("Masukkan angka antara 1 dan 5.")
                continue

            if tebakan == goa_beruang:
                print("Anda Benar!")
                print("Beruang Berada Di Gua =", goa_beruang)
                bentuk_goa[goa_beruang - 1] = bentuk_beruang
                print(" ".join(bentuk_goa))
                break
            else:
                if kesempatan == 2:
                    print("Kesempatan Anda Telah Habis")
                    print("Beruang Berada Di Gua =", goa_beruang)
                    bentuk_goa[goa_beruang - 1] = bentuk_beruang
                    print(" ".join(bentuk_goa))
                elif tebakan < goa_beruang:
                    print("Gua yang Anda pilih terlalu rendah.")
                elif tebakan > goa_beruang:
                    print("Gua yang Anda pilih terlalu tinggi.")

        if not kembali_ke_tebak_goa():
            break

def start():
    while True:
        tebak_goa()

def kembali_ke_tebak_goa():
    while True:
        choice = input("Apakah Anda ingin bermain lagi? (Yes/No): ")
        if choice.lower() == 'yes':
            return True
        elif choice.lower() == 'no':
            main_game.menu()
            exit_message()
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan pilih Yes/No.")

if __name__ == "__main__":
    start()