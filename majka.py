import pyautogui, time
from random import randint
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime


start=datetime.now()
global ingame


class bot:
    def __init__(self):
        self.exp = 0

    def lobby(self): #checking lobby
        time.sleep(10)
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " > waiting for menu")
        print(Style.RESET_ALL)
        while True:
            lobby = pyautogui.locateOnScreen("ImageChecks/lobby.png")
            lobby2 = pyautogui.locateOnScreen("ImageChecks/lobby.png", confidence=0.6)
            if lobby is not None or lobby2 is not None:
                print(Fore.GREEN + " in-menu")
                print(Style.RESET_ALL)
                if lobby != None:
                    pyautogui.click(lobby)   
                if lobby2 != None:
                    pyautogui.click(lobby2)    
                time.sleep(1)
                self.ingame()
        
    def ingame(self): #checking mathmaking
        print(Fore.YELLOW + " > waiting for game")
        print(Style.RESET_ALL)
        while True:
            ingame = pyautogui.locateOnScreen(banner)
            ingame2 = pyautogui.locateOnScreen(banner, confidence=0.6)
            if ingame is not None or ingame2 is not None:
                print(Fore.GREEN + " in-game")
                print(Style.RESET_ALL)
                time.sleep(1)
                print(Fore.YELLOW + " > waiting for the end of the game")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.endofthegame()

    def endofthegame(self):
        time.sleep(5)
        while True:
            compteur = pyautogui.locateOnScreen("ImageChecks/confirm2.png")
            compteur2 = pyautogui.locateOnScreen("ImageChecks/confirm2.png", confidence=0.6)
            if compteur is not None or compteur2 is not None:
                print(Fore.GREEN + " game-end")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.result()
            else:
                self.antiafk()

    def antiafk(self):
        time.sleep(5)
        n = randint(20, 35)
        a = 0
        while a <= n:
            a += 1
            n2 = randint(1,6)
            if n2 == 1:
                pyautogui.keyDown('w')
                sleep(randint(2, 6)/10)
            if n2 == 2:
                pyautogui.keyUp('w')
                pyautogui.keyDown('d')
                pyautogui.click()
            if n2 == 3:
                pyautogui.keyDown('a')
                sleep(randint(1, 3)/10)
                pyautogui.keyDown('a')
                pyautogui.click()
                sleep(randint(2, 4)/10)
            if n2 == 4:
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                sleep(randint(2, 5)/10)
            if n2 == 5:
                pyautogui.keyUp('s')
                sleep(randint(4, 6)/10)
            if n2 == 6:
                pyautogui.keyDown('w')
                sleep(randint(2, 4)/10)
                pyautogui.keyUp('w')

        self.endofthegame()

    def result(self):
        print(Fore.YELLOW + " > waiting for menu xp screen")
        print(Style.RESET_ALL)
        time.sleep(10)
        while True:
            results = pyautogui.locateOnScreen("ImageChecks/confirm.png")
            results2 = pyautogui.locateOnScreen("ImageChecks/confirm.png", confidence=0.6)
            if results is not None or results2 is not None:
                print(Fore.GREEN + " xp-screen")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.exp += 900
                print(Fore.MAGENTA + self.exp, " xp")
                print(Fore.MAGENTA + "[DEBUG] runned for",datetime.now()-start)
                print(Style.RESET_ALL)
                print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print(Style.RESET_ALL)
                time.sleep(2)
                pyautogui.click(x=980, y=30)
                time.sleep(2)
                self.lobby()          

a = bot()

