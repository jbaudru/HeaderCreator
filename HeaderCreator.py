#===============================================================================
#   Project Name : Header Maker V.1
#   Author Name :  Baudru J.
#   Date :         2020-02-15
#===============================================================================

from datetime import date
import os


def welcome():
    print("\n                   _    _                _           ")
    print("                  | |  | |              | |          ")
    print("                  | |__| | ___  __ _  __| | ___ _ __ ")
    print("                  |  __  |/ _ \/ _` |/ _` |/ _ | '__|")
    print("                  | |  | |  __| (_| | (_| |  __| |   ")
    print("                  |_|__|_|\___|\__,_|\__,_|\___|_|   ")
    print("                 / ____|              | |            ")
    print("                | |     _ __ ___  __ _| |_ ___  _ __ ")
    print("                | |    | '__/ _ \/ _` | __/ _ \| '__|")
    print("                | |____| | |  __| (_| | || (_) | |   ")
    print("                 \_____|_|  \___|\__,_|\__\___/|_| v.0.0.1 ")
    print("                                                     ")


def show_menu():
    print(" ====================================================================")
    print(" | Select a langage :                                               |")
    print(" |------------------------------------------------------------------|")
    print(" |    01 - Python/Bash/Perl/Ruby  |    02 - C/C++/Java/Swift        |")
    print(" |    03 - Latex/MatLab           |    04 - SQL/Haskell/Lua         |")
    print(" |    05 - Visual Basic .NET      |    06 - Fortran 90              |")
    print(" |    07 - BASIC                  |                                 |")
    print(" |------------------------------------------------------------------|")
    print(" |                                     99 - Quit HeaderCreator      |")
    print(" ====================================================================")


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    show_menu()
    choice = ['1', '2', '3', '4', '5', '6', '7', '01', '02', '03', '04', '05', '06', '07', '99']
    langage_choice = input("  > ")
    while( (langage_choice.isdigit() == False) or (langage_choice not in choice) ):
        clean_screen()
        welcome()
        show_menu()
        print(" [Error]               Please choose a number.                [Error] ")
        langage_choice = input("  > ")


    if(int(langage_choice) == 99):
        print("\n")
        quit()

    dat, project_name, author_name = project_data()
    if(int(langage_choice) == 1):
        separator = "#"
    if(int(langage_choice) == 2):
        separator = "//"
    if(int(langage_choice) == 3):
        separator = "%"
    if(int(langage_choice) == 4):
        separator = "--"
    if(int(langage_choice) == 5):
        separator = "'"
    if(int(langage_choice) == 6):
        separator = "!"
    if(int(langage_choice) == 7):
        separator = "REM "

    create_header(dat, project_name, author_name, separator)
    main()


def project_data():
    dat = str(date.today())
    print("\n\n ====================================================================")
    print(" | Project name :                                                   |")
    print(" ====================================================================")
    project_name = input("  > ")
    print("\n\n ====================================================================")
    print(" | Author name :                                                    |")
    print(" ====================================================================")
    author_name = input("  > ")
    print("\n\n ====================================================================")
    print(" | Opening header...                                                |")
    print(" ====================================================================\n")
    return dat, project_name, author_name


def create_header(dat, project_name, author_name, separator): #aussi pour bash
    f = open("temp.txt", 'w')
    f.close()
    header = separator + "===============================================================================" + "\n"
    header += separator + "   Project Name : " + project_name + "\n"
    header += separator + "   Author Name :  " + author_name + "\n"
    header += separator + "   Date :         " + dat + "\n"
    header += separator + "===============================================================================" + "\n"
    f = open("temp.txt", "a+")
    f.write(header)
    f.close()
    os.startfile("temp.txt")


def main():
    clean_screen()
    welcome()
    menu()


if __name__ == "__main__":
    main()
