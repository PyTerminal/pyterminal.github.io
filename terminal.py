#Feel free to edit code without permission.
import os
os.system("color a")
os.system("title PyTerminal")
def terminal():
    commands = ["python", "goto", "cd","webview", "batch", "exists", "rem", "echo", "output", "ping", "exit", "help", "listfile", "listdir", "openfile", "color", "rem", "cls", "ipconfig", "start"]
    command = input("Enter command > ")
    if command == "help" or command == "/?":
        print("The commands are > ")
        for command in commands:
            print(command)
        terminal()
    if command == "echo":
        output = input("Enter something to output > ")
        print(output)
        terminal()
    if command == "output":
        output = input("Enter something to output ")
        os.system("echo " + output)
        terminal()
    if command == "exit":
        exit()
    if command == "ping":
        destination = input("Enter who you want to ping > ")
        os.system("ping " + destination)
        terminal()
    if command == "":
        terminal()
    if command == "listfile":
        files = []
        for file in os.listdir():
            if os.path.isfile(file):
                files.append(file)
            else:
                continue
        for file in files:
            print(file)
        terminal()
    if command == "listdir":
        folders = []
        for folder in os.listdir():
            if os.path.isdir(folder):
                folders.append(folder)
            else:
                continue
        for folder in folders:
            print(folder)
        terminal()
    if command == "openfile":
        file = input("Enter a file > ")
        if os.path.exists(file):
            if os.path.isfile(file):
                os.system("notepad " + file)
            else:
                print("You can not enter a directory")
        terminal()
    if command == "rem":
        file = input("Enter a file or directory > ")
        if os.path.exists(file):
            if os.path.isfile(file):
                if file != "terminal.py":
                    os.remove(file)
                else:
                    print("You have to manually remove the terminal.")
            else:
                os.rmdir(file)
        else:
            print("The file or directory doesn't exist!")
        terminal()
    if command == "color":
        color = input("Enter > ")
        os.system("color " + color)
        terminal()
    if command == "cls":
        os.system("cls")
        terminal()
    if command == "ipconfig":
        option = input("Enter > ")
        if option != "":
            os.system("ipconfig /" + option)
        else:
            os.system("ipconfig")
    if command == "exists":
        file = input("Enter a file or directory > ")
        if os.path.exists(file):
            print("The file or directory exists!")
        else:
            print("The file or directory doesn't exist!")
    if command == "batch":
        print("Running batch files could be dangerous. USE AT OWN RISK. Hit enter key to not run a batch file.")
        batch = input("Where is the batch file? ")
        if batch != "":
            os.system(batch)
        else:
            print("You didn't run a batch file.")
            terminal()
        terminal()
    if command == "webview":
        import webbrowser
        url = input("Enter a website > ")
        webbrowser.open_new(url)
    if command == "start":
        program = input("Enter a program > ")
        os.system("start " + program)
        terminal()
    if command == "cd":
        os.system("cd")
    if command == "goto":
        destination = input("Enter destination > ")
        os.system("cd " + destination)
    if command == "python":
        python = input("Enter a python file (optinal) > ")
        os.system("python " + python)
    if command != commands:
        print("The command you just entered might be unkown. The commands are > ")
        for command in commands:
            print(command)
        print("If the command is not unkown there is a bug in the program. Feel free to edit the program when ever you like")
        terminal()
terminal()
