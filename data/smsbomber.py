from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

system("cls||clear")

print("Telefon numarasini basinda '+90' olmadan yaziniz: ", end="")
tel_no = input()
try:
    int(tel_no)
    if len(tel_no) != 10:
        raise ValueError
except ValueError:
    system("cls||clear")
    print("Hatalı telefon numarası. Tekrar deneyiniz.") 
    sleep(3)
    exit()

system("cls||clear")
print("Kac adet SMS gondermek istiyorsunuz: ", end="")
try:
    adet = int(input())
except ValueError:
    system("cls||clear")
    print("Hatalı giris yaptiniz. Tekrar deneyiniz.")
    sleep(3)
    exit()

system("cls||clear")
send_sms = SendSms(tel_no, "")
sent_count = 0

while sent_count < adet:
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(getattr(send_sms, attribute)) for attribute in dir(send_sms)
            if callable(getattr(send_sms, attribute)) and not attribute.startswith('__')
        ]
        wait(futures)

    if send_sms.adet > sent_count:
        sent_count += (send_sms.adet - sent_count)
        print(f"{sent_count}/{adet} SMS basariyla gonderildi.")
    else:
        print("SMS gonderimi basarisiz oldu.")

    sleep(1)

system("cls||clear")
print(f"Tum {adet} SMS basariyla gonderildi.")
sleep(2)
exit()
