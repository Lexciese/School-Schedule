import tkinter as tk
# from tkinter import ttk
import json
import os
from subprocess import Popen as OpenFile
# from sys import *
# from constructor import *


def windowAlert():
    Width = str(200)
    Height = str(50)

    root = tk.Tk()
    root.title("Alert")
    root.geometry('{}x{}'.format(Width, Height))
    root.iconbitmap("Bin\\Images\\warning.ico")
    root.resizable(False, False)

    Alert = tk.Label(root, text = "Reload the App\nTo Update")
    Alert.pack()

    root.mainloop()


def windowError():
    Width = str(350)
    Height = str(150)

    root = tk.Tk()
    root.title("Error")
    root.geometry('{}x{}'.format(Width, Height))
    root.iconbitmap("Bin\\Images\\warning.ico")
    root.resizable(False, False)

    Error = tk.Label(root, text = "Error's Encounter\n\nPlease Check/ Fix your 'UserData.json'\nIf you Get Confused/ Don't Know What's Wrong\nYou can validate your 'UserData.json' at \nhttps://jsonlint.com/\nJust Copy/ Paste all of the 'UserData.json' content to that site \nand you will know what's wrong")
    Error.pack()

    ChangeSubjects()


def note():
    os.startfile("Bin/Sticky Notes.lnk")


def StartRedirect():
    os.startfile("C:/Developing/App/Python/Automated File Mover/dist/app.exe")


def ChangeSubjects():
    # os.system('notepad.exe {}'.format("Data/UserData.json"))
    # os.startfile('../Data/UserData.json')
    OpenFile(["notepad.exe", "Data/UserData.json"], shell=True)
    windowAlert()



def About():
    # os.system('notepad.exe {}'.format("Data/About.txt"))
    OpenFile(["notepad.exe", "Data/About.txt"], shell=True)


def Help():
    # os.system('notepad.exe {}'.format("Data/Help.txt"))
    OpenFile(["notepad.exe", "Data/Help.txt"], shell=True)



class ManageData:
    jumlah = 0
    Title = ""
    Time = []
    Senin = []
    Selasa = []
    Rabu = []
    Kamis = []
    Jumat = []
    Sabtu = []
    Day0 = ""
    Day1 = ""
    Day2 = ""
    Day3 = ""
    Day4 = ""
    Day5 = ""
    isDay0 = True
    isDay1 = True
    isDay2 = True
    isDay3 = True
    isDay4 = True
    isDay5 = True
    Icon = ""
    isError = False


    def __init__(self):
        try:
            data_ = open("Data/UserData.json")
            data = json.loads(data_.read())

            for d in range(1):
                Icon = data["Icon"]
                self.Icon = Icon

                Title = data["Title"]
                self.Title = Title
                
                Time = data["Time"]
                self.Time = Time

                if data["Day0"]["Exist"] == False:
                    self.isDay0 = False
                else:
                    Senin = data["Day0"]["Sub"]
                    Senin_ = data["Day0"]["Name"]
                    self.Senin = Senin
                    self.Day0 = Senin_

                if data["Day1"]["Exist"] == False:
                    self.isDay1 = False
                else:
                    Selasa = data["Day1"]["Sub"]
                    Selasa_ = data["Day1"]["Name"]
                    self.Selasa = Selasa
                    self.Day1 = Selasa_

                if data["Day2"]["Exist"] == False:
                    self.isDay2 = False
                else:
                    Rabu = data["Day2"]["Sub"]
                    Rabu_ = data["Day2"]["Name"]
                    self.Rabu = Rabu
                    self.Day2 = Rabu_

                if data["Day3"]["Exist"] == False:
                    self.isDay3 = False
                else:
                    Kamis = data["Day3"]["Sub"]
                    Kamis_ = data["Day3"]["Name"]
                    self.Kamis = Kamis
                    self.Day3 = Kamis_

                if data["Day4"]["Exist"] == False:
                    self.isDay4 = False
                else:
                    Jumat = data["Day4"]["Sub"]
                    Jumat_ = data["Day4"]["Name"]
                    self.Jumat = Jumat
                    self.Day4 = Jumat_

                if data["Day5"]["Exist"] == False:
                    self.isDay5 = False
                else:
                    self.isDay5 = True
                    Sabtu = data["Day5"]["Sub"]
                    Sabtu_ = data["Day5"]["Name"]
                    self.Sabtu = Sabtu
                    self.Day5 = Sabtu_
                    
            data_.close()
        except:
            self.isError = True
            windowError()
        # print(type(data))
        # print(data)
        # print(data["app"][1]['hari'])
        


