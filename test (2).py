import os, pyautogui, time

APP_FOLDER = 'C:\\Users\\MIQIU\\Desktop\\Bigolive\\Account Shortcut'

totalFiles = 0

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for Files in files:
        totalFiles += 1


for x in range(totalFiles):
    total=(x+1)
    if(total>=100):
        Stringtotal = str(total)
    elif(total>=10):
        Stringtotal = "0" + str(total)
    else:
        Stringtotal = "00" + str(total)
    os.startfile("Account Shortcut\\"+Stringtotal+".lnk")
    

    def login():
        location = pyautogui.locateCenterOnScreen('C:\\Users\\MIQIU\\\Desktop\\Bigolive\\Python\\loginbutton.png',confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.doubleClick(location)
        print(location)
        time.sleep(2)
        if(location==None):
            login()


    def google():
        location = pyautogui.locateCenterOnScreen('C:\\Users\\MIQIU\\Desktop\\Bigolive\\Python\\google3.png',confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.doubleClick(location)
        print(location)
        time.sleep(2)
        if(location==None):
            google()

    def loginaccount():
        location = pyautogui.locateCenterOnScreen('C:\\Users\\MIQIU\\Desktop\\Bigolive\\Python\\use.png',confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.doubleClick(966, 575)
        print(location)
        time.sleep(2)
        if(location==None):
            loginaccount()
        
    def close():
        time.sleep(5)
        pyautogui.moveTo(1893, 16)
        pyautogui.click(1893, 16)
        

    pyautogui.moveTo(966, 575)
    
    login()
    
    google()
    
    loginaccount()
    
    close()

