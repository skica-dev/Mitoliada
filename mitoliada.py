import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
np = 2
x = 1

print(" __  __ _____ _______ ____  _      _____          _____          ")
print("|  \/  |_   _|__   __/ __ \| |    |_   _|   /\   |  __ \   /\    ")
print("| \  / | | |    | | | |  | | |      | |    /  \  | |  | | /  \   ")
print("| |\/| | | |    | | | |  | | |      | |   / /\ \ | |  | |/ /\ \  ")
print("| |  | |_| |_   | | | |__| | |____ _| |_ / ____ \| |__| / ____ \ ")
print("|_|  |_|_____|  |_|  \____/|______|_____/_/    \_\_____/_/    \_\  2976")
print("Autor I  : Maks Skica")
#print("Autor II : **********") edit 05.05.2017, name cesored
print("")
time.sleep(10)
print("")
time.sleep(0.05) ### ahh.. from my today view this code really sucks
print("")       ### please don't shame on me because of it
time.sleep(0.05) ### I was only 12 ;P and 'for' was a mystical word =
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("")
time.sleep(0.05)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("0!")
time.sleep(1)
pytanie1 = "Skad pochodzil Ikar?"
pytanie2 = "Co oznacza powiedzenie jablko niezgody ?"
pytanie4 = "Co przedstawione jest na obrazku? (Obrazek 1)"
pytanie6 = "Kto byl krolowa Hadesu?"
pytanie8 = "Gdzie mieszkal Hefajstos, a gdzie Hades?"
pytanie9 = "Co oznacza powiedzenie pieta Achillesa?"
pytanie11 = "Wymien trzy znane ci nimfy."
pytanie12 = "Kogo to atrybut? (Obrazek 2)"
pytanie13 = "Opisz kilkoma slowami Hestie?"
pytanie14 = "Jak nazywala sie wyspa Eola?"
pytanie15 = "Kto napisal Iliade i Odyseje i o czym one opowiadaja?"
pytanie16 = "Ktora z bogin przygotowala jablko niezgody?"
pytanie17 = "Ile bylo bogow olimpijskich?"
pytanie18 = "Kto byl mezem Pandory?"
pytanie19 = "Kim byla koza Almatea?"
pytanie20 = "Co to za bog? (Obrazek 3)"
pytanie21 = "Co oznacza powiedzenie kon trojanski?"
pytanie22 = "Kim byl Orfeusz?"
pytanie23 = "Co spowodowalo, ze Eurydyka zmarla?"
pytanie24 = "Kim jest czlowiek przedstawony na obrazku? (Obrazek 4)"
pytanie25 = "Czemu Dedal musial uciekac z Aten?"
pytanie26 = "Kim byly Danaidy?"
pytanie27 = "Ile lat trwala tulaczka Odyseusza?"
pytanie28 = "Ktorzy z herosow sa przedstawieni na rysunku? (Obrazek 5)"
pytanie29 = "Jak nazywal sie bozek smierci"
pytanie30 = "Jak narodzila sie Afrodyta?"
pytanie31 = "Podaj imie bogini zwyciestwa."
pytanie32 = "Co zrobil pies Odysa, gdy ujrzal pana po dwudziestu latach?"
pytanie33 = "Opisz Zeusa w pieciu zdaniach."
pytanie34 = "Co to za bogini? (Obrazek 6)"
pytanie35 = "Kim byl Eros?"
pytanie36 = "Jakie zwierzeta pasly sie na Wyspie Slonca?"
pytanie37 = "Przy kim wystepowala bogini zwyciestwa?"
pytanie38 = "Czyim atrybutem byl owoc granatu?"
pytanie39 = "Jakie swieto ludzie organizowali na czesc Dionizosa?"
pytanie40 = "Co Atena zaoferowala atenczykom?"
pytanie3 = "Krolem jakiego panstwa byl Syzyf?"
pytanie5 = "Ktorzy bogowie wylonili sie z Chaosu?"
pytanie7 = "Wymien piec osob, ktore pomogly Odysowi."
pytanie10 = "Kim byl Charon?"
pytanie40 = "Co Atena zaoferowala atenczykom?"
pytanie41 = "Ile lat trwala wojna pomiedzy Zeusem, a jego ojcem?"
pytanie42 = "Jak ma na imie ten bog? (Obrazek 7)"
pytanie43 = "Z kim walczyl w zawodach Apollo?"
pytanie45 = "Podaj dwa podobienstwa mitologii greckiej i religii chrzescijanskiej."
pytanie46 = "Kim byl Hektor?"
pytanie47 = "Kogo to atrybut? (Obrazek 8)"
pytanie48 = "Czemu Hefajstos byl kulawy?"
pytanie50 = "Jaka byla kara Tantala?"

