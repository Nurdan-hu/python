import hesapmaktry_01
import calender
import BMIhesaplama
import sıcaklıkhes
print("╔═════════════════════╗")
#print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║   VEKTOREL APP      ║")
print("║                     ║")
print("║  1-Hesap makinesi   ║")
print("║  2-Takvim           ║")
print("║  3-BMI hesapla      ║")
print("║  4-Sıcaklık çevirme ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

secim = input ()
if secim == "1" : hesapmaktry_01.hesaplarmenu()
if secim == "2" : calender.takvım()
if secim == "3" : BMIhesaplama.BMI()
if secim == "4" : sıcaklıkhes.sıcaklık()