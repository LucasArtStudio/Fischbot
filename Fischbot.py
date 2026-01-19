import time
import datetime
import threading
from time import sleep

import numpy as np
import pyautogui
import pydirectinput
import pytesseract
import cv2
import random
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r'D:\Programme\Python Umgebung\Tesseract\tesseract.exe'
pause_threads = threading.Event()
pause_threads2 = threading.Event()

def Leveln(x1, y1):
    if (pyautogui.pixelMatchesColor(x1 + 67, y1 + 111, (199, 199, 199))):
        pydirectinput.click((x1 + 67, y1 + 111))



def DropItems(item, x1, y1, x2, y2):
    invSeite1 = 'InvSeite1.png'
    try:
        inv1x, inv1y = pyautogui.locateCenterOnScreen(invSeite1, grayscale=False, confidence=0.8,
                                                      region=(x1, y1, x2, y2))
        x, y = pyautogui.locateCenterOnScreen(item, grayscale=True, confidence=0.9, region=(x1, y1, x2, y2))
        pydirectinput.click(x, y)
        time.sleep(0.1)
        pydirectinput.click(inv1x -100, inv1y)  # Drop POS
        time.sleep(0.3)
        pydirectinput.click(inv1x - 300 , inv1y +145)  # Drop Bestätigen POS
    except pyautogui.ImageNotFoundException:
        pass
def Drop(x1, y1, x2, y2):
    KleinerFisch = 'KleinerFisch.png'
    KleinerZander = 'KleinerZander.png'
    Graskarpfen = 'Graskarpfen.png'
    Kaiser = 'Kaiser.png'
    Kaiser2 = 'Kaiser2.png'
    Karpfen = 'Karpfen.png'
    Lachs = 'Lachs.png'
    Mandarinfisch = 'Mandarinfisch.png'
    Regenbogenforelle = 'Regenbogenforelle.png'
    Ring = 'Ring.png'
    Tenchi = 'Tenchi.png'
    Umhang = 'Umhang.png'
    Zander = 'Zander.png'
    Bachforelle = 'Bachforelle.png'
    Rotfeder = 'Rotfeder.png'
    Aal = 'Aal.png'
    Barsch = 'Barsch.png'
    Lotusfisch = 'Lotusfisch.png'
    DropItems(Barsch, x1, y1, x2, y2)
    DropItems(Aal, x1, y1, x2, y2)
    DropItems(Rotfeder, x1, y1, x2, y2)
    DropItems(KleinerFisch, x1, y1, x2, y2)
    DropItems(KleinerFisch, x1, y1, x2, y2)
    DropItems(Bachforelle, x1, y1, x2, y2)
    DropItems(KleinerZander, x1, y1, x2, y2)
    DropItems(KleinerZander, x1, y1, x2, y2)
    DropItems(Graskarpfen, x1, y1, x2, y2)
    DropItems(Kaiser, x1, y1, x2, y2)
    DropItems(Kaiser2, x1, y1, x2, y2)
    DropItems(Karpfen, x1, y1, x2, y2)
    DropItems(Lachs, x1, y1, x2, y2)
    DropItems(Mandarinfisch, x1, y1, x2, y2)
    DropItems(Regenbogenforelle, x1, y1, x2, y2)
    DropItems(Ring, x1, y1, x2, y2)
    DropItems(Tenchi, x1, y1, x2, y2)
    DropItems(Umhang, x1, y1, x2, y2)
    DropItems(Lotusfisch, x1, y1, x2, y2)
    DropItems(Zander, x1, y1, x2, y2)

def FischanHaken(x1, y1):
    if pyautogui.pixelMatchesColor(x1 + 385, y1 + 438, (102, 81, 82), tolerance=13): #Golum Tag farbe
        Reichsiegel(x1, y1)
    if pyautogui.pixelMatchesColor(x1 + 385, y1 + 438, (50, 42, 47), tolerance=8): #Golum Nacht farbe
        Reichsiegel(x1, y1)
    if (pyautogui.pixelMatchesColor(x1 + 406, y1 + 395, (241, 245, 248))):
        pydirectinput.click(x1 + 406, y1 + 395)

    if not (pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))):
        if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
            pydirectinput.leftClick(x1 + 402, y1 + 386)

    if pyautogui.pixelMatchesColor(x1 + 263, y1 + 185, (175, 115, 98), tolerance=13) or pyautogui.pixelMatchesColor(x1 + 263, y1 + 185, (206, 138, 107), tolerance=13): #Puppe Tag
        wurmx, wurmy = find_color_in_inv(x1 + 627, y1 + 238, (245, 192, 173))
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 650, y1 + 180)
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.rightClick(wurmx, wurmy)
        pydirectinput.press('space')

    if pyautogui.pixelMatchesColor(x1 + 263, y1 + 185, (85, 59, 57), tolerance=6): #Puppe Nacht
        wurmx, wurmy = find_color_in_inv(x1 + 627, y1 + 238, (245, 192, 173))
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 650, y1 + 180)
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.rightClick(wurmx, wurmy)
        pydirectinput.press('space')

