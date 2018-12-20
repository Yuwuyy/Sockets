import socket
UDP_IP = "10.160.108.101"
UDP_PORT = 5005
MESSAGE = (b"?")
def code (code) :
    octall2 = code.hex()
    octall = ""
    octall += octall2[-2:]
    octall += octall2[4:6]
    octall += octall2[2:4]
    octall += octall2[:2]
    print (octall)

    hexadecimal = octall
    decimal = 0
    taillehexa = len(hexadecimal)

    for i in range (taillehexa):
                   
        if (hexadecimal[taillehexa - (i+1)] == "a"):
            decimal += 10 * pow(16, i)
        elif (hexadecimal[taillehexa - (i+1)] == "b"):
            decimal += 11 * pow(16, i)
        elif (hexadecimal[taillehexa - (i+1)] == "c"):
            decimal += 12 * pow(16, i)
        elif (hexadecimal[taillehexa - (i+1)] == "d"):
            decimal += 13 * pow(16, i)
        elif (hexadecimal[taillehexa - (i+1)] == "e"):
            decimal += 14 * pow(16, i)
        elif (hexadecimal[taillehexa - (i+1)] == "f"):
            decimal += 15 * pow(16, i)
        else :
            decimal += (int(hexadecimal[taillehexa - (i+1)])) * pow(16, i)

    print("La valeur en decimal est : ", decimal)
    decimal = str(decimal)
    sock.sendto(decimal.encode(), (UDP_IP, UDP_PORT))
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("cinema".encode(), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print("Instruction : ", data)
code(data)
data, addr = sock.recvfrom(1024)
print("Instruction : ", data)


    
    #Instruction :  b'\xb8\x04\xde\xf7'
