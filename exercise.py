import json
import os
import time
import glob
import shutil
from datetime import datetime
from random import shuffle
#cSpell:disable

# %%%%%%%%%%%%%%%%%%%%%%
#   E X E R C I S E S
# %%%%%%%%%%%%%%%%%%%%%%
version = "18-10-2023|00:00:00" #change together with dictionaries!
triceps = {
    "version" : version,
    "Flexion y rotacion"    : {"reps": 10, "level": 1, "weight": 0},
    "Flexion normal"        : {"reps": 10, "level": 1, "weight": 5},
    "Flexion abierta"       : {"reps": 10, "level": 1, "weight": 5},
    "Fondos militares"      : {"reps": 10, "level": 2, "weight": 5},
    "Flexion explosiva"     : {"reps": 10, "level": 2, "weight": 0},
    "Flexion en diamante"   : {"reps": 10, "level": 2, "weight": 5},
    "Fondo paralelas"       : {"reps": 9, "level": 3, "weight": 0},
    "Extension con pesa"    : {"reps": 10, "level": 1, "weight": 8},
    "Flexiones en pica"     : {"reps": 10, "level": 2, "weight": 0}
}

biceps = {
    "version" : version,
    "Chin-ups"              : {"reps": 9, "level": 3, "weight": 0},
    "Curl 2x palma abajo"   : {"reps": 10, "level": 1, "weight": 12},
    "Curl palma arriba"     : {"reps": 10, "level": 1, "weight": 8},
    "Curl martillo"         : {"reps": 10, "level": 1, "weight": 8}
}

hombro = {
    "version" : version,
    "Elevacion lateral"     : {"reps": 10, "level": 1, "weight": 5},
    "Elevacion frontal"     : {"reps": 10, "level": 1, "weight": 5},
    "Press (arriba)"        : {"reps": 10, "level": 1, "weight": 6.5},
    "Rear delt. flies"      : {"reps": 10, "level": 1, "weight": 5}
}

espalda = {
    "version" : version,
    "Pull-ups"              : {"reps": 6, "level": 3, "weight": 0},
    "Body row"              : {"reps": 10, "level": 2, "weight": 0},
    "Swimmer"               : {"reps": 10, "level": 1, "weight": 1},
    "Wall-angel"            : {"reps": 10, "level": 1, "weight": 0},
    "Front lever raise"     : {"reps": 6, "level": 3, "weight": 0}
}

abdominales = {
    "version" : version,
    "Hollow body crunch"    : {"reps": 8, "level": 1, "weight": 0},
    "Plank"                 : {"time": 90, "level": 1, "weight": 8},
    "Corkscrew"             : {"reps": 10, "level": 2, "weight": 0},
    "Upper circle crunch"   : {"reps": 10, "level": 2, "weight": 0},
    "V sit"                 : {"reps": 10, "level": 2, "weight": 0}
}

piernas = {
    "version" : version,
    "Escaleras"             : {"reps": 5, "level": 1, "weight": 10},
    "Calf raises"           : {"reps": 10, "level": 1, "weight": 16},
    "Sit-up to high jump"   : {"reps": 10, "level": 2, "weight": 0},
    "Wall sit"              : {"time": 120, "level": 1, "weight": 0},
    "Inverse leg curl"      : {"reps": 10, "level": 2, "weight": 0}
}

flexibilidad = {
    "version" : version,
    "Hip flexor stretch"    : {"time": 30, "level": 1, "weight": 0},
    "Elephant walks"        : {"time": 30, "level": 2, "weight": 0},
    "Pancake stretch"       : {"time": 30, "level": 3, "weight": 0},
    "Figure 4 stretch"      : {"time": 30, "level": 1, "weight": 0},
    "Lat. stretch"          : {"time": 30, "level": 1, "weight": 0},
    "Side stretch"          : {"time": 30, "level": 1, "weight": 0},
    "Splits"                : {"time": 30, "level": 3, "weight": 0}
}
Ejercicios_dict = {"triceps": triceps, "biceps": biceps, "hombro": hombro, "espalda": espalda, "abdominales": abdominales, "piernas": piernas, "flexibilidad": flexibilidad}

