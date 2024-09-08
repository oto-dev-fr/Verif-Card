import re
from colorama import Fore, Style, init
import socket
import os
import platform

# Initialisation de colorama
init(autoreset=True)

class Color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

def validate_credit_card(number):
    """Applique l'algorithme de Luhn pour valider le numéro de carte."""
    number = str(number)
    total = 0
    reverse_digits = number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10 == 0

def clear_screen():
    """Efface l'écran de la console."""
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
    pc_name = socket.gethostname()  # Obtient le nom de l'ordinateur

    while True:
        clear_screen()
        print(Color.RED + '''
 ▄████▄   ▄▄▄       ██▀███  ▓█████▄     ██▒   █▓ ▄▄▄       ██▓     ██▓▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌   ▓██░   █▒▒████▄    ▓██▒    ▓██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌    ▓██  █▒░▒██  ▀█▄  ▒██░    ▒██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌     ▒██ █░░░██▄▄▄▄██ ▒██░    ░██░░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓       ▒▀█░   ▓█   ▓██▒░██████▒░██░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒       ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░░▓   ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒       ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░          ░   ▒     ░░   ░  ░ ░  ░         ░░    ░   ▒     ░ ░    ▒ ░ ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
░ ░            ░  ░   ░        ░             ░        ░  ░    ░  ░ ░     ░          ░  ░            ░ ░     ░     
░                            ░              ░                          ░                                                 
''' + Color.WHITE + "fully coded by oto.dev" + Color.RESET)

        # Affiche les options disponibles
        print(f"{Color.RED}[{Color.RESET}1{Color.RED}]{Color.RESET} Vérifier plusieurs cartes")
        print(f"{Color.RED}[{Color.RESET}2{Color.RED}]{Color.RESET} Vérifier une seule carte")
        
        # Affiche le prompt pour la saisie du choix
        choice = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Choisissez une option : ").strip()
        
        if choice == '1':
            while True:
                card_numbers = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Veuillez entrer les numéros de carte séparés par des virgules : {Color.RESET}").strip()
                card_numbers = [number.strip() for number in card_numbers.split(',')]
                
                if not all(re.match(r'^\d+$', number) for number in card_numbers):
                    print(f"{Color.RED}[!] {Color.WHITE}Erreur : Tous les numéros de carte doivent contenir uniquement des chiffres.{Color.RESET}")
                    input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
                    clear_screen()
                    continue
                
                for card_number in card_numbers:
                    is_valid = validate_credit_card(card_number)
                    status = Color.GREEN + "Valide" + Color.RESET if is_valid else Color.RED + "Invalide" + Color.RESET
                    print(f"{Color.GREEN}[+] {Color.WHITE}Numéro de carte : {card_number} est {status}{Color.RESET}")
                break
        
        elif choice == '2':
            while True:
                card_number = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Veuillez entrer le numéro de carte de crédit : {Color.RESET}").strip()
                
                if not re.match(r'^\d+$', card_number):
                    print(f"{Color.RED}[!] {Color.WHITE}Erreur : Le numéro de carte doit contenir uniquement des chiffres.{Color.RESET}")
                    input(f"{Color.GREEN}┌───({Color.RESET}{pc_name}{Color.GREEN})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
                    clear_screen()
                    continue
                
                is_valid = validate_credit_card(card_number)
                
                if is_valid:
                    print(f"{Color.GREEN}[+] {Color.WHITE}Votre numéro de carte est {Color.GREEN}Valide{Color.RESET}")
                else:
                    print(f"{Color.RED}[!] {Color.WHITE}Votre numéro de carte est {Color.RED}Invalide{Color.RESET}")
                break
        
        else:
            print(f"{Color.RED}[!] {Color.WHITE}Choix invalide. Veuillez sélectionner 1 ou 2.{Color.RESET}")
            input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
            clear_screen()
            continue
        
        break

    input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour quitter...{Color.RESET}")

if __name__ == '__main__':
    main()