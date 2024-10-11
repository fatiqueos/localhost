import os
import subprocess
import time
import psutil
import webbrowser

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_service_running(service_name):
    for proc in psutil.process_iter(['name']):
        if service_name.lower() in proc.info['name'].lower():
            return True
    return False

def start_service(service_name, service_path):
    if not is_service_running(service_name):
        try:
            subprocess.Popen(service_path)
            time.sleep(2)
            if is_service_running(service_name):
                print(f"{service_name} servisi basariyla baslatildi.")
            else:
                print(f"Hata: {service_name} servisi baslatilamadi.")
        except Exception as e:
            print(f"{service_name} servisi baslatilirken hata olustu: {e}")
    else:
        print(f"{service_name} servisi zaten calisiyor.")

def manage_xampp():
    xampp_path = "C:\\xampp"
    services = {
        'apache': {'name': 'httpd.exe', 'path': [os.path.join(xampp_path, 'apache', 'bin', 'httpd.exe')]},
        'mysql': {'name': 'mysqld.exe', 'path': [os.path.join(xampp_path, 'mysql', 'bin', 'mysqld.exe')]},
    }

    for service in services.values():
        start_service(service['name'], service['path'])

def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Hata olustu: {e}")

    input("\nMenuye donmek icin bir tusa basin...")

def open_project():
    webbrowser.open("https://github.com/fatiqueos/localhost")
    input("Devam etmek icin bir tusa basin...")

def main_menu():
    manage_xampp()

    menu_options = {
        '1': {'action': lambda: run_script("data/adres.py")},
        '2': {'action': lambda: run_script("data/aile.py")},
        '3': {'action': lambda: run_script("data/gsmtc.py")},
        '4': {'action': lambda: run_script("data/sorgu.py")},
        '5': {'action': lambda: run_script("data/sulale.py")},
        '6': {'action': lambda: run_script("data/tcgsm.py")},
        '7': {'action': lambda: run_script("data/tckn.py")},
        '8': {'action': lambda: run_script("data/smsbomber.py")},
        '9': {'action': open_project},
        'q': {'action': lambda: exit_program()},
    }

    while True:
        clear_console()
        print("--- Ana Menu ---")
        print("1. Adres Sorgu")
        print("2. Aile Sorgu")
        print("3. GSM TC Sorgu")
        print("4. Ad Soyad Sorgu")
        print("5. Sulale Sorgu")
        print("6. TC GSM Sorgu")
        print("7. TC Sorgu")
        print("8. Sms Bomber")
        print("9. Projeye Git")
        print("q. Cikis")

        choice = input("\nSeciminiz: ").lower()

        if choice in menu_options:
            clear_console()
            menu_options[choice]['action']()
        else:
            print("Gecersiz secim, tekrar deneyin.")
            time.sleep(1)

def exit_program():
    print("Cikiliyor...")
    time.sleep(1)
    os._exit(0)

if __name__ == "__main__":
    main_menu()