# %%%%%%%%%%%%%%%%%%%%%%
#   F U N C T I O N S
# %%%%%%%%%%%%%%%%%%%%%%
def getNow():
    now = datetime.now()
    hh = str(now.hour)
    mm = str(now.minute)
    ss = str(now.second)
    if (len(hh) == 1):
        hh = "0"+hh
    if (len(mm) == 1):
        mm = "0"+mm
    if (len(ss) == 1):
        ss = "0"+ss
    nowString = str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"|"+hh+":"+mm+":"+ss
    return nowString

def reset (dictionary):
    files = glob.glob("data/*.json")
    for file in files:
        destroyFile(file.replace(".json","").removeprefix("data\\"),False)
    for name, dict_ in dictionary.items():
        path = "data/"+name+".json"
        with open(path, "w") as outfile: 
            json.dump(dict_, outfile, indent = 4)

def printHelp():
    print("[LIST]: Shows all files in 'data' or all the currently loaded files.")
    print("[LOAD]: Creates a copy of a file in 'data' ready to be modified or read.")
    print("[UNLOAD]: Deletes a loaded file without saving it in the 'data' folder.")
    print("[READ]: Shows all contents of a loaded file.")
    print("[GIVE]: Selects a number of exercises from a loaded file in a randomized order.")
    print("[ADD]: Includes/updates an exercise in a loaded file.")
    print("[REMOVE]: Eliminates an existing exercise from a loaded file.")
    print("[CREATE]: Creates a new file in the 'data' folder and then loads it.")
    print("[DESTROY]: Deletes an existing file from the 'data' folder.")
    print("[SAVE]: Saves a loaded file to the 'data' folder and then unloads it.")
    print("[RESET]: Replaces ALL the files in 'data' with a default version and clears ALL loaded files.")
    print("[CLEAR]: Clears the screen.")
    print("[EXIT]: Program goes bye bye.")

def unload(jsonFileName):
    path1 = jsonFileName+".json"
    if os.path.exists(path1):
        os.remove(path1)
        print("'",jsonFileName,"' has been unloaded.",sep="")
    else:
        print("Sorry, the file does not exist or it's not currently loaded.") 

def unloadAll():
    files = glob.glob("*.json")
    if len(files) != 0:
        for file in files:
            unload(file.replace(".json",""))

def load(jsonFileName):
    src = "data/"+jsonFileName+".json"
    dst = jsonFileName+".json"
    try:
        shutil.copyfile(src, dst)
        print("'",jsonFileName,"' has been loaded.",sep="")
    except:
        print("Sorry, the file does not exist.")

def loadAll():
    files = glob.glob("data/*.json")
    for file in files:
        load(file.replace(".json","").removeprefix("data\\"))

def readFile(jsonFileName):
    path = jsonFileName+".json"
    try:
        with open(path, "r") as file: 
            data = json.load(file)
        return data
    except:
        print("Sorry, the file does not exist or it's not currently loaded.") 
        return -1
    
def readDict(dictionary):
    for key, value in dictionary.items():
        if(key=="version"):
            print("<% VERSION:",value,"%>")
            continue
        print(f"·{key}:",end="  ->  ")
        for key2, value2 in value.items():  
            print(f"{key2}: {value2}",end="  ")
        print()

def checkAddition(list):
    if (len(list)!=7):
        print("Check the amount of parameters provided.")
        return False
    if (list[1] != "r" and list[1] != "t"):
        print("Only 'r' or 't' allowed.")
        return False
    try:
        if (int(list[2]) < 1):
            print("Please, select a number of repetitions/time above 0.")
            return False
    except:
        print("Only numbers allowed for repetitions/time.")
        return False
    if (list[3] != "l"):
        print("Only 'l' allowed.")
        return False
    if (list[5] != "w"):
        print("Only 'w' allowed.")
        return False
    if (list[4] != "1" and list[4] != "2" and list[4] != "3"):
        print("Only three numbers (1, 2 or 3) are allowed for the exercise level.")
        return False
    try:
        if (int(list[6])<0):
            print("Please, select a positive number (or 0) for weight.")
            return False
    except:
        print("Only numbers allowed for weight.")
        return False
    return True

def addExercise(ex,dict,name):
    repOrTime = ex[1]
    if (repOrTime=="r"):
        repOrTime = "reps"
    elif (repOrTime=="t"):
        repOrTime = "time"
    exercise = {ex[0]: {repOrTime:ex[2],"level":ex[4],"weight":ex[6]}}
    dict.update(exercise)
    dict.update({"version": getNow()}) #just in case they added "version" we replace it later
    path = name+".json"
    with open(path, "w") as outfile: 
        json.dump(dict, outfile, indent = 4)

