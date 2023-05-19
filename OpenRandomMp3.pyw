import os, random, glob, sys, subprocess, time

Iteration = 0
CurrentDirectory = sys.path[0]

def Open_File(FilePath):
    try:
        subprocess.call([r"C:\Program Files (x86)\foobar2000\foobar2000.exe", "/add", FilePath])
    except Exception as e:
        print("ERROR : ", str(e))

def FlipCoin():
    return bool(random.getrandbits(1))

def FindValidFiles():
    files = next(os.walk(CurrentDirectory))[2]
    files = [f for f in files if f.lower().endswith(('.mp3', '.wav'))]
    print("Valid Files : " + str(len(files)))
    return files

def OpenRandom_File():
    global Iteration
    Iteration = 0
    files = FindValidFiles()
    if (len(files) > 0):
        Open_File(os.path.join(CurrentDirectory, files[random.randint(0, (len(files) - 1))]))
    else:
        print("ERROR : No More Valid Files!")

def OpenRandom_Directory():
    global Iteration, CurrentDirectory
    Iteration += 1
    print("Current Iteration : " + str(Iteration) + " - Current Directory : " + CurrentDirectory)
    Directories = next(os.walk(CurrentDirectory))[1]

    if (len(Directories) > 0) and ((len(FindValidFiles()) == 0) or FlipCoin()):
        print("Sub-Directories : " + str(len(Directories)))
        CurrentDirectory = os.path.join(CurrentDirectory, Directories[random.randint(0, (len(Directories) - 1))])
        print("Random Directory : " + str(CurrentDirectory))
        OpenRandom_Directory()
    else:
        OpenRandom_File()

if (len(sys.argv) > 1):
    Loop = int(sys.argv[1])
    print("Loop Length : " + str(Loop))

    for i in range(Loop):
        OpenRandom_Directory()
        time.sleep(0.1)
else:
    OpenRandom_Directory()
