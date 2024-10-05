import mysql.connector
import os
import time

def create_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='101m'
    )

def clear_console():
    os.system('clear' if os.name != 'nt' else 'cls')

def fetch_personal_info(tc, cursor):
    query = "SELECT * FROM 101m WHERE TC=%s"
    cursor.execute(query, (tc,))
    result = cursor.fetchone()
    
    if not result:
        return "Kisinin bilgileri bulunamadi."

    return (
        f'TC: {result["TC"]}\n'
        f'ADI: {result["ADI"]}\n'
        f'SOYADI: {result["SOYADI"]}\n'
        f'DOGUM TARİHI: {result["DOGUMTARIHI"]}\n'
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
    tc = input("Kisinin TC Kimlik Numarasi: ").strip()

    if not tc:
        print("TC Kimlik Numarasi zorunludur.")
        return

    try:
        con = create_db_connection()
        cursor = con.cursor(dictionary=True)

        print("Sorgulaniyor, lutfen bekleyin...")
        time.sleep(2)

        personal_info = fetch_personal_info(tc, cursor)

        clear_console()
        print(personal_info.strip())

    except mysql.connector.Error as err:
        print(f"Veritabani hatasi: {err}")
    except Exception as e:
        print(f"Bir hata olustu: {e}")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

if __name__ == "__main__":
    main()
