import mysql.connector
import os
import time
import platform
import subprocess

def clear_console():
    os.system('clear' if os.name != 'nt' else 'cls')

def query_database(isim, soyisim, dogumtarihi=None, il=None, ilce=None, anneadi=None, annetc=None, babaadi=None, babatc=None):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='101m'
        )
        cursor = con.cursor(dictionary=True)

        query = "SELECT * FROM 101m WHERE ADI = %s AND SOYADI = %s"
        params = [isim, soyisim]

        if dogumtarihi:
            query += " AND DOGUMTARIHI REGEXP %s"
            params.append(dogumtarihi)
        if il:
            query += " AND NUFUSIL = %s"
            params.append(il)
        if ilce:
            query += " AND NUFUSILCE = %s"
            params.append(ilce)
        if anneadi:
            query += " AND ANNEADI = %s"
            params.append(anneadi)
        if annetc:
            query += " AND ANNETC = %s"
            params.append(annetc)
        if babaadi:
            query += " AND BABAADI = %s"
            params.append(babaadi)
        if babatc:
            query += " AND BABATC = %s"
            params.append(babatc)

        print("Sorgulaniyor, lutfen bekleyin...")
        time.sleep(2)

        cursor.execute(query, params)
        result = cursor.fetchall()
    finally:
        cursor.close()
        con.close()

    return result

def get_temp_directory():
    if platform.system() == 'Windows':
        return os.getenv('TEMP')
    else:
        return '/tmp'

def save_results_to_file(results, isim, soyisim):
    temp_dir = get_temp_directory()
    file_path = os.path.join(temp_dir, f'{isim}_{soyisim}_sonuclar.txt')

    with open(file_path, 'w', encoding='utf-8') as f:
        result_count = len(results)
        f.write(f"Toplam {result_count} sonuç bulundu.\n\n")

        if not results:
            f.write("Sonuc bulunamadi.\n")
        else:
            for row in results:
                f.write(
                    f'TC: {row["TC"]} | AD: {row["ADI"]} | SOYAD: {row["SOYADI"]} | '
                    f'DOGUMTARIHI: {row["DOGUMTARIHI"]} | IL: {row["NUFUSIL"]} | ILCE: {row["NUFUSILCE"]} | '
                    f'ANNE ADI: {row["ANNEADI"]} | ANNE TC: {row["ANNETC"]} | '
                    f'BABA ADI: {row["BABAADI"]} | BABA TC: {row["BABATC"]}\n'
                )

    return file_path

def open_file(file_path):
    if platform.system() == 'Windows':
        os.startfile(file_path)
    else:
        subprocess.call(['xdg-open', file_path])

def main():
    clear_console()
    print("Zorunlu kisimlar:")
    
    isim = input("Adi: ").strip()
    soyisim = input("Soyadi: ").strip()

    if not isim or not soyisim:
        print("Ad ve soyad zorunlu.")
        return

    print("\nIstege bagli kisimlar (gecmek icin enter basin):")
    dogumtarihi = input("Dogum Tarihi (GG-AA-YYYY veya YYYY): ").strip()
    il = input("Il: ").strip()
    ilce = input("Ilce: ").strip()
    anneadi = input("Anne Adi: ").strip()
    annetc = input("Anne TC: ").strip()
    babaadi = input("Baba Adi: ").strip()
    babatc = input("Baba TC: ").strip()

    results = query_database(isim, soyisim, dogumtarihi, il, ilce, anneadi, annetc, babaadi, babatc)
    
    file_path = save_results_to_file(results, isim, soyisim)
    
    print(f"Sonuclar '{file_path}' dosyasina kaydedildi.")
    
    open_file(file_path)

if __name__ == "__main__":
    main()
