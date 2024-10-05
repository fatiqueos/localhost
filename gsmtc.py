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
    except:
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
    except:
        return None

def main():
    gsm = input("GSM Numarasini girin (0 olmadan ve birlesik): ")

    if gsm.startswith('0'):
        return

    clear_console()

    print("Sorgulaniyor, lutfen bekleyin...")
    time.sleep(2)

    data_120m = get_data_from_120m(gsm)

    if not data_120m:
        print("GSM numarasina ait veri bulunamadi.")
        return

    tc_number = data_120m[0]['TC']
    data_101m = get_data_from_101m(tc_number)

    if not data_101m:
        print("TC numarasina ait veri bulunamadi.")
        return

    additional_info = "\n\n".join([
        f"{index + 1}. Kisi:\n"
        f"TC: {person['TC']}\n"
        f"ADI: {person['ADI']}\n"
        f"SOYADI: {person['SOYADI']}\n"
        f"DOGUM TARIHI: {person['DOGUMTARIHI']}\n"
        f"IL: {person['NUFUSIL']}\n"
        f"ILCE: {person['NUFUSILCE']}\n"
        for index, person in enumerate(data_101m)
    ])

    print(f"{gsm} numarasina ait bilgiler:\n\n{additional_info}")

if __name__ == "__main__":
    main()
