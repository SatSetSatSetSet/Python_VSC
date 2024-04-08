import time

def welcome_message():
    welcome_message = "Selamat Datang di Program Buatan Saya"
    print(welcome_message)
    print("Mohon Tunggu...")
    loading_message = "Loading"
    for _ in range(3):
        print(loading_message + "...")
        time.sleep(1)
        
def exit_message():
    exit_message = "Program Akan Dihentikan"
    print(exit_message)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
if __name__ == "__main__":
    welcome_message()
    exit_message()
