from welcome_exit import exit_message, welcome_message
import tebak_angka
import tebak_goa

def menu():
    print("=== MENU GAMES ===")
    print("1.Tebak Angka")
    print("2.Tebak Goa")
    print("3.Keluar")
    choice = int(input("Masukkan pilihan Anda: "))
        
    if choice == '1':
        tebak_angka.start()
    elif choice == '2':
        tebak_goa.start()
    elif choice == '3':
        print("Terima kasih!")

def main():
    welcome_message()
    menu()
    exit_message()

if __name__ == "__main__":
    main()