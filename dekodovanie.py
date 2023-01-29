import PIL
from PIL import Image

obr = Image.open("obrazokspr.png")
pixels = obr.load()

dlzka = 8

def zisk_modrej():
    zoz = []
    for y in range(obr.size[1]):
        for x in range(obr.size[0]):
            pixel_blue = pixels[x,y][2]
            blue = bin(pixel_blue)
            zoz.append(blue[-1])
    return zoz

zoz = zisk_modrej()
def desifrovacka(zoz):
    sprava = ""
    cislo = ""
    for i in zoz:
        x = ""
        cislo += i
        if len(cislo) == dlzka:
            x = chr(int(cislo,2))
            sprava += x
            cislo = ""
        if "#" in sprava:
            break
    return sprava

print(desifrovacka(zoz))
