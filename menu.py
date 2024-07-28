from colorama import init, Fore, Style
import keyboard
import threading
import time
init()

TEXT_COLORS = {
    "Magenta": Fore.MAGENTA + Style.BRIGHT
}

class Menu:
    def __init__(self, game_state):
        self.game_state = game_state
        self.menu_options = ["View Hand", "View Hoards", "View Discard Pile", "View Scoreboard"]
        self.menu_displayed = False
        #self.menu_thread = threading.Thread(target=self.listen_for_keypresses, daemon=True)
        #self.menu_thread.start()
    
    def listen_for_keypresses(self):
        keyboard.add_hotkey('m', self.toggle_menu)
        while True:
            time.sleep(0.1)

    def toggle_menu(self):
        self.menu_displayed = not self.menu_displayed
        if self.menu_displayed:
            self.display_menu()
        else:
            print(f"{Style.RESET_ALL}")

    def display_menu(self):
        self.toggle_menu()
        color = TEXT_COLORS["Magenta"]
        print()
        for index, option in enumerate(self.menu_options):
            print(f"{color}{index + 1}. {option}{Style.RESET_ALL}") 