def main():

    from colorama import init
    from colorama import Fore, Back, Style
    init()
    print (Fore.RED + """
    ▄▄▄▄███▄▄▄▄      ▄████████      ▄█    ▄█   ▄█▄    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄   ███    ███     ███   ███ ▄███▀   ███    ███ 
 ███   ███   ███   ███    ███     ███   ███▐██▀     ███    ███ 
 ███   ███   ███   ███    ███     ███  ▄█████▀      ███    ███ 
 ███   ███   ███ ▀███████████     ███ ▀▀█████▄    ▀███████████ 
 ███   ███   ███   ███    ███     ███   ███▐██▄     ███    ███ 
 ███   ███   ███   ███    ███     ███   ███ ▀███▄   ███    ███ 
  ▀█   ███   █▀    ███    █▀  █▄ ▄███   ███   ▀█▀   ███    █▀   """)
    print(Style.RESET_ALL)


    print(Style.RESET_ALL)
    print("")
    print(Fore.RED + "              made by sora#xdd (ethan#1439)")
    print("")
    print(Style.RESET_ALL)
    
    time.sleep(1/2)
    print("")
    print(Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(Style.RESET_ALL)
    time.sleep(1/2)
    print (Style.BRIGHT + Fore.RED)
    print(Fore.RED+" 1)",Fore.RED+"launch")
    print("")
    print(Fore.RED+" 2)",Fore.RED+"exit")
    print("")
    print(Fore.RED+" 3)",Fore.RED+"help")
    print("")
    print(Style.BRIGHT + Fore.RED+"")
    menu = int(input(" > "))
    
    try:
        if menu == 1:
            print ("")
            print(Style.RESET_ALL,Fore.YELLOW+"select a banner in-game")
            print ("")
            print (Style.BRIGHT,Fore.WHITE+"1)",Fore.YELLOW+"beta banner")
            print("")
            print (Fore.WHITE+" 2)",Fore.YELLOW+"valorant default banner",Style.RESET_ALL,)
            print ("")
            print (Fore.WHITE+" 3)",Fore.WHITE+"back")
            print ("")
            print(Style.BRIGHT + Fore.RED+"")
            banneroption = int(input(" > "))
            try:
                global banner
                if banneroption == 1:
                    banner = ("ImageChecks/1.png")
                    print (Style.RESET_ALL)
                    print (Fore.RED+" selected (beta)")
                elif banneroption == 2:
                    banner = ("ImageChecks/2.png")
                    print (Style.RESET_ALL)
                    print (Fore.RED+" selected (default)")
                elif banneroption == 3:
                    main()
                else:
                    print (Fore.RED+" error")
                    time.sleep(2)
                    main()
            except ValueError:
                print (" error")
                time.sleep(2)
                main()
            
            print (Style.RESET_ALL)
            time.sleep(2)
            print(Fore.WHITE + " 1)",Fore.CYAN +"make sure valorant is focused FIRST:",Fore.BLUE +"PLAY",Fore.CYAN +"and then click",Fore.BLUE+"DEATHMATCH", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"wait around",Fore.BLUE +"10 seconds",Fore.CYAN +"and do not click anything", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"enjoy", Style.RESET_ALL)
            print ("")
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print("")
            time.sleep(5)
            a.lobby()

        elif menu == 2:
            print(" bye")
            print(" ")
            time.sleep(2)
            quit()

        elif menu == 3:
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.RESET_ALL+"")
            
            print(Fore.RED + " how to run(?)")
            print("")
            print(Fore.WHITE + " 1)",Fore.CYAN +"open the game and click",Fore.BLUE +"PLAY",Fore.CYAN +"and then click",Fore.BLUE+"DEATHMATCH", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)",Fore.CYAN +"run this by selecting",Fore.BLUE +"1",Fore.CYAN +"in the main menu")
            print("")
            print(Fore.WHITE + " 3)",Fore.CYAN +"change your player banner")
            print(Fore.BLUE +" beta banner",Fore.CYAN +"or the",Fore.BLUE +"default banner",Fore.CYAN)
            print("")
            print(Fore.WHITE + " 4)",Fore.CYAN +"select the banner you have selected in the",Fore.BLUE +"console",Fore.CYAN)
            print("")
            print(Fore.WHITE + " 5)",Fore.CYAN +"doesnt move your mouse or press any key.")
            print("")
            print(Fore.CYAN +" how to stop the bot?",Fore.BLUE +"simply close this window",Fore.CYAN)
            print("")
            print("")
            print(Fore.RED + " OTHER PRECAUTIONS AND INFORMATION")
            print("")
            print(Fore.CYAN +" it is advised to turn the Name Hide option on in",Fore.BLUE +"Settings > Privacy",Fore.CYAN)
            print("")
            print("") 
            print(Fore.RED + " XP INFO")
            print("")
            print(Fore.CYAN +" Minimum XP gain are as follows")
            print(Fore.WHITE +" 1h:",Fore.MAGENTA +"3,6k XP")
            print(Fore.WHITE +" 8h:",Fore.MAGENTA +"28,8k XP")
            print(Fore.WHITE +" 24h:",Fore.MAGENTA +"86,4 XP")
            
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print(Style.BRIGHT,Fore.RED)
            print("")
            print(" press any key to return")
            print(Style.RESET_ALL+"")
            print ("")
            menureturn = input(" > ")
            main()
                
                
            print(Style.BRIGHT + Fore.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            time.sleep(30)
            main()
        else:
            print (" error")
            time.sleep(2)
            main()
    except ValueError:
        print (" error")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
