import os
from colorama import Fore, Back, Style
#TODO ricerca by url, metti l'url prende l'ID e ti cerca by ID

def target(max):
    x = input(Fore.GREEN + "Name:Surname: ")
    file_output = input("Output file: ")

    if file_output in os.listdir():
        print('Already Existing file')
        open('file.txt', 'w').close()

    else:
                         
        open(file_output, "x")
                
        fout = open(file_output, "a")

        i = 1

        perc = 0

        for path, dirs, files in os.walk("all"):
            
            for f in files:
                
                filename = os.path.join(path, f)

                file = open(filename, 'r', encoding = 'utf8')

                print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

                perc = perc + 1

                for line in file:

                    if x in line:

                        print(Fore.RED + '[+] Found: ' + str(i))
                        print(Fore.RED + '[+] ' + Fore.GREEN + line)
                        i = i + 1
                                        
                        lv = str(line.encode('utf8', errors = 'replace')).split('/n')
                        for t in lv:
                            
                            fout.write(t)
                                        
                            fout.write('\n')

        file.close()
        fout.close()
        print('File Created!')

def phone(max):

    x = input("Phone number: ")
    fout = open('phone_output.txt', "a", encoding = 'utf8')

    i = 1

    print('Searching...')

    perc = 0
    
    for path, dirs, files in os.walk("all"):

        for f in files:
                
            filename = os.path.join(path, f)

            file = open(filename, 'r', encoding = 'utf8')
            
            print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

            perc = perc + 1

            for line in file:
                                
                if x in line:
                        
                    print('Found:')
                    print(Fore.RED + '[+] ' + Fore.GREEN + line)
                    i = i + 1
                                        
                    lv = str(line.encode('utf8', errors = 'replace')).split('/n')

                    for t in lv:
                        fout.write(t)
                                        
                    fout.write('\n')

                    file.close()
                    fout.close()
                    print('File Edited!')

                    quit()

    fout.write(x + ': NOT_FOUND\n')
    print(x + ': NOT_FOUND')

    file.close()
    fout.close()
    print('File Edited!')

def multiplet(max):

    cond = True
    arrayofppl = []

    while cond:

        arrayofppl.append(input(Fore.GREEN + "Name:Surname: "))

        cond2 = input('Continue? [y/n]')    #[y/n], [s/n], [si/no], [yes, no] (no case sensitive)

        if((cond2.lower() == 'y') or (cond2.lower() == 's') or (cond2.lower() == 'yes') or (cond2.lower() == 'si')):
            pass

        elif((cond2.lower() == 'n') or (cond2.lower() == 'no')):
            cond = False

        else:
            print('Error, Wrong Input!')
            quit()

    file_output = input("Output file: ")

    if file_output in os.listdir():
        print('Already Existing file')
        open('file.txt', 'w').close()

    else:
                         
        open(file_output, "x")
                
        fout = open(file_output, "a")

        i = 1

        perc = 0

        for path, dirs, files in os.walk("all"):
            
            for f in files:
                
                filename = os.path.join(path, f)

                file = open(filename, 'r', encoding = 'utf8')

                print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

                perc = perc + 1

                for line in file:

                    for x in arrayofppl:

                        if x in line:

                            print(Fore.RED + '[+] Found: ' + str(i))
                            print(Fore.RED + '[+] ' + Fore.GREEN + line)
                            i = i + 1
                                            
                            lv = str(line.encode('utf8', errors = 'replace')).split('/n')
                            for t in lv:
                                
                                fout.write(t)
                                            
                                fout.write('\n')

        file.close()
        fout.close()
        print('File Created!')

def multiplep(max):

    cond = True
    arrayofnb = []

    while cond:

        arrayofnb.append(input(Fore.GREEN + "Phone number: "))

        cond2 = input('Continue? [y/n]')    #[y/n], [s/n], [si/no], [yes, no] (no case sensitive)

        if((cond2.lower() == 'y') or (cond2.lower() == 's') or (cond2.lower() == 'yes') or (cond2.lower() == 'si')):
            pass

        elif((cond2.lower() == 'n') or (cond2.lower() == 'no')):
            cond = False

        else:
            print('Error, Wrong Input!')
            quit()

    fout = open('phone_output.txt', "a", encoding = 'utf8')
    
    i = 1

    tot = 0

    print('Searching...')

    perc = 0
    
    for path, dirs, files in os.walk("all"):

        for f in files:
                
            filename = os.path.join(path, f)

            file = open(filename, 'r', encoding = 'utf8')
            
            print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

            perc = perc + 1

            for line in file:

                for line in file:

                    for x in arrayofnb:

                        if x in line:

                            print(Fore.RED + '[+] Found: ' + str(i))
                            print(Fore.RED + '[+] ' + Fore.GREEN + line)
                            i = i + 1
                                            
                            lv = str(line.encode('utf8', errors = 'replace')).split('/n')
                            for t in lv:
                                
                                fout.write(t)
                                            
                                fout.write('\n')

                                tot = tot + 1

        if tot == 0:
                fout.write(x + ': NOT_FOUND\n')
                print(x + ': NOT_FOUND')


    file.close()
    fout.close()
    print('File Edited!')

