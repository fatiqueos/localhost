import subprocess
import sys
import shutil
import os
import winreg as reg

def install(package):
    """Kutuphaneleri indirir ve yukler."""
    print(f"[INFO] {package} kutuphanesi indiriliyor...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    print(f"[BASARILI] {package} basariyla kuruldu!")

install('mysql-connector-python')
install('requests')
install('mysqlclient')
install('psutil')
install('colorama')

source_file = 'data/sulaleapi.php'

def get_xampp_path_from_registry():
    try:
        reg_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\XAMPP"
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_key) as key:
            install_dir, _ = reg.QueryValueEx(key, "InstallLocation")
            return install_dir
    except Exception as e:
        print(f"[HATA] XAMPP dizini kayit defterinden alinamadi: {e}")
        return None

xampp_path = get_xampp_path_from_registry()

if not xampp_path:
    xampp_paths = [
        r'C:\xampp',
        r'D:\xampp',
        r'E:\xampp'
    ]
    
    for path in xampp_paths:
        if os.path.exists(path):
            xampp_path = path
            break

if xampp_path:
    windows_destination = os.path.join(xampp_path, 'htdocs', 'sulaleapi.php')
    shutil.copy(source_file, windows_destination)
    print("\n[BASARILI] Dosya basariyla kopyalandi.")
    print(f"Dosya {windows_destination} dizinine basariyla kopyalandi.\n")
else:
    print("\n[HATA] XAMPP dizini bulunamadi.\n")

input("Kapatmak icin bir tusa basin...")
sys.exit()
