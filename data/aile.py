import mysql.connector
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_and_send_results(cursor, query, error_message, title):
    cursor.execute(query)
    result = cursor.fetchall()
    
    if not result:
        return f"{title}: {error_message}\n----------------------------\n"
    else:
        bilgiler = ""
        for row in result:
            bilgiler += f"TC: {row[1]}\tADI: {row[2]}\tSOYADI: {row[3]}\tDOĞUM TARİHİ: {row[4]}\tİL: {row[5]}\tİLÇE: {row[6]}\n----------------------------\n"
        return f"{title}: {bilgiler}"

def main():
    clear_screen()
    tc = input("Kişinin TC Kimlik Numarasını girin: ")

    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='101m'
    )
    cursor = con.cursor()

    all_information = ""
    
    all_information += fetch_and_send_results(cursor, f'SELECT * FROM 101m WHERE TC="{tc}"', 'Bulunamadı', 'Kendisi')
    
    all_information += fetch_and_send_results(cursor, f'SELECT * FROM 101m WHERE ANNETC="{tc}" OR BABATC="{tc}"', 'Bulunamadı', 'Çocukları')
    
    all_information += fetch_and_send_results(cursor, f'SELECT * FROM 101m WHERE TC=(SELECT ANNETC FROM 101m WHERE TC="{tc}")', 'Bulunamadı', 'Annesi')
    
    all_information += fetch_and_send_results(cursor, f'SELECT * FROM 101m WHERE TC=(SELECT BABATC FROM 101m WHERE TC="{tc}")', 'Bulunamadı', 'Babası')
    
    all_information += fetch_and_send_results(cursor, f'SELECT * FROM 101m WHERE ANNETC=(SELECT ANNETC FROM 101m WHERE TC="{tc}") OR BABATC=(SELECT BABATC FROM 101m WHERE TC="{tc}")', 'Bulunamadı', 'Kardeşleri')

    clear_screen()
    print(all_information.strip())

    cursor.close()
    con.close()

if __name__ == "__main__":
    main()
