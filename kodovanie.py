import PIL
sprava = "Ahoj svet#"
dlzka = 8

def priprav(sprava:str)->list:
    res = []
    for pismenko in sprava:
        cislo = bin(ord(pismenko))[2:]
        while len(cislo) < dlzka:
            cislo = "0" + cislo
        for j in cislo:
            res.append(int(j))
    return res

from PIL import Image

obr = Image.open("obrazok.png")
pixels = obr.load()

def drticka(sprava:str):
    spvds = priprav(sprava)
    for i in range(len(spvds)):
        sirka = obr.size[0]
        vyska = obr.size[1]
        x = i % sirka
        y = i // sirka
        pixelblue = pixels[x, y][2]
        new_blue = int(bin(pixelblue)[2:-1] + str(spvds[i]),2)
        new_color = (pixels[x,y][0], pixels[x,y][1], new_blue, pixels[x,y][3])
        pixels[x,y] = new_color
    obr.save("obrazokspr.png")
drticka(sprava)

