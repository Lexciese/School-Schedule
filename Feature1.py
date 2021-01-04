import os
import time
import sys


Bahasa = -6
Biologi = -7
English = -7
Fisika = -6
Geografi = -8
Jawa = -4
Kimia = -5
MTK_Peminatan = -13
MTK_Wajib = -9
PAI = -3
PJOK = -4
PPKn = -4
Pramuka = -7
Sejarah = -7
Senbud = -6
Sosiologi = -9


class Filename:
    formatF = "Falah Naufal Zaki(13)_X MIPA 4"
    src = "C:/Users/ZAKI/Google Drive/X MIPA 4/TMP/"
    dest = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/"
    ifNot = "C:/Users/ZAKI/Google Drive/X MIPA 4/If not, maybe in here/"
    Bahasa = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Bahasa/"
    Biologi = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Biologi/"
    English = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/English/"
    Fisika = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Fisika/"
    Geografi = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Geografi/"
    Jawa = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Jawa/"
    Kimia = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Kimia/"
    MTK_Peminatan = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/MTK_Peminatan/"
    MTK_Wajib = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/MTK_Wajib/"
    PAI = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/PAI/"
    PJOK = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/PJOK/"
    PPKn = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/PPKn/"
    Pramuka = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Pramuka/"
    Sejarah = "C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Sejarah/"
    Senbud ="C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Senbud/"
    Sosiologi ="C:/Users/ZAKI/Google Drive/X MIPA 4/TUGAS/Sosiologi/"


    def __init__(self):
        print("Initializing...\n")

        # Iterate all the files from src Folder
        for file in os.listdir(self.src):
            print(file)
            # To check if the file already named
            if file[:30] != self.formatF: 
                # Rename all the Files
                os.rename(self.src + file, self.src + self.formatF + ' - ' + file)

            x = 0
            y = os.listdir(self.src)[x]
            x += 1
            # print(os.listdir(self.src))

            if y[Bahasa-5:-5] == "Bahasa":
                os.replace(self.src + y, self.Bahasa + y)
                print('Redirected')
            elif y[Biologi-5:-5] == "Biologi":
                os.replace(self.src + y, self.Biologi + y)
                print('Redirected')
            elif y[English-5:-5] == "English":
                os.replace(self.src + y, self.English + y)
                print('Redirected')
            elif y[Fisika-5:-5] == "Fisika":
                os.replace(self.src + y, self.Fisika + y)
                print('Redirected')
            elif y[Geografi-5:-5] == "Geografi":
                os.replace(self.src + y, self.Geografi + y)
                print('Redirected')
            elif y[Jawa-5:-5] == "Jawa":
                os.replace(self.src + y, self.Jawa + y)
                print('Redirected')
            elif y[Kimia-5:-5] == "Kimia":
                os.replace(self.src + y, self.Kimia + y)
                print('Redirected')
            elif y[MTK_Peminatan-5:-5] == "MTK Minat":
                os.replace(self.src + y, self.MTK_Peminatan + y)
                print('Redirected')
            elif y[MTK_Wajib-5:-5] == "MTK Wajib":
                os.replace(self.src + y, self.MTK_Wajib + y)
                print('Redirected')
            elif y[PAI-5:-5] == "PAI":
                os.replace(self.src + y, self.PAI + y)
                print('Redirected')
            elif y[PJOK-5:-5] == "PJOK":
                os.replace(self.src + y, self.PJOK + y)
                print('Redirected')
            elif y[PPKn-5:-5] == "PPKn":
                os.replace(self.src + y, self.PPKn + y)
                print('Redirected')
            elif y[Pramuka-5:-5] == "Pramuka":
                os.replace(self.src + y, self.Pramuka + y)
                print('Redirected')
            elif y[Sejarah-5:-5] == "Sejarah":
                os.replace(self.src + y, self.Sejarah + y)
                print('Redirected')
            elif y[Senbud-5:-5] == "Senbud":
                os.replace(self.src + y, self.Senbud + y)
                print('Redirected')
            elif y[Sosiologi-5:-5] == "Sosiologi":
                os.replace(self.src + y, self.Sosiologi + y)
                print('Redirected')
            
            else:
                os.replace(self.src + y, self.ifNot + y)
                print("Redirected to \nC:/Users/ZAKI/Google Drive/X MIPA 4/If not, maybe in here/ folder")

def StartRedirect():
    File = os.listdir("C:/Users/ZAKI/Google Drive/X MIPA 4/TMP/")
    if len(File) == 0:
            print("-----Your TMP/ Directory is Empty-----\nTry to Put Something in It ^_^\nTry Again After You Did It!!\n")
            print("Exiting Progam in 3s")
            time.sleep(3)
            exit()
    else:
        print("Found" + len(File) + "Item/s")
        Confirm = input("Do you want to redirecting your Assignment :\nPress Y/N to Confirm - ").lower()
        if Confirm == "y":
            Filename()
        else:
            print("Good bye!!!")
            time.sleep(3)
            exit()

# StartRedirect()



# Filename()