def Auswurf():
    while True:
        x1 = 7
        y1 = 0

        now = datetime.datetime.now()
        if (now.minute % 6 == 0 and now.second < 10):
            return

        FischanHaken(x1, y1)
        Login(x1, y1)
        Aufstehen(x1, y1)

        x1 = 1757
        y1 = 0
        FischanHaken(x1, y1)
        Login(x1, y1)
        Aufstehen(x1, y1)

        x1 = 7
        y1 = 770
        FischanHaken(x1, y1)
        Login(x1, y1)
        Aufstehen(x1, y1)

        time.sleep(0.5) #Zeit wie schnell nach gewurmt wird

def Login(x1, y1):
    global pause_threads
    if (pyautogui.pixelMatchesColor(x1 + 600, y1 + 250, (250, 74, 63))):
        if(x1 == 7 and y1 == 0):
            pydirectinput.click(x1 + 530, y1 + 340)
        elif(x1 == 1757 and y1 == 0):
            pydirectinput.click(x1 + 530, y1 + 360)
        elif(x1 == 7 and y1 == 770):
            pydirectinput.click(x1 + 530, y1 + 380)
    if (pyautogui.pixelMatchesColor(x1 + 600, y1 + 250, (8, 10, 11))):
        pydirectinput.click(x1 + 100, y1 + 420) #Klickt hier Start zum Joinen
    while pause_threads.is_set():
        time.sleep(0.01)
    if (not pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))
            and pyautogui.pixelMatchesColor(x1 + 785, y1 + 140, (99, 48, 0))):
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('i')
        print("Inv nicht geöffnet")
        pydirectinput.keyDown('r')
        pydirectinput.keyDown('g')
        time.sleep(2)
        pydirectinput.keyUp('r')
        pydirectinput.keyUp('g')
        pause_threads.set()
        print("Kritischer Bereich")
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('w')
        pydirectinput.press('w')
        sleep(0.05)
        print("Kritischer Bereich Ende")
        pause_threads.clear()


def Aufstehen(x1,y1):
    if pyautogui.pixelMatchesColor(x1 + 560, y1 + 450, (82, 107, 140), tolerance=8) or pyautogui.pixelMatchesColor(x1 + 560, y1 + 450, (104, 135, 168), tolerance=8) or pyautogui.pixelMatchesColor(x1 + 560, y1 + 450, (135, 174, 200), tolerance=8):
        print('Aufstehen')
        pydirectinput.rightClick(x1 + 620, y1 + 80)
        time.sleep(1)
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('space')
        time.sleep(3)
        print("Kritischer Bereich")
        x, y = find_color_in_inv(x1 + 618, y1 + 230, (38, 26, 20), 8)
        print(x, y)
        pydirectinput.rightClick(x, y)
        pause_threads.clear()

def OpenInv(x1,y1):
    if (pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))):
        print("Inv geöffnet")
    else:
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('i')
        print("Inv nicht geöffnet")

def Reichsiegel(x1, y1):
    pydirectinput.rightClick(x1 + 627, y1 + 238)  # Reichssiegel drücken
    time.sleep(2)

    Rechnungx1 = x1 + 232
    Rechnungy1 = y1 + 292
    BildRechnung = pyautogui.screenshot(region=(int(Rechnungx1), int(Rechnungy1), 50, 20))

    # Bild in Graustufen und hochskalieren für bessere OCR
    Screenshot = cv2.cvtColor(np.array(BildRechnung), cv2.COLOR_BGR2GRAY)
    Screenshot2 = cv2.resize(Screenshot, None, fx=30, fy=30, interpolation=cv2.INTER_CUBIC)

    # OCR ausführen
    Text = pytesseract.image_to_string(
        Screenshot2,
        config='--psm 6 -c tessedit_char_whitelist=0123456789+'
    )

    # Nur Zahlen und + behalten
    Text = re.sub(r'[^0-9+]', '', Text)

    # Falls kein + erkannt wurde, bei 5 Zeichen heuristisch splitten
    if "+" not in Text and len(Text) == 5:
        mitte = len(Text) // 2
        links = Text[:mitte]
        rechts = Text[mitte:].lstrip("0")  # führende Null entfernen
        Text = f"{links}+{rechts}"

    print("OCR Text:", Text)

    # Klick ausführen
    pydirectinput.click(x1 + 400, y1 + 350)

    # Berechnung durchführen
    if "+" in Text:
        a, b = Text.split("+", 1)

        try:
            y = int(a.strip()) + int(b.strip())
            print("Ergebnis:", y)
        except:
            print("Ungültiger Text, y = 0")
            y = 0
    else:
        print("Kein + gefunden, y = 0")
        y = 0
    # --- Zahl ausgeben ---
    for digit in str(y):
        pydirectinput.press(digit)
    print("End verwandelt")
    if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
        pydirectinput.leftClick(x1 + 402, y1 + 386)
    time.sleep(1)
    if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
        pydirectinput.leftClick(x1 + 402, y1 + 386)

