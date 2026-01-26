import time
import datetime
import threading
from time import sleep
import pydirectinput

import pyautogui

import torch

# ---------- Modell einmal laden ----------

from transformers import TrOCRProcessor, VisionEncoderDecoderModel

processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-small-printed",
    use_fast=True  # Fast-Processor aktivieren
)
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-small-printed")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

pause_threads = threading.Event()
pause_threads2 = threading.Event()

def Leveln(x1, y1):
    if (pyautogui.pixelMatchesColor(x1 + 67, y1 + 111, (199, 199, 199))):
        pydirectinput.click((x1 + 67, y1 + 111))



def DropItems(target_color, x1, y1):
    for y in range(y1 + 235, y1 + 235 + 32*8 + 1, 32):
        for x in range(x1 + 625, x1 + 625 + 32*4 + 1, 32):
            if pyautogui.pixelMatchesColor(x, y, target_color):
                pydirectinput.click(x, y)  # Bild anklicken
                # Drop POS
                pydirectinput.click(x1 + 370, y1 + 350)

                # Bestätigen
                pydirectinput.click(x1 + 370, y1 + 350)

def Drop(x1, y1):
    DropItems((57, 61, 62), x1, y1)#Barsch
    DropItems((91, 65, 45), x1, y1 + 3)#Aal
    DropItems((241, 216, 180), x1, y1)#Rotfeder
    DropItems((102, 82, 82), x1, y1)#KleinerFisch
    DropItems((133, 133, 122), x1, y1)#Bachforelle
    #DropItems(KleinerZander, x1, y1)#KleinerZander
    DropItems((122, 110, 73), x1, y1)#Graskarpfen
    DropItems((38, 31, 8), x1, y1)#Symbole d. weisen Kaisers
    DropItems((172, 169, 98), x1, y1)#Handschuhe d. weisen Kaiser2
    DropItems((208, 179, 179), x1, y1)#Karpfen
    DropItems((72, 82, 29), x1, y1)#Lachs
    DropItems((183, 163, 133), x1, y1)#Mandarinfisch
    DropItems((230, 229, 201), x1, y1) #Regenbogenforelle
    DropItems((53, 71, 28), x1, y1) #Lucys Ring
    DropItems((205, 207, 98), x1, y1) #Tenchi
    DropItems((87, 87, 81), x1, y1) #Umhang
    DropItems((255, 255, 255), x1, y1) #Lotusfisch
    DropItems((175, 169, 116), x1, y1) #Zander

def FischanHaken(x1, y1):
    if (not pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))
            and (pyautogui.pixelMatchesColor(x1 + 785, y1 + 140, (99, 48, 0)) or pyautogui.pixelMatchesColor(x1 + 785, y1 + 140,(148, 105,57)))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('i')
        print("Inv nicht geöffnet")

    if pyautogui.pixelMatchesColor(x1 + 415, y1 + 487, (80, 46, 24), tolerance=6) or pyautogui.pixelMatchesColor(x1 + 455, y1 + 457, (101, 60, 38), tolerance=6) or pyautogui.pixelMatchesColor(x1 + 385, y1 + 438, (103, 80, 81), tolerance=6) or pyautogui.pixelMatchesColor(x1 + 455, y1 + 457, (57, 34, 25), tolerance=6) or pyautogui.pixelMatchesColor(x1 + 385, y1 + 438, (50, 42, 47), tolerance=6): #Golum Tag/Nacht farbe
        Reichsiegel(x1, y1)
    if (pyautogui.pixelMatchesColor(x1 + 405, y1 + 385, (43, 43, 54))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 405, y1 + 395)

    if not (pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))):
        if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
            while pause_threads2.is_set():
                time.sleep(0.01)
            pydirectinput.leftClick(x1 + 402, y1 + 386)

    if pyautogui.pixelMatchesColor(x1 + 265, y1 + 182, (166, 110, 92), tolerance=12) or pyautogui.pixelMatchesColor(x1 + 265, y1 + 182, (206, 138, 107), tolerance=8) or pyautogui.pixelMatchesColor(x1 + 275, y1 + 182, (166, 110, 92), tolerance=12) or pyautogui.pixelMatchesColor(x1 + 275, y1 + 182, (183, 121, 102), tolerance=12): #Puppe Tag
        wurmx, wurmy = find_color_in_inv(x1 + 627, y1 + 238, (245, 192, 173))
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 650, y1 + 180)
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.rightClick(wurmx, wurmy)
        pydirectinput.press('space')

    if pyautogui.pixelMatchesColor(x1 + 265, y1 + 182, (88, 60, 58), tolerance=6) or pyautogui.pixelMatchesColor(x1 + 275, y1 + 182, (88, 60, 58), tolerance=6): #Puppe Nacht
        wurmx, wurmy = find_color_in_inv(x1 + 627, y1 + 238, (245, 192, 173))
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 650, y1 + 180)
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.rightClick(wurmx, wurmy)
        pydirectinput.press('space')