pytanie49 = "Czym opiekowala sie bogini Iris?"
pytanie44 = "Kto byl krolem Sparty za czasow Odyseusza?"
print(pytanie1)
while True:
      if x == 1:
            while x == 1:
                  if GPIO.input(18) == False:
                        print("Zolci odpowiadaja na zadane pytanie.")
                        x = 2
                  if GPIO.input(23) == False:
                        print("Czerwoni odpowiadaja na zadane pytanie.")
                        x = 2
                  if GPIO.input(24) == False:
                        print("Zieloni odpowiadaja na zadane pytanie.")
                        x = 2
                  if GPIO.input(25) == False:
                        print("Niebiescy odpowiadaja na zadane pytanie.")
                        x = 2
      if x == 2:
            while x == 2:
                  print("Udzielanie odpowiedzi...")
                  print("Zostalo 20 sekund...")
                  time.sleep(1)
                  print("Zostalo 19 sekund...")
                  time.sleep(1)
                  print("Zostalo 18 sekund...")
                  time.sleep(1)
                  print("Zostalo 17 sekund...")
                  time.sleep(1)
                  print("Zostalo 16 sekund...")
                  time.sleep(1)
                  print("Zostalo 15 sekund...")
                  time.sleep(1)
                  print("Zostalo 14 sekund...")
                  time.sleep(1)
                  print("Zostalo 13 sekund...")
                  time.sleep(1)
                  print("Zostalo 12 sekund...")
                  time.sleep(1)
                  print("Zostalo 11 sekund...")
                  time.sleep(1)
                  print("Zostalo 10 sekund...")
                  time.sleep(1)
                  print("Zostalo 9 sekund...")
                  time.sleep(1)
                  print("Zostalo 8 sekund...")
                  time.sleep(1)
                  print("Zostalo 7 sekund...")
                  time.sleep(1)
                  print("Zostalo 6 sekund...")
                  time.sleep(1)
                  print("Zostalo 5 sekund...")
                  time.sleep(1)
                  print("Zostalo 4 sekundu...")
                  time.sleep(1)
                  print("Zostalo 3 sekundy...")
                  time.sleep(1)
                  print("Zostalo 2 sekundy...")
                  time.sleep(1)
                  print("Zostalo 1 sekunda...")
                  time.sleep(1)
                  print("Koniec czasu!")
                  print("")
                  print("")
                  print("")
                  print("Nastepne pytanie...")
                  time.sleep(5)
                  if np == 2:   # yeah...
                        print(pytanie2)
                  if np == 3:
                        print(pytanie3)
                        np + 1
                  if np == 4:
                        print(pytanie4)
                  if np == 5:
                        print(pytanie5)
                  if np == 6:
                        print(pytanie6)
                  if np == 7:
                        print(pytanie7)
                  if np == 8:
                        print(pytanie8)
                  if np == 9:
                        print(pytanie9)
                  if np == 10:
                        print(pytanie10)
                  if np == 11:
                        print(pytanie11)
                  if np == 12:
                        print(pytanie12)
                  if np == 13:
                        print(pytanie13)
                  if np == 14:
                        print(pytanie14)
                  if np == 15:
                        print(pytanie15)
                  if np == 16:
                        print(pytanie16)
                  if np == 17:
                        print(pytanie17)
                  if np == 18:
                        print(pytanie18)
                  if np == 19:
                        print(pytanie19)
                  if np == 20:
                        print(pytanie20)
                  if np == 21:
                        print(pytanie21)
                  if np == 22:
                        print(pytanie22)
                  if np == 23:
                        print(pytanie23)
                  if np == 24:
                        print(pytanie24)
                  if np == 25:
                        print(pytanie25)
                  if np == 26:
                        print(pytanie26)
                  if np == 27:
                        print(pytanie27)
                  if np == 28:
                        print(pytanie28)
                  if np == 29:
                        print(pytanie29)
                  if np == 30:
                        print(pytanie30)
                  if np == 31:
                        print(pytanie31)
                  if np == 32:
                        print(pytanie32)
                  if np == 33:
                        print(pytanie33)
                  if np == 34:
                        print(pytanie34)
                  if np == 35:
                        print(pytanie35)
                  if np == 36:
                        print(pytanie36)
                  if np == 37:
                        print(pytanie37)
                  if np == 38:
                        print(pytanie38)
                  if np == 39:
                        print(pytanie39)
                  if np == 40:
                        print(pytanie40)
                  if np == 41:
                        print(pytanie41)
                  if np == 42:
                        print(pytanie42)
                  if np == 43:
                        print(pytanie43)
                  if np == 44:
                        print(pytanie44)
                  if np == 45:
                        print(pytanie45)
                  if np == 46:
                        print(pytanie46)
                  if np == 47:
                        print(pytanie47)
                  if np == 48:
                        print(pytanie48)
                  if np == 49:
                        print(pytanie49)
                  if np == 50:
                        print(pytanie50)
                  if np == 51:
                        print("Gra zostala zakonczona!")
                        break
                  np = np+1
                  x = 1