def removeExercise(ex,dict,name):
    del data[ex]
    newDict = {"version": getNow()} #if version still existed, this line will be replaced 
    newDict.update(dict) #just in case they deleted "version", this will keep it on top
    newDict.update({"version": getNow()}) #if version wasn't deleted, this line will refresh it again
    path = name+".json"
    with open(path, "w") as outfile: 
        json.dump(newDict, outfile, indent = 4)

def checkAnyLoaded():
    if len(glob.glob("*.json")) != 0:
        return True
    else:
        return False
    
def saveFile(data,filename):
    path = "data/"+filename+".json"
    with open(path, "w") as outfile: 
        json.dump(data, outfile, indent = 4)
    print("File '",filename,"' has been saved!",sep="")
    unload(filename)
    
def saveAll():
    files = glob.glob("*.json")
    if len(files) != 0:
        for file in files:
           file = file.replace(".json","")
           data = readFile(file)
           saveFile(data,file)
        print("All files correctly saved!")
        unloadAll()
    else:
        print("There are not any loaded files to save.")
    
def destroyFile(filename,verbose):
    path1 = "data/"+filename+".json"
    if os.path.exists(path1):
        os.remove(path1)
        if(verbose):
            print("'",filename,"' has been deleted.",sep="")
    else:
        print("Sorry, that file does not exist.")

def createFile(filename):
    path = "data/"+filename+".json"
    data = {"version" : getNow()}
    with open(path, "w") as outfile: 
        json.dump(data, outfile, indent = 4)
    print('File created!')
    load(filename)

def getExercises(dictionary,number):
    Exercises = {}
    keys = list(dictionary.keys())
    keys.remove("version")
    shuffle(keys)
    keys = keys[:number]
    for key in keys:
        Exercises.update({key: "NULL"})
    for key, value in dictionary.items():
        if key in keys:
            Exercises.update({key: value})
    readDict(Exercises)

# %%%%%%%%%%%%%%%%%%%%%%
#        M A I N
# %%%%%%%%%%%%%%%%%%%%%%
versoft = "27/09/2024" #software last updated
print("@=",53*"-=","@\n| YOU'RE USING 'exercise.py'. THIS PROGRAM WAS WRITTEN BY VÍCTOR M. AS AN EXERCISE ORGANIZER FOR THE GYM.   |\n| Software last updated: ",versoft,".",72*" ","|\n@=",53*"-=","@",sep="")
c = True
if not os.path.exists("data/"):
    os.makedirs("data/")
    print("\n%_",62*"/\\","_%\n| HEY! This is your first time, right? Some files have been added in the newly-created 'data' folder to speed up the process.  |\n| Those files will be replaced EACH TIME you use the [RESET] command. Hope you like this little program and find it helpful!   |\n%\u203e",62*"\\/","\u203e%",sep="")
    reset(Ejercicios_dict)
