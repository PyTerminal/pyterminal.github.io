import os
os.system("color a")
os.system("title PyTerminal")
def terminal():
    commands =["isdir", "github", "repository", "listcmd", "pingwp", "mkdir" "color", "title", "tracert", "isfile", "iscommand", "python", "goto", "cd","webview", "batch", "exists", "rem", "echo", "output", "ping", "exit", "help", "listfile", "listdir", "openfile", "color", "rem", "cls", "ipconfig", "start"]
    command = input("Enter command(type help or /? or listcmd for help > ")
    if command == "help" or command == "/?" or command == "listcmd":
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
        if output != "":
            os.system("echo " + output)
        terminal()
    if command == "exit":
        exit()
    if command == "ping":
        destination = input("Enter who you want to ping > ")
        if destination != "":
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
        if file != "":
            if os.path.exists(file):
                if os.path.isfile(file):
                    os.system("notepad " + file)
                else:
                    print("You can not enter a directory")
        terminal()
    if command == "rem":
        file = input("Enter a file or directory > ")
        if file != "":
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
        if color != "":
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
        terminal()
    if command == "exists":
        file = input("Enter a file or directory > ")
        if file != "":
            if os.path.exists(file):
                print("The file or directory exists!")
            else:
                print("The file or directory doesn't exist!")
        else:
            terminal()
        terminal()
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
        if url != "":
            webbrowser.open_new(url)
        else:
            terminal()
        terminal()
    if command == "start":
        program = input("Enter a program > ")
        if program != "":
            os.system("start " + program)
        else:
            terminal()
        terminal()
    if command == "cd":
        os.system("cd")
    if command == "goto":
        destination = input("Enter destination > ")
        if destination != "":
            os.system("cd " + destination)
        else:
            terminal()
        terminal()
    if command == "isdir":
        directory = input("Enter a directory > ")
        if os.path.isdir(directory):
            print("True")
        else:
            print("False")
        terminal()
    if command == "isfile":
        file = input("Enter a file > ")
        if os.path.isfile(file):
            print("True")
        else:
            print("False")
        terminal()
    if command == "iscommand":
        cmd = input("Enter a command > ")
        if cmd in commands or cmd == "/?":
            print("True")
        else:
            print("False")
        terminal()
    if command == "python":
        python = input("Enter a python file (optinal) > ")
        if python == "":
            os.system("python")
         else:
            os.system("python " + python)
         terminal()
    if command == "tracert":
        website = input("Enter a website > ")
        os.system("tracert " + website)
        terminal()
    if command == "arp":
        cmd = input("Enter > ")
        if cmd != "":
            os.system("arp " + cmd)
        else:
            os.system("arp")
        terminal()
    if command == "netstat":
        cmd = input("Enter > ")
        if cmd != "":
            os.system("netstat " + cmd)
        else:
            os.system("netstat")
        terminal()
    if command == "mkdir":
        directory = input("Enter directory name > ")
        if os.path.exists(directory):
            print("The directory already exists!")
        else:
            os.system("mkdir " + directory)
    if command == "title":
        title = input("Enter  title > ")
        if title != "":
            os.system("title " + title)
        else:
            terminal()
        terminal()
    if command == "repository":
        import webbrowser
        webbrowser.open_new("https://github.com/PyTerminal/pyterminal.github.io/")
    if command == "pingwp":
        packets = input("Enter packet amount 1-6550 > ")
        if packets < 6551:
            destination = input("Enter destination > ")
            repeat = input("Do you want to repeat it? True/False > ")
            if repeat == True:
                os.system("ping " + destination + "-t -l " + packets)
            if repeat == False:
                os.system("ping " + destination + "-l " + packets)
         else:
            print("You can only enter 1-6550!")
            terminal()
      if command == "github":
        project == input("Enter project URL(optional) > ")
        if project != "":
            import webbrowser
            webbrowser.open_new(project)
        else:
            webbrowser.open_new("https://github.com")
        terminal()
      if command != commands:
        print("The command you just entered might be unkown. The commands are > ")
        for command in commands:
            print(command)
        print("If the command is not unknown there is a bug in the program. Feel free to edit the program when ever you like")
        terminal()
terminal()
