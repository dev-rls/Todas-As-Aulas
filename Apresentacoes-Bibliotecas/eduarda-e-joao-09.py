#Colorama
'''from colorama import Fore, Style, init
init()
print(Fore.GREEN + "Green")
print(Fore.BLACK + "Black")
print(Fore.BLUE + "Blue")

print(Style.RESET_ALL + "Texto na cor padrão")

from colorama import Fore, Style, init, Back
init()
print(Fore.RED + "Vermelho")
print(Fore.BLACK + "Black")
print(Fore.BLUE + "Blue")

print(Back.YELLOW + "Texto na cor padrão")'''

#Pyfiglet
'''import pyfiglet

text = "Quintooou!"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)'''

'''import pyfiglet

text = "Quintooou!"
ascii_art_standard = pyfiglet.figlet_format(text, font="siant")
print(ascii_art_standard)'''

# import pyfiglet

# text = "Seja Luz"
# ascii_art_slant = pyfiglet.figlet_format(text, font="slant")
# print(ascii_art_slant)

'''import pyfiglet
from colorama import Fore, Style

from colorama import init
init(autoreset=True)

text= "Obrigadaaan"

ascii_art = pyfiglet.figlet_format(text, font="slant")
print(Fore.BLUE + Style.BRIGHT + ascii_art)'''

'''Exercicio
02 - Faça uma lista com 5 palavras que imprima com as cores vermelho, azul, branco, amarelo e verde.'''

#Colorama
from colorama import Fore, Style, init
init()
print(Fore.RED + "Maça")
print(Fore.BLUE + "Céu")
print(Fore.WHITE + "Leite")
print(Fore.YELLOW + "Gema de ovo")
print(Fore.GREEN + "Arvore")
