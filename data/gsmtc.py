import mysql.connector
import time
import os

def clear_console():
    os.system('clear' if os.name != 'nt' else 'cls')

def get_data_from_120m(gsm):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='120m'
        )
        cursor = con.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM 120m WHERE GSM='{gsm}'")
        result = cursor.fetchall()
        con.close()
        return result
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
        return None

def get_data_from_101m(tc_number):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='101m'
        )
        cursor = con.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM 101m WHERE TC='{tc_number}'")
        result = cursor.fetchall()
        con.close()
        return result
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
        return None

def main():
    clear_console()

    gsm = input("GSM Numarasını girin (0 olmadan ve birleşik): ")

    if gsm.startswith('0'):
        print("GSM numarası 0 ile başlayamaz.")
        return

    print("Sorgulanıyor, lütfen bekleyin...")
    time.sleep(2)

    data_120m = get_data_from_120m(gsm)

    if not data_120m:
        print("GSM nin TC si bulunamadi.")
        return

    tc_number = data_120m[0]['TC']
    data_101m = get_data_from_101m(tc_number)

    if not data_101m:
        print("GSM nin TC si bulunamadi.")
        return

    additional_info = "\n\n".join([
        f"{index + 1}. Kişi:\n"
        f"TC: {person['TC']}\n"
        f"ADI: {person['ADI']}\n"
        f"SOYADI: {person['SOYADI']}\n"
        f"DOĞUM TARİHİ: {person['DOGUMTARIHI']}\n"
        f"İL: {person['NUFUSIL']}\n"
        f"İLÇE: {person['NUFUSILCE']}\n"
        for index, person in enumerate(data_101m)
    ])

    print(f"{gsm} numarasına ait bilgiler:\n\n{additional_info}")

if __name__ == "__main__":
    main()
