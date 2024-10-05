import mysql.connector
import os
import time

def create_db_connection():
    """Veritabani baglantisini olusturur."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='101m'
    )

def clear_console():
    """Terminal ekranini temizler."""
    os.system('clear' if os.name != 'nt' else 'cls')

def fetch_personal_info(tc, cursor):
    """Kisinin bilgilerini veritabanindan getirir ve formatlar."""
    query = "SELECT * FROM 101m WHERE TC=%s"
    cursor.execute(query, (tc,))
    result = cursor.fetchone()
    
    if not result:
        return "Kisinin bilgileri bulunamadi."

    return (
        f'TC: {result["TC"]}\tADI: {result["ADI"]}\tSOYADI: {result["SOYADI"]}\t'
        f'DOGUM TARİHI: {result["DOGUMTARIHI"]}\tIL: {result["NUFUSIL"]}\t'
        f'ILCE: {result["NUFUSILCE"]}'
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
