import mysql.connector
import os
import time

def create_db_connection():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='101m'
        )
    except mysql.connector.Error:
        return None

def clear_console():
    os.system('clear' if os.name != 'nt' else 'cls')

def fetch_personal_info(tc, cursor):
    query = "SELECT * FROM 101m WHERE TC=%s"
    cursor.execute(query, (tc,))
    result = cursor.fetchone()
    
    if not result:
        return "Kisinin aile bilgileri bulunamadi."

    return (
        f'TC: {result["TC"]}\n'
        f'ADI: {result["ADI"]}\n'
        f'SOYADI: {result["SOYADI"]}\n'
        f'DOGUM TARIHI: {result["DOGUMTARIHI"]}\n'
        f'IL: {result["NUFUSIL"]}\n'
        f'ILCE: {result["NUFUSILCE"]}\n'
        f'ANNE ADI: {result["ANNEADI"]}\n'
        f'ANNE TC: {result["ANNETC"]}\n'
        f'BABA ADI: {result["BABAADI"]}\n'
        f'BABA TC: {result["BABATC"]}\n'
        f'UYRUK: {result["UYRUK"]}'
    )

def main():
    clear_console()
    tc = input("TC Kimlik Numarasini girin: ").strip()

    con = None
    cursor = None

    try:
        if not tc:
            return

        con = create_db_connection()
        if con is None:
            return

        cursor = con.cursor(dictionary=True)

        print("Sorgulaniyor, lutfen bekleyin...")
        time.sleep(2)

        personal_info = fetch_personal_info(tc, cursor)

        clear_console()
        print(personal_info.strip())

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

if __name__ == "__main__":
    main()
