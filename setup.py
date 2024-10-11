import subprocess
import sys
import shutil
import os

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

install('mysql-connector-python')
install('requests')
install('mysqlclient')
install('colorama')

source_file = 'data/sulaleapi.php'
windows_destination = r'C:\xampp\htdocs\sulaleapi.php'
linux_destination = '/var/www/html/sulaleapi.php'

if os.name == 'nt':
    shutil.copy(source_file, windows_destination)
else:
    shutil.copy(source_file, linux_destination)

sys.exit()
