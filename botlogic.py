import random

def gen_pass(pass_length):
    elements = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&-=+;:,./?<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coin():
    moneta = random.randint(0,1)
    if moneta == 0:
        return('Orzeł')
    else:
        return('Reszka')
    
def gen_emoji():
    emoji = "🙂😀😆🤣😍😜😈😇🤑😎😂💀"
    return random.choice(emoji)

def kostka(sciany):
    return random.randint(1, sciany)