def Auswurf(x1, y1):
    while True:
        FischanHaken(x1, y1)
        Login(x1, y1)
        Aufstehen(x1, y1)

        now = datetime.datetime.now()
        if (now.minute % 10 == 0 and now.second < 10):
            return

        time.sleep(0.2) #Zeit wie schnell nach gewurmt wird

def Login(x1, y1):
    global pause_threads
    if (pyautogui.pixelMatchesColor(x1 + 600, y1 + 250, (250, 74, 63))):
        if(x1 == 7 and y1 == 0):
            while pause_threads2.is_set():
                time.sleep(0.01)
            pydirectinput.click(x1 + 530, y1 + 340)
        elif(x1 == 1757 and y1 == 0):
            while pause_threads2.is_set():
                time.sleep(0.01)
            pydirectinput.click(x1 + 530, y1 + 360)
        elif(x1 == 7 and y1 == 770):
            while pause_threads2.is_set():
                time.sleep(0.01)
            pydirectinput.click(x1 + 530, y1 + 380)
        elif(x1 == 1757 and y1 == 770):
            while pause_threads2.is_set():
                time.sleep(0.01)
            pydirectinput.clickww(x1 + 530, y1 + 400)
    if (pyautogui.pixelMatchesColor(x1 + 600, y1 + 250, (8, 10, 11))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 100, y1 + 420) #Klickt hier Start zum Joinen
        sleep(7)

    if (not pyautogui.pixelMatchesColor(x1 + 760, y1 + 100, (8, 4, 8))
            and pyautogui.pixelMatchesColor(x1 + 785, y1 + 140, (99, 48, 0))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.keyDown('r')
        pydirectinput.keyDown('g')
        time.sleep(2)
        pydirectinput.keyUp('r')
        pydirectinput.keyUp('g')

def Aufstehen(x1,y1):
    if pyautogui.pixelMatchesColor(x1 + 400, y1 + 280, (60, 42, 40), tolerance=5) or pyautogui.pixelMatchesColor(x1 + 400, y1 + 280, (30, 22, 23), tolerance=5): #Tag/Nacht
        print('Aufstehen')
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.rightClick(x1 + 620, y1 + 80)
        time.sleep(1)
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.click(x1 + 785, y1 + 140)
        pydirectinput.press('space')
        time.sleep(3)
    result = find_color_in_inv(x1 + 618, y1 + 230, (38, 26, 20), 8)
    if result is not None:
        x, y = result

        while pause_threads2.is_set():
            time.sleep(0.01)

        pydirectinput.rightClick(x, y)


def Reichsiegel(x1, y1):
    while pause_threads2.is_set():
        time.sleep(0.01)
    pydirectinput.rightClick(x1 + 627, y1 + 238)  # Reichssiegel drücken
    time.sleep(2)

    # ---------- Dein Screenshot-Code ----------
    Rechnungx1 = x1 + 232
    Rechnungy1 = y1 + 292

    screenshot = pyautogui.screenshot(
        region=(int(Rechnungx1), int(Rechnungy1), 50, 20)
    )

    # leichtes Upscaling (3x reicht!)
    screenshot = screenshot.resize((50*3, 20*3))

    pixel_values = processor(
        screenshot,
        return_tensors="pt"
    ).pixel_values.to(device)

    with torch.no_grad():
        ids = model.generate(pixel_values)

    text = processor.decode(ids[0], skip_special_tokens=True)

    text = ''.join(c for c in text if c in "0123456789+")
    print("OCR Text:", text)

    # Rechnung auswerten
    if "+" in text:
        a, b = text.split("+", 1)
        try:
            ergebnis = int(a.strip()) + int(b.strip())
        except:
            ergebnis = 0
    else:
        ergebnis = 0

    print("Ergebnis:", ergebnis)

    # --- Zahl ausgeben ---
    while pause_threads2.is_set():
        time.sleep(0.01)
    pause_threads2.set()
    pydirectinput.click(x1 + 785, y1 + 140)
    for digit in str(ergebnis):
        pydirectinput.press(digit)
    pause_threads2.clear()
    print("End verwandelt")
    if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.leftClick(x1 + 402, y1 + 386)
    time.sleep(1)
    if (pyautogui.pixelMatchesColor(x1 + 402, y1 + 386, (255, 255, 255))):
        while pause_threads2.is_set():
            time.sleep(0.01)
        pydirectinput.leftClick(x1 + 402, y1 + 386)
    global pause_threads
    while pause_threads2.is_set():
        time.sleep(0.01)
    pause_threads.set()
    pause_threads2.set()
    print("Kritischer Bereich")
    pydirectinput.click(x1 + 785, y1 + 140)
    pydirectinput.press('w')
    pydirectinput.press('w')
    sleep(0.05)
    print("Kritischer Bereich Ende")
    pause_threads.clear()
    pause_threads2.clear()

def AutoFisching():
    pydirectinput.click(1000,0)
    while True:
        x1 = 7
        y1 = 0
        t1 = threading.Thread(target=Bot, args=(x1, y1, 2.7))
        t4 = threading.Thread(target=Auswurf, args=(x1, y1))

        x1 = 1757
        y1 = 0
        t2 = threading.Thread(target=Bot, args=(x1, y1, 2.7))
        t5 = threading.Thread(target=Auswurf, args=(x1, y1))

        x1 = 7
        y1 = 770
        t3 = threading.Thread(target=Bot, args=(x1, y1, 2.6))
        t6 = threading.Thread(target=Auswurf, args=(x1, y1))

        print(datetime.datetime.now())
        t1.start()
        print(datetime.datetime.now())
        t2.start()
        print(datetime.datetime.now())
        t3.start()
        print(datetime.datetime.now())
        t4.start()
        print(datetime.datetime.now())
        t5.start()
        print(datetime.datetime.now())
        t6.start()
        t1.join()
        print(datetime.datetime.now())
        t2.join()
        print(datetime.datetime.now())
        t3.join()
        print(datetime.datetime.now())
        t4.join()
        print(datetime.datetime.now())
        t5.join()
        print(datetime.datetime.now())
        t6.join()
        #sleep(2)
        x1 = 7
        y1 = 0
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1)
        Aufstehen(x1, y1)

        x1 = 1757
        y1 = 0
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1)
        Aufstehen(x1, y1)

        x1 = 7
        y1 = 770
        pydirectinput.click(x1 + 760, y1 + 100)
        Drop(x1, y1)
        Aufstehen(x1, y1)

