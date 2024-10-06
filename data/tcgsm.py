import mysql.connector
import os
import time

def clear_console():
    os.system('clear' if os.name != 'nt' else 'cls')

def get_data_from_db(tc):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='120m'
        )
        cursor = con.cursor(dictionary=True)

        cursor.execute(f'SELECT * FROM 120m WHERE TC="{tc}"')
        result = cursor.fetchall()
        con.close()
        return result
    except:
        return None

def main():
    clear_console()
    tc = input("TC Kimlik Numarasini girin: ")

    print("Sorgulaniyor, lutfen bekleyin...")
    time.sleep(2)
    clear_console()

    data = get_data_from_db(tc)

    if not data:
        print("Kisinin GSM numarasi bulunamadi.")
        return

    print(f"\n{tc} TC'sine Ait Telefon Numaralari:")
    for index, entry in enumerate(data):
        print(f"Numara {index + 1}: {entry['GSM']}")

if __name__ == "__main__":
    main()
