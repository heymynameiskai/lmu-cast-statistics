from simple_term_menu import TerminalMenu
from termcolor import cprint

def main():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


# ask for auth-key, check it
def welcome():
    # print(colored("LMUCast Statistics Exporter", 'green'))
    cprint("""
 _      __  __ _    _  _____          _      _____ _        _   _     _   _ _              
| |    |  \/  | |  | |/ ____|        | |    / ____| |      | | (_)   | | (_) |             
| |    | \  / | |  | | |     __ _ ___| |_  | (___ | |_ __ _| |_ _ ___| |_ _| | _____ _ __  
| |    | |\/| | |  | | |    / _` / __| __|  \___ \| __/ _` | __| / __| __| | |/ / _ \ '_ \ 
| |____| |  | | |__| | |___| (_| \__ \ |_   ____) | || (_| | |_| \__ \ |_| |   <  __/ | | |
|______|_|  |_|\____/ \_____\__,_|___/\__| |_____/ \__\__,_|\__|_|___/\__|_|_|\_\___|_| |_|
    """, 'green', attrs=['bold'])

    print("Autor: Kai Hennig")
    print("Version: 1.0")
    print("https://github.com/heymynameiskai/lmu-cast-statistics")
    print("")
    cprint("Dieses Programm erstellt für jede LMUCast-Playlist ein PDF der aktuellen Nutzungsstatistik.", 'yellow')

def get_auth_key():
    cprint("Geben Sie Ihren LMUCast Authentification Key ein, um fortzufahren.", 'yellow', attrs=['bold'])
    authkey = input("Auth-Key: ")
    print(authkey)


# show all playlists, select multiple





# show export location, continue to export, open export dir





if __name__ == "__main__":
    welcome()
    get_auth_key()