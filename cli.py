from simple_term_menu import TerminalMenu
from termcolor import cprint
import api
import pdf
from datetime import datetime


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

def main_menu():
    options = ["PDFs für alle Playlists exportieren", "PDFs für ausgewählte Playlists exportieren", "Programm beenden"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if(menu_entry_index == 0):
        export_all_PDFs()
    elif(menu_entry_index == 1):
        export_selected_PDFs()
    elif(menu_entry_index == 2):
        print("exit")


def export_all_PDFs():
    playlists = api.get_all_playlists()
    playlist_count = len(playlists)
    for i in playlists:
        print((playlists.index(i) + 1), "/", playlist_count, ": ", end='')
        generate_PDF_by_ID(i['id'])



def export_selected_PDFs():
    # get all playlists and generate an easy-to-read name (name + url) for multi-select menu
    playlists = api.get_all_playlists()
    options = []
    for i in playlists:
        i['display'] = i['name'] + " (" + i['url'] + ")"
        options.append(i['display'])

    # init menu
    terminal_menu = TerminalMenu(
        options,
        multi_select=True,
        show_multi_select_hint=True,
        multi_select_select_on_accept=False
    )
    menu_entry_indices = terminal_menu.show()


    # for each element of choosen entries, find element in playlists[] with same display-name, and append playlist-id to selection[]
    # selection is an array of all playlist-ids to generate pdfs from
    selected_playlists = []
    for i in terminal_menu.chosen_menu_entries:
        selected_playlists.append(next(item for item in playlists if item['display'] == i)['id'])

    # for each element in selection[], generate pdf and export into chosen folder
    playlist_count = len(selected_playlists)
    for i in selected_playlists:
        print((selected_playlists.index(i)+1), "/",playlist_count, ": ", end = '')
        generate_PDF_by_ID(i)





def generate_PDF_by_ID(playlist_id):
    playlist_attributes = api.get_single_playlist(playlist_id)
    playlist_name = playlist_attributes['name']
    print("Exportiere " + playlist_name + " [ID: " + playlist_id + "]...")

    now = datetime.now()
    date = now.strftime("%d.%m.%Y %H:%M Uhr")

    playlist_url = playlist_attributes['url']
    playlist_hits = api.get_playlist_total_hits(playlist_id)

    pdf.printStatistics(file_name=playlist_name, date=date, playlist_title=playlist_name, playlist_url=playlist_url,
                        hits=playlist_hits)


    # datetime object containing current date and time





if __name__ == "__main__":
    # welcome()
    # get_auth_key()
    main_menu()