def find_color_in_inv(x1, y1, target_color, tolerance = 0):
    for y in range(y1, y1 + 32*8 + 1, 32):
        for x in range(x1, x1 + 32*4 + 1, 32):
            if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=tolerance):
                return x , y

def Bot(x1, y1, wait_time):
    while True:
        now = datetime.datetime.now()
        if (now.minute % 10 == 0 and now.second < 10):
            return
        pixelMatchesColor = pyautogui.pixelMatchesColor(x1 + 390, y1 + 170, (255, 255, 255), tolerance=10) #Einhol Symbole erkennen
        if(pixelMatchesColor):
            time.sleep(wait_time)
            while pause_threads.is_set():
                time.sleep(0.01)
            global pause_threads2
            pause_threads2.set()
            pydirectinput.click(x1 + 785, y1 + 140)
            pydirectinput.press('space')
            pause_threads2.clear()
            print('Ziehe Fisch raus.')

            time.sleep(4)

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

move_clients()
#move_clientsLeveln()
AutoFisching()

x1=7
x1=7
y1=0

#Drop(x1,y1)
#x, y = find_color_in_inv(x1 + 560, y1 + 450, (38, 26, 20), 8)
#print(x, y)
color = pyautogui.screenshot().getpixel((x1 + 275, y1 + 182))
print(color)
#pydirectinput.moveTo(x1 + 385, y1 + 438)
color = pyautogui.screenshot().getpixel((x1 + 785, y1 + 140))
print(color)


werte = []  # Array für alle RGB-Werte
n = 200

for i in range(n):
    color = pyautogui.screenshot().getpixel((x1 + 385, y1 + 438))
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


