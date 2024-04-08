import random
import sys
import time
from welcome_exit import exit_message
import main_game

MAX_ATTEMPTS = 8

def tebak_angka():
    while True:
        time.sleep(1)
        print("Selamat Datang di Game Tebak Angka")
        print(f"Anda Akan Diberikan Kesempatan Sebanyak {MAX_ATTEMPTS} kali")
        
        while True:  
            angka_rahasia = random.randint(1, 10)
            for kesempatan in range(1, MAX_ATTEMPTS + 1):
                try:
                    tebakan = int(input("Tebak angka (1-10): "))
                    if tebakan < 1 or tebakan > 10:
                        raise ValueError
                except ValueError:
                    print("Masukkan angka antara 1 dan 10.")
                    continue
                
                if tebakan < angka_rahasia:
                    print("Angka terlalu kecil.")
                elif tebakan > angka_rahasia:
                    print("Angka terlalu besar.")
                else:
                    print("Selamat, tebakan Anda benar!")
                    break
            
            if kesempatan == MAX_ATTEMPTS:
                print("Maaf, Anda kehabisan kesempatan.")
                print(f"Angka yang benar adalah: {angka_rahasia}")  

            if not kembali_ke_tebak_angka():  
                break  

def start():
    while True:
        tebak_angka()

def kembali_ke_tebak_angka():
    while True:
        choice = input("Apakah Anda ingin bermain lagi? (Yes/No): ")
        if choice.lower() == 'yes':
            tebak_angka()
        elif choice.lower() == 'no':
            main_game.menu()
            exit_message()
            sys.exit()
        else:
            print("Silakan pilih Yes atau No.")

if __name__ == "__main__":
    start()