d = ManageData()

# d.readData()


def windowApp():
    Width = str(700)
    Height = str(450)

    root = tk.Tk()
    root.title(d.Title)
    root.iconbitmap("Bin\\Images\\{}".format(d.Icon)) # Here's to change in-window Icon
    root.resizable(False, False)

    # tabControl = ttk.Notebook(root) 
    # tab1 = ttk.Frame(tabControl)
    # tab2 = ttk.Frame(tabControl)

    # tabControl.add(tab1, text ='Schedule') 
    # tabControl.add(tab2, text ='Tab 2') 
    # tabControl.pack(expand = 1, fill ="both") 

    master = tk.Canvas(root, width=Width, height=Height, bg='lightgrey')
    master.pack()


    # Menu ------------------------------------------------------------
    menubar = tk.Menu(root, bg = "grey")
    filemenu = tk.Menu(menubar, tearoff=0, font=('open sans', 10))
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = tk.Menu(menubar, tearoff=0, font=('open sans', 10))
    editmenu.add_command(label="Change Subjects", command=ChangeSubjects)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=Help)
    helpmenu.add_command(label="About...", command=About)
    menubar.add_cascade(label="Help", menu=helpmenu)

    

    waktu = tk.LabelFrame(master, text="Times", font=('open sans', 10, "bold"))
    waktu.grid(column=0, row=1)
    lWaktu = tk.Listbox(waktu, width=30)
    i = 0
    for x in d.Time:
        lWaktu.insert(i, x)
        i += 1
    lWaktu.itemconfigure(0, background="#ffcccb")
    lWaktu.itemconfigure(2, background="#ffcccb")
    lWaktu.pack()

    # Senin ----------------------------------------------------------------------------------------
    if d.isDay0 == False:
        pass
    else:
        senin = tk.LabelFrame(master, text=d.Day0, font=('open sans', 10, "bold"))
        senin.grid(column=1, row=1)
        lSenin = tk.Listbox(senin)
        i = 0
        for x in d.Senin:
            lSenin.insert(i, x)
            i += 1
        lSenin.itemconfigure(0, background="#d6f0ff")
        lSenin.itemconfigure(2, background="#d6f0ff")
        lSenin.pack()

    # Selasa ----------------------------------------------------------------------------------------
    if d.isDay1 == False:
        pass
    else:
        selasa = tk.LabelFrame(master, text=d.Day1, relief="groove", font=('open sans', 10, "bold"))
        selasa.grid(column=2, row=1)
        lSelasa = tk.Listbox(selasa, highlightcolor="white")
        i = 0
        for x in d.Selasa:
            lSelasa.insert(i, x)
            i += 1
        lSelasa.itemconfigure(0, background="#d6f0ff")
        lSelasa.itemconfigure(2, background="#d6f0ff")
        lSelasa.pack()

    # Rabu -----------------------------------------------------------------------------------------
    if d.isDay2 == False:
        pass
    else:
        rabu = tk.LabelFrame(master, text=d.Day2, relief="groove", font=('open sans', 10, "bold"))
        rabu.grid(column=3, row=1)
        lRabu = tk.Listbox(rabu, highlightcolor="white")
        i = 0
        for x in d.Rabu:
            lRabu.insert(i, x)
            i += 1
        lRabu.itemconfigure(0, background="#d6f0ff")
        lRabu.itemconfigure(2, background="#d6f0ff")
        lRabu.pack()

    # Kamis ----------------------------------------------------------------------------------------
    if d.isDay3 == False:
        pass
    else:
        kamis = tk.LabelFrame(master, text=d.Day3,
                            relief="groove", font=('open sans', 10, "bold"))
        kamis.grid(column=4, row=1)
        lKamis = tk.Listbox(kamis, highlightcolor="white")
        i = 0
        for x in d.Kamis:
            lKamis.insert(i, x)
            i += 1
        lKamis.itemconfigure(0, background="#d6f0ff")
        lKamis.itemconfigure(2, background="#d6f0ff")
        lKamis.pack()

    # Jumat ----------------------------------------------------------------------------------------
    if d.isDay4 == False:
        pass
    else:
        jumat = tk.LabelFrame(master, text=d.Day4, relief="groove", font=('open sans', 10, "bold"))
        jumat.grid(column=5, row=1)
        lJumat = tk.Listbox(jumat, highlightcolor="white")
        i = 0
        for x in d.Jumat:
            lJumat.insert(i, x)
            i += 1
        lJumat.itemconfigure(0, background="#d6f0ff")
        lJumat.itemconfigure(2, background="#d6f0ff")
        lJumat.pack()

    # Sabtu ----------------------------------------------------------------------------------------
    if d.isDay5 == False:
        pass
    else:
        sabtu = tk.LabelFrame(master, text=d.Day5, relief="groove", font=('open sans', 10, "bold"))
        sabtu.grid(column=6, row=1)
        lSabtu = tk.Listbox(sabtu, highlightcolor="white")
        i = 0
        for x in d.Sabtu:
            lSabtu.insert(i, x)
            i += 1
        lSabtu.itemconfigure(0, background="#d6f0ff")
        lSabtu.itemconfigure(2, background="#d6f0ff")
        lSabtu.pack()

    bottomNavbar = tk.Canvas(root, height=20, width=Width)
    bottomNavbar.pack(side="bottom", anchor="w")

    
    # Delete Codes under this line to make compatible for various device -------------------------

    # buttonNote = tk.Button(bottomNavbar, text="To-Do | Note",
    #                        relief='groove', command=note)
    # buttonNote.pack(side="right", padx=15, pady=7)

    # buttonF = tk.Button(bottomNavbar, text="Assignment Mover",
    #                     relief='groove', command=StartRedirect)
    # buttonF.pack(side="right", padx=15)

    # ----------------------------------------------------------------------------------------------
    # ttk.Style().configure('TNotebook', tabposition='s')
    root.config(menu=menubar)
    root.mainloop()






