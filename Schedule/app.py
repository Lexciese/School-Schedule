import tkinter as tk
# from tkinter import ttk
from json import loads
from os import startfile
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
    startfile("Bin/Sticky Notes.lnk")


def StartRedirect():
    startfile("C:/Developing/App/Python/Automated File Mover/dist/app.exe")


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
    Size = ["700", "425"]
    jumlah = 0
    Datas = {
        "Icon": "",
        "Title": "",
        "Time": [],
        "Days": {
            "Day0": {
                "Name": "",
                "Exist": True,
                "Sub": []
            },
            "Day1": {
                "Name": "",
                "Exist": True,
                "Sub": []
            },
            "Day2": {
                "Name": "",
                "Exist": True,
                "Sub": []
            },
            "Day3": {
                "Name": "",
                "Exist": True,
                "Sub": []
            },
            "Day4": {
                "Name": "",
                "Exist": True,
                "Sub": []
            },
            "Day5": {
                "Name": "",
                "Exist": True,
                "Sub": []
            }
        }
    }
    isError = False


    def __init__(self):
        try:
            data_ = open("Data/UserData.json")
            data = loads(data_.read())

            for loop__ in range(1):
                self.Datas["Icon"] = data["Icon"]
                self.Datas["Title"] = data["Title"]
                self.Datas["Time"] = data["Time"]

                # Day0
                if data["Day0"]["Exist"] == False:
                    self.Datas["Days"]["Day0"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day0"]["Name"], self.Datas["Days"]["Day0"]["Sub"] = data["Day0"]["Name"], data["Day0"]["Sub"]

                # Day1
                if data["Day1"]["Exist"] == False:
                    self.Datas["Days"]["Day1"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day1"]["Sub"] = data["Day1"]["Sub"]
                    self.Datas["Days"]["Day1"]["Name"] = data["Day1"]["Name"]

                # Day2
                if data["Day2"]["Exist"] == False:
                    self.Datas["Days"]["Day2"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day2"]["Sub"] = data["Day2"]["Sub"]
                    self.Datas["Days"]["Day2"]["Name"] = data["Day2"]["Name"]

                # Day3
                if data["Day3"]["Exist"] == False:
                    self.Datas["Days"]["Day3"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day3"]["Sub"] = data["Day3"]["Sub"]
                    self.Datas["Days"]["Day3"]["Name"] = data["Day3"]["Name"]

                # Day4
                if data["Day4"]["Exist"] == False:
                    self.Datas["Days"]["Day4"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day4"]["Sub"] = data["Day4"]["Sub"]
                    self.Datas["Days"]["Day4"]["Name"] = data["Day4"]["Name"]

                # Day5
                if data["Day5"]["Exist"] == False:
                    self.Datas["Days"]["Day5"]["Exist"] = False
                else:
                    self.Datas["Days"]["Day5"]["Exist"] = True
                    self.Datas["Days"]["Day5"]["Sub"] = data["Day5"]["Sub"]
                    self.Datas["Days"]["Day5"]["Name"] = data["Day5"]["Name"]
                    
            data_.close()
        except:
            self.isError = True
            windowError()

    def windowApp(self):
        Width = self.Size[0]
        Height = self.Size[1]

        root = tk.Tk()
        root.title(self.Datas["Title"])
        root.iconbitmap("Bin\\Images\\{}".format(self.Datas["Icon"])) # Here's to change in-window Icon
        root.resizable(False, False)

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


        waktu = tk.LabelFrame(master, text="Time", font=('open sans', 10, "bold"))
        waktu.grid(column=0, row=1)
        lWaktu = tk.Listbox(waktu, width=30)
        i = 0
        for x in self.Datas["Time"]:
            lWaktu.insert(i, x)
            i += 1
        lWaktu.itemconfigure(0, background="#ffcccb")
        lWaktu.itemconfigure(2, background="#ffcccb")
        lWaktu.pack()


        # Senin ----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day0"]["Exist"] == False:
            pass
        else:
            senin = tk.LabelFrame(master, text= self.Datas["Days"]["Day0"]["Name"], font=('open sans', 10, "bold"))
            senin.grid(column=1, row=1)
            lSenin = tk.Listbox(senin)
            i = 0
            for x in self.Datas["Days"]["Day0"]["Sub"]:
                lSenin.insert(i, x)
                i += 1
            lSenin.itemconfigure(0, background="#d6f0ff")
            lSenin.itemconfigure(2, background="#d6f0ff")
            lSenin.pack()

        # Selasa ----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day1"]["Exist"] == False:
            pass
        else:
            selasa = tk.LabelFrame(master, text=self.Datas["Days"]["Day1"]["Name"], relief="groove", font=('open sans', 10, "bold"))
            selasa.grid(column=2, row=1)
            lSelasa = tk.Listbox(selasa, highlightcolor="white")
            i = 0
            for x in self.Datas["Days"]["Day1"]["Sub"]:
                lSelasa.insert(i, x)
                i += 1
            lSelasa.itemconfigure(0, background="#d6f0ff")
            lSelasa.itemconfigure(2, background="#d6f0ff")
            lSelasa.pack()

        # Rabu -----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day2"]["Exist"] == False:
            pass
        else:
            rabu = tk.LabelFrame(master, text=self.Datas["Days"]["Day2"]["Name"], relief="groove", font=('open sans', 10, "bold"))
            rabu.grid(column=3, row=1)
            lRabu = tk.Listbox(rabu, highlightcolor="white")
            i = 0
            for x in self.Datas["Days"]["Day2"]["Sub"]:
                lRabu.insert(i, x)
                i += 1
            lRabu.itemconfigure(0, background="#d6f0ff")
            lRabu.itemconfigure(2, background="#d6f0ff")
            lRabu.pack()

        # Kamis ----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day3"]["Exist"] == False:
            pass
        else:
            kamis = tk.LabelFrame(master, text=self.Datas["Days"]["Day3"]["Name"],
                                relief="groove", font=('open sans', 10, "bold"))
            kamis.grid(column=4, row=1)
            lKamis = tk.Listbox(kamis, highlightcolor="white")
            i = 0
            for x in self.Datas["Days"]["Day3"]["Sub"]:
                lKamis.insert(i, x)
                i += 1
            lKamis.itemconfigure(0, background="#d6f0ff")
            lKamis.itemconfigure(2, background="#d6f0ff")
            lKamis.pack()

        # Jumat ----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day4"]["Exist"] == False:
            pass
        else:
            jumat = tk.LabelFrame(master, text=self.Datas["Days"]["Day4"]["Name"], relief="groove", font=('open sans', 10, "bold"))
            jumat.grid(column=5, row=1)
            lJumat = tk.Listbox(jumat, highlightcolor="white")
            i = 0
            for x in self.Datas["Days"]["Day4"]["Sub"]:
                lJumat.insert(i, x)
                i += 1
            lJumat.itemconfigure(0, background="#d6f0ff")
            lJumat.itemconfigure(2, background="#d6f0ff")
            lJumat.pack()

        # Sabtu ----------------------------------------------------------------------------------------
        if self.Datas["Days"]["Day5"]["Exist"] == False:
            pass
        else:
            sabtu = tk.LabelFrame(master, text=self.Datas["Days"]["Day5"]["Sub"], relief="groove", font=('open sans', 10, "bold"))
            sabtu.grid(column=6, row=1)
            lSabtu = tk.Listbox(sabtu, highlightcolor="white")
            i = 0
            for x in self.Datas["Days"]["Day5"]["Sub"]:
                lSabtu.insert(i, x)
                i += 1
            lSabtu.itemconfigure(0, background="#d6f0ff")
            lSabtu.itemconfigure(2, background="#d6f0ff")
            lSabtu.pack()

        bottomNavbar = tk.Canvas(root, height=30, width=Width)
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


d = ManageData()
# d.readData()








# Execute the App ----------------------------------------------------------------------------------
if d.isError == False:
    d.windowApp()
else:
    pass
 
# import cProfile

# cProfile.run('d.windowApp()')


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
