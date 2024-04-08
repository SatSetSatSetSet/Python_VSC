import sys

def kembali_ke_menu_tools():
    while True:
        choice = input("Apakah Anda ingin kembali ke menu tools? (Yes/No): ")
        if choice.lower() == 'yes':
            kembali_ke_menu_tools()
        elif choice.lower() == 'no':
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan pilih yes atau no.")

if __name__ == "__main__":
    kembali_ke_menu_tools()