def targetwf(): #error they print multiple time the target i dunno why

    x = input(Fore.GREEN + "Name:Surname: ")

    file_input = input(Fore.GREEN + "Nationality: ")

    file_output = input("Output file: ")

    if file_output in os.listdir():
        print('Already Existing file')
        open('file.txt', 'w').close()

    else:
                         
        open(file_output, "x")
                
        fout = open(file_output, "a")

        i = 1

        perc = 1

        max = 0

    for path, dirs, files in os.walk("all"):
            
        for f in files:

            if file_input in f:

                max = max + 1

    for path, dirs, files in os.walk("all"):
            
        for f in files:

            try:
                
                if file_input in f:
                    
                    filename = os.path.join(path, f)

                    file = open(filename, 'r', encoding = 'utf8')

                    print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

                    perc = perc + 1

                    for line in file:

                        if x in line:

                            print(Fore.RED + '[+] Found: ' + str(i))
                            print(Fore.RED + '[+] ' + Fore.GREEN + line)
                            i = i + 1
                                                
                            lv = str(line.encode('utf8', errors = 'replace')).split('/n')
                            for t in lv:
                                    
                                fout.write(t)
                                                
                                fout.write('\n')

            except:
                print('Nationality: ' + file_input + " didn't found")

    file.close()
    fout.close()
    print('File Created!')

def multipletwf():
    cond = True
    arrayofppl = []

    while cond:

        arrayofppl.append(input(Fore.GREEN + "Name:Surname: "))

        cond2 = input('Continue? [y/n]')    #[y/n], [s/n], [si/no], [yes, no] (no case sensitive)

        if((cond2.lower() == 'y') or (cond2.lower() == 's') or (cond2.lower() == 'yes') or (cond2.lower() == 'si')):
            pass

        elif((cond2.lower() == 'n') or (cond2.lower() == 'no')):
            cond = False

        else:
            print('Error, Wrong Input!')
            quit()

    file_input = input(Fore.GREEN + "Nationality: ") #we consider that the target are from the same nationality

    file_output = input("Output file: ")

    if file_output in os.listdir():
        print('Already Existing file')
        open('file.txt', 'w').close()

    else:
                         
        open(file_output, "x")
                
        fout = open(file_output, "a")

        i = 1

        perc = 1

        max = 0

        for path, dirs, files in os.walk("all"):
            
            for f in files:

                if file_input in f:

                    max = max + 1 #arriavto qui

        for path, dirs, files in os.walk("all"):
            
            for f in files:
                
                filename = os.path.join(path, f)

                file = open(filename, 'r', encoding = 'utf8')

                print(Fore.GREEN + f' [{perc}/{max}] Opening... ' + Fore.RED + str(f))

                perc = perc + 1

                for line in file:

                    for x in arrayofppl:

                        if x in line:

                            print(Fore.RED + '[+] Found: ' + str(i))
                            print(Fore.RED + '[+] ' + Fore.GREEN + line)
                            i = i + 1
                                            
                            lv = str(line.encode('utf8', errors = 'replace')).split('/n')
                            for t in lv:
                                
                                fout.write(t)
                                            
                                fout.write('\n')

        file.close()
        fout.close()
        print('File Created!')

def phonewf():
    pass

def multiplepwf():
    pass


def main():

    print('Welcome to the ultimate Mobile Number Finder!\n')

    i = 0

    for path, dirs, files in os.walk("all"):
            
        for f in files:

            i = i + 1

    
    print(Fore.GREEN + 'Number of file avaible: ' + str(i))


    print('\n' + Fore.BLUE + "1." + Fore.YELLOW + " Search for a specific number phone in the DB (Remember use the prefix, ex. 39333...)")
    print('\n' + Fore.BLUE + "2." + Fore.GREEN + " Search your target via name:surname")
    print('\n' + Fore.BLUE + "3." + Fore.GREEN + " Search multiple target at the time via name:surname")
    print('\n' + Fore.BLUE + "4." + Fore.YELLOW + " Search multiple number phone in the DB (Remember use the prefix, ex. 39333...)")
    print('\n' + Fore.BLUE + "5." + Fore.GREEN + " Search target via name:surname with Nationality")
    print('\n' + Fore.BLUE + "6." + Fore.GREEN + " Search multiple target at the time via name:surname with Nationality")
    print('\n' + Fore.BLUE + "7." + Fore.YELLOW + " Search mobile phone with Nationality")
    print('\n' + Fore.BLUE + "8." + Fore.YELLOW + " Search multiple mobile phone at the time  with Nationality")
    choice = input(Fore.RED + "\nChoose Functionality: ")

    if (choice == '1'):
        phone(i)

    elif (choice == '2'):
        target(i)

    elif (choice == '3'):
        multiplet(i)

    elif (choice == '4'):
        multiplep(i)

    elif (choice == '5'):
        targetwf()

    elif (choice == '6'):
        multipletwf()

    elif (choice == '7'):
        phonewf()

    elif (choice == '8'):
        multiplepwf()



if __name__ == '__main__':      
        main()
