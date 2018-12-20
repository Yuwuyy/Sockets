code = (b'\xb8\x04\xde\xf7')
yaya = ""
octall2 = code.hex()
octall = ""
octall += octall2[-2:]
octall += octall2[4:6]
octall += octall2[2:4]
octall += octall2[:2]
print (octall)
for i in range (4) :
    oct1 = octall[:2]
    octall = octall.replace(oct1,"")
    decode = bin(int(oct1, base=16))
    print(decode)
    decode = decode.replace('0b',"")
    for i in range (len(decode)) :
        yaya += decode[i]

decimal = 0
taillebinaire = len(yaya) # taille du binaire entré

for i in range (len(yaya)): # pour i allant de 0 à la taille de binaire
    decimal += int(yaya[taillebinaire - (i+1)])*pow(2, i) # rajoute a decimal 0 ou 1 multiplié par 2 puissance i

print("Valeur en decimal : ", decimal)
#input_str = '0x'+oui
#c = BitArray(hex=input_str)
#c.bin
#oui2 = bytes.fromhex('b804def7').decode('utf-8')
#oui2 = oui.bin()
#decode2 = decode2.decode(oui, "hex")
#decode2 = oui.decode("hex")
