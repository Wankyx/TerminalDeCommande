#coding:utf-8 
import time 

close = False 
name = "Default"
while not close:
    userStreamInput = input("[{}]> ".format(name)) 

    if userStreamInput == "run":
        i = 0
        while i < 5:
            print(".")
            i+=1
            time.sleep(1)
    elif userStreamInput == "name":
        name = input("[{}] Enter a new name > ".format(name))
    elif userStreamInput == "help":
        print("run : print three point with a delay.")
        print("name : change a terminal name.")+
        print("help : diplay all command with a definition.")
        print("quit : quit the terminal.")
    elif userStreamInput == "quit":
        close = True 
    else:
        print("/!\ unknow command !")