def AutoFisching():
    pydirectinput.click(1000,0)
    while True:
        x1 = 7
        y1 = 0
        t1 = threading.Thread(target=Bot, args=(x1, y1))

        x1 = 1757
        y1 = 0
        t2 = threading.Thread(target=Bot, args=(x1, y1))

        x1 = 7
        y1 = 770
        t3 = threading.Thread(target=Bot, args=(x1, y1))

        t4 = threading.Thread(target=Auswurf)

        print(datetime.datetime.now())
        t1.start()
        print(datetime.datetime.now())
        t2.start()
        print(datetime.datetime.now())
        t3.start()
        print(datetime.datetime.now())
        t4.start()
        t1.join()
        print(datetime.datetime.now())
        t2.join()
        print(datetime.datetime.now())
        t3.join()
        print(datetime.datetime.now())
        t4.join()
        #sleep(2)
        x1 = 7
        y1 = 0
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1, 800, 600)
        Aufstehen(x1, y1)

        x1 = 1757
        y1 = 0
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1, 800, 600)
        Aufstehen(x1, y1)

        x1 = 7
        y1 = 770
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1, 800, 600)
        Aufstehen(x1, y1)

def find_color_in_inv(x1, y1, target_color, tolerance = 1):
    for y in range(y1, y1 + 32*8 + 1, 32):
        for x in range(x1, x1 + 32*4 + 1, 32):
            if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=tolerance):
                return x , y
    return 0, 0

def Bot(x1, y1):
    while True:
        now = datetime.datetime.now()
        if (now.minute % 6 == 0 and now.second < 10):
            return
        pixelMatchesColor = pyautogui.pixelMatchesColor(x1 + 390, y1 + 170, (255, 255, 255), tolerance=10) #Einhol Symbole erkennen
        if(pixelMatchesColor):
            time.sleep(2.7)
            while pause_threads.is_set():
                time.sleep(0.01)
            global pause_threads2
            pause_threads2.set()
            pydirectinput.click(x1 + 785, y1 + 140)
            pydirectinput.press('space')
            pause_threads2.clear()
            print('Ziehe Fisch raus.')

            time.sleep(10)

def move_clients():
    pyautogui.mouseDown(50, 15, button='left')
    sleep(0.7)
    pyautogui.mouseUp(1800, 15, button='left')
    pyautogui.mouseDown(50, 15, button='left')
    sleep(0.7)
    pyautogui.mouseUp(50, 785, button='left')

def move_clientsLeveln():
    pyautogui.mouseDown(50, 15, button='left')
    sleep(0.7)
    pyautogui.mouseUp(900, 15, button='left')

#move_clients()
#move_clientsLeveln()
AutoFisching()

x1=1757
y1=0
#x, y = find_color_in_inv(x1 + 560, y1 + 450, (38, 26, 20), 8)
#print(x, y)
color = pyautogui.screenshot().getpixel((x1 + 560, y1 + 450))
print(color)
pydirectinput.moveTo(x1 + 66, y1 + 111)


werte = []  # Array für alle RGB-Werte
n = 200

for i in range(n):
    color = pyautogui.screenshot().getpixel((x1 + 263, y1 + 185))
    werte.append(color)
    #time.sleep(0.1)  # kleine Pause (optional)

print("Alle Werte:", werte)

# Einzelne Kanäle extrahieren
r_values = [c[0] for c in werte]
g_values = [c[1] for c in werte]
b_values = [c[2] for c in werte]

print("R min:", min(r_values), "R max:", max(r_values))
print("G min:", min(g_values), "G max:", max(g_values))
print("B min:", min(b_values), "B max:", max(b_values))


# Mittelwert
r_avg = sum(r_values) / len(r_values)
g_avg = sum(g_values) / len(g_values)
b_avg = sum(b_values) / len(b_values)

print("R Mittelwert:", r_avg)
print("G Mittelwert:", g_avg)
print("B Mittelwert:", b_avg)


