import subprocess
import os

# Bulunduğun dizindeki repo kontrol edilecek
repo_dir = os.getcwd()  # Şu anki dizini alır

def update_repo():
    if os.path.isdir(os.path.join(repo_dir, ".git")):  # Git dizini var mı?
        print(f"Git repo bulundu, {repo_dir} güncelleniyor...")
        # Repo dizinine gir ve güncelle
        subprocess.run(["git", "-C", repo_dir, "pull"])
    else:
        print(f"{repo_dir} dizininde bir Git repo bulunamadı.")
        # Repo dizinini klonlamak için seçenek sun
        clone = input("Repo klonlansın mı? (Evet/Hayır): ").lower()
        if clone == "evet":
            subprocess.run(["git", "clone", "https://github.com/fatiqueos/localhost", repo_dir])

if __name__ == "__main__":
    update_repo()
    print("Güncelleme tamamlandı.")