# Execute the App ----------------------------------------------------------------------------------
if d.isError == False:
    windowApp()
else:
    pass
 


# Convert to EXE commands --------------------------------------------------------------------------
# pyinstaller --windowed --add-data "data.json;." app.py
# pyinstaller --distpath ..\Build\dist --workpath ..\Build\build app.spec








# ------------------------------- app.spec ----------------------------------------------
# -*- mode: python ; coding: utf-8 -*-

# block_cipher = None


# a = Analysis(['app.py'],
#              pathex=['C:\\Developing\\App\\Python\\Jadwal\\Schedule'],
#              binaries=[],
#              datas = [
#                  ('C:\\Developing\\App\\Python\\Jadwal\\Data\\UserData.json', 'Data'),
#                  ('C:\\Developing\\App\\Python\\Jadwal\\Data\\Help.txt', 'Data'),
#                  ('C:\\Developing\\App\\Python\\Jadwal\\Data\\About.txt', 'Images'),
#                  ('C:\\Developing\\App\\Python\\Jadwal\\Bin\\Images\\schedule-ico1.ico', 'Images')
#              ],
#              hiddenimports=[],
#              hookspath=[],
#              runtime_hooks=[],
#              excludes=[],
#              win_no_prefer_redirects=False,
#              win_private_assemblies=False,
#              cipher=block_cipher,
#              noarchive=False)
# pyz = PYZ(a.pure, a.zipped_data,
#              cipher=block_cipher)
# exe = EXE(pyz,
#           a.scripts,
#           [],
#           exclude_binaries=True,
#           name='Schedule',
#           debug=False,
#           bootloader_ignore_signals=False,
#           strip=False,
#           upx=True,
#           console=False )
# coll = COLLECT(exe,
#                a.binaries,
#                a.zipfiles,
#                a.datas,
#                strip=False,
#                upx=True,
#                upx_exclude=[],
#                name='Schedule')
