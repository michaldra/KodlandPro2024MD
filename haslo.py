import random
znaki = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*-_=+;:,./?"
while True:
    dlugosc = int(input("Podaj długość hasła: "))
    haslo = ""
    for i in range(dlugosc):
        haslo = haslo + znaki[random.randint(0,len(znaki)-1)]
    print(haslo)