while (c):
    string = "\n"+61*"##"+"\nSelect your command: [LIST] [LOAD] [UNLOAD] [READ] [GIVE] [ADD] [REMOVE] [CREATE] [DESTROY] [SAVE] [RESET] [CLEAR] [EXIT]\nType '?' if you don't know what the commands do!\n"+61*"##"+"\n> "
    comm = input(string)
    comm = comm.casefold()
    if comm == "list":
        opt = input("Which files would you like to list? [ALL] [LOADED]\n> ")
        opt = opt.casefold()
        if opt == "all":
            print("These are all the muscular groups available in 'data':")
            files = glob.glob("data/*.json")
            for file in files:
                print(file.replace(".json","").removeprefix("data\\"))
        if opt == "loaded":
            files = glob.glob("*.json")
            if len(files) == 0:
                print("There are 0 files loaded.")
            else:
                if len(files) == 1:
                    print("There is",len(files),"muscular group loaded:")
                else:
                    print("There are",len(files),"muscular groups loaded:")
                for file in files:
                    print(file.replace(".json","")) 
    elif comm == "load":
        file = input("Specify the file you'd like to load: [ALL] [NAME]\n> ")
        if (file.casefold()=="all"):
            loadAll()
        else:
            load(file)
    elif comm == "unload":
        file = input("Specify the file you'd like to unload: [ALL] [NAME]\n> ")
        if(file.casefold()=="all"):
            unloadAll()
        else:
            unload(file)
    elif comm == "read":
        file = input("Specify the loaded file you'd like to read: [NAME]\n> ")
        data = readFile(file)
        if (data != -1):
            readDict(data)
    elif comm == "give":
        file = input("Select the loaded file from which you will get randomized exercises: [NAME]\n> ")
        data = readFile(file)
        if (data != -1):
            number = input("How many exercises would you like? [NUMBER]\n> ")
            try:
                num = int(number)
                if (num > 0):
                    dictLen = len(data) - 1
                    if num > dictLen:
                        print("This file doesn't have that many exercises; instead, these are all of them shuffled:")
                        num = dictLen
                    else:
                        print("These are your ",num," exercises:",sep="")
                    getExercises(data,num)
                else:
                    print("Please, introduce a number greater than 0.")
            except:
                print("Please, introduce a number greater than 0.")   
    elif comm == "add":
        file = input("Specify the loaded file you'd like to modify: [NAME]\n> ")
        data = readFile(file)
        if (data != -1):
            addition = input("Describe the exercise you want as: '[NAME], r/t, [REPS/TIME], l, [LEVEL(1-3)], w, [WEIGHT]'\nEXAMPLE -> Flexion, r, 10, l, 1, w, 0\n> ")
            additionList = addition.split(", ")
            if (checkAddition(additionList)):
                print("Do you want to add/update '",addition,"' to file '",file,"'? [YES] [NO]",sep="")
                opt = input("> ")
                if (opt.casefold() == "yes"):
                    addExercise(additionList,data,file)
                    print("Exercise added/updated!")
                elif (opt.casefold() == "no"):
                    print("The exercise was not added/updated.")
                else:
                    print("Action aborted.")
    elif comm == "remove":
        file = input("Specify the loaded file you'd like to modify: [NAME]\n> ")
        data = readFile(file)
        if (data != -1):
            print("Name the exercise you want to remove from the file '",file,"':",sep="")
            readDict(data)
            removal = input("> ")
            if removal in data:
                print("Are you sure you want to delete exercise '",removal,"'? [YES] [NO]",sep="")
                opt = input("> ")
                if (opt.casefold() == "yes"):
                    removeExercise(removal,data,file)
                    print("Exercise removed!")
                elif (opt.casefold() == "no"):
                    print("The exercise was not removed.")
                else:
                    print("Action aborted.")
            else:
                print("Exercise not found.")
    elif comm == "save":
        file = input("Which file would you like to save? [ALL] [NAME]\n> ")
        if file.casefold() == "all":
            saveAll()
        else:
            data = readFile(file)
            if (data != -1):
                saveFile(data,file)
    elif comm == "create":
        conf = "no"
        while conf=="no":
            file = input("Please, write how the file shall be named.\n> ")
            if not file:
                print("Action aborted.")
                break
            string = "Is '"+file+"' correct? Write anything else to cancel the operation [YES] [NO] [-]\n> "
            conf = input(string)
            conf = conf.casefold()
        if conf == "yes":
            createFile(file)
        if conf != "no" and conf != "yes":
            print("Action aborted.")
    elif comm == "destroy":
        print(5*"#%"," W A R N I N G ",5*"%#")
        print("This option will COMPLETELY REMOVE one file from the 'data' folder, this action is IRREVERSIBLE.")
        file = input("Which file would you like to permanently erase? [NAME]\n> ")
        destroyFile(file,True)
    elif comm == "reset":
        print(5*"#%"," W A R N I N G ",5*"%#")
        string = "This option will COMPLETELY REMOVE all existing files and replace them with the ["+version+"] version, this action is IRREVERSIBLE.\nAre you sure you want to proceed? [YES] [NO]\n> "
        conf = input(string)
        conf = conf.casefold()
        if conf == "yes":
            reset(Ejercicios_dict)
            unloadAll()
            print("All files reset.")
        elif conf == "no":
            print("Files unchanged.")
        else:
            print("Action aborted.")
    elif comm == "clear":
        os.system('cls')
    elif comm == "?":
        printHelp()
    elif comm == "secret":
        print("Oh, you read the code, didn't you... Well, hellooo!") #How are you doing?
    elif comm == "exit":
        if(checkAnyLoaded()):
            conf = input("There are loaded files. Do you want to save all changes? [YES] [-]\n> ")
            conf = conf.casefold()
            if (conf == "yes"):
                saveAll()
            else:
                print("OK!")
                unloadAll()
        print("See you soon",end="",flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.6)
        c = False