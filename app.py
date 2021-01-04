import tkinter as tk
import json
# from sys import *
import os
# from constructor import *
import json


class ManageData:
    jumlah = 0
    Waktu = []
    Senin = []
    Selasa = []
    Rabu = []
    Kamis = []
    Jumat = []
    Sabtu = ["Tidak Ada"]

    def __init__(self):
        data_ = open("data.json")
        data = json.loads(data_.read())
        # print(type(data))
        # print(data)
        # print(data["app"][1]['hari'])
        for d in range(1):
            Waktu = data["Waktu"]
            self.Waktu = Waktu
            Senin = data["Senin"]
            self.Senin = Senin
            Selasa = data["Selasa"]
            self.Selasa = Selasa
            Rabu = data["Rabu"]
            self.Rabu = Rabu
            Kamis = data["Kamis"]
            self.Kamis = Kamis
            Jumat = data["Jumat"]
            self.Jumat = Jumat
            if data["Sabtu"]["ada"] == True:
                Sabtu = data["Sabtu"]['isi']
                self.Sabtu = Sabtu
            else:
                pass
        data_.close()
        # print(self.Senin)
        # print(self.Selasa)
        # return Senin, Selasa, Rabu, Kamis, Jumat

    # def insertData(self, x):
    #     insert = {
    #         "hari": x,
    #     }
    #     data_ = open("data.json")
    #     data = json.loads(data_.write())
    #     data.append(insert)
    #     data_.seek(0)
    #     json.dumps(data, data_)
    #     data_.close()

    # def readData(self):
    #     data_ = open("data.json")
    #     data = json.loads(data_.read())
    #     # print(type(data))
    #     # print(data)
    #     # print(data["app"][1]['hari'])
    #     for d in range(1):
    #         Senin = data["Senin"]
    #         self.Senin = Senin
    #         Selasa = data["Selasa"]
    #         self.Selasa = Selasa
    #         Rabu = data["Rabu"]
    #         self.Rabu = Rabu
    #         Kamis = data["Kamis"]
    #         self.Kamis = Kamis
    #         Jumat = data["Jumat"]
    #         self.Jumat = Jumat
    #         if data["Sabtu"]["ada"] == True:
    #             Sabtu = data["Sabtu"]['isi']
    #             self.Sabtu = Sabtu
    #         else:
    #             pass
    #     data_.close()
    #     print(self.Senin)
    #     print(self.Selasa)
    #     return Senin, Selasa, Rabu, Kamis, Jumat


# d = ManageData()
# print(d.Jumat)
d = ManageData()
# d.readData()
# print(d.Senin)


def note():
    os.startfile("C:/Developing/App/Python/Jadwal/Sticky Notes.lnk")


def StartRedirect():
    os.startfile("C:/Developing/App/Python/Automated File Mover/dist/app.exe")




def window():

    Width = str(700)
    Height = str(450)

    root = tk.Tk()
    root.title("Jadwal X MIPA 4")
    window = root.resizable(False, False)
    master = tk.Canvas(root, width=Width, height=Height, bg='lightgrey')
    master.pack()

    waktu = tk.LabelFrame(master, text="Waktu", font=('open sans', 10, "bold"))
    waktu.grid(column=0, row=1)
    lWaktu = tk.Listbox(waktu, width=30)
    i = 0
    for x in d.Waktu:
        lWaktu.insert(i, x)
        i += 1
    # lWaktu.insert(1, '07.30 – 09.30')
    # lWaktu.insert(2, '10.00 – 11.30')
    # lWaktu.insert(3, '12.30 – 14.00')
    # lWaktu.insert(4, '14.00 – 14.45/15.30(Rabu)')
    lWaktu.itemconfigure(0, background="#ffcccb")
    lWaktu.itemconfigure(2, background="#ffcccb")
    lWaktu.pack()

    senin = tk.LabelFrame(master, text="Senin", font=('open sans', 10, "bold"))
    senin.grid(column=1, row=1)
    lSenin = tk.Listbox(senin)
    i = 0
    for x in d.Senin:
        lSenin.insert(i, x)
        i += 1
    # lSenin.insert(1, 'Sejarah Indonesia')
    # lSenin.insert(2, 'Fisika')
    # lSenin.insert(3, 'Sosiologi')

    lSenin.itemconfigure(0, background="#d6f0ff")
    lSenin.itemconfigure(2, background="#d6f0ff")
    lSenin.pack()

    selasa = tk.LabelFrame(master, text="Selasa", relief="groove", font=('open sans', 10, "bold"))
    selasa.grid(column=2, row=1)
    lSelasa = tk.Listbox(selasa, highlightcolor="white")
    i = 0
    for x in d.Selasa:
        lSelasa.insert(i, x)
        i += 1
    # lSelasa.insert(1, 'Penjasorkes')
    # lSelasa.insert(2, 'Geografi (LM)')
    # lSelasa.insert(3, 'Kimia')
    # lSelasa.insert(4, 'BK/BK TIK')
    lSelasa.itemconfigure(0, background="#d6f0ff")
    lSelasa.itemconfigure(2, background="#d6f0ff")
    lSelasa.pack()

    rabu = tk.LabelFrame(master, text="Rabu", relief="groove",
                         font=('open sans', 10, "bold"))
    rabu.grid(column=3, row=1)
    lRabu = tk.Listbox(rabu, highlightcolor="white")
    i = 0
    for x in d.Rabu:
        lRabu.insert(i, x)
        i += 1
    # lRabu.insert(1, 'Matematika Wajib')
    # lRabu.insert(2, 'Bhs. Inggris')
    # lRabu.insert(3, 'Bhs. Jawa')
    # lRabu.insert(4, 'Prakarya(PKWU)')
    lRabu.itemconfigure(0, background="#d6f0ff")
    lRabu.itemconfigure(2, background="#d6f0ff")
    lRabu.pack()

    kamis = tk.LabelFrame(master, text="Kamis",
                          relief="groove", font=('open sans', 10, "bold"))
    kamis.grid(column=4, row=1)
    lKamis = tk.Listbox(kamis, highlightcolor="white")
    i = 0
    for x in d.Kamis:
        lKamis.insert(i, x)
        i += 1
    # lKamis.insert(1, 'Matematika Minat')
    # lKamis.insert(2, 'Biologi')
    # lKamis.insert(3, 'Seni Budaya (Musik)')
    lKamis.itemconfigure(0, background="#d6f0ff")
    lKamis.itemconfigure(2, background="#d6f0ff")
    lKamis.pack()

    jumat = tk.LabelFrame(master, text="Jum'at",
                          relief="groove", font=('open sans', 10, "bold"))
    jumat.grid(column=5, row=1)
    lJumat = tk.Listbox(jumat, highlightcolor="white")
    i = 0
    for x in d.Jumat:
        lJumat.insert(i, x)
        i += 1
    # lJumat.insert(1, 'Bhs. Indonesia')
    # lJumat.insert(2, 'PPKn')
    # lJumat.insert(3, 'Agama')
    lJumat.itemconfigure(0, background="#d6f0ff")
    lJumat.itemconfigure(2, background="#d6f0ff")
    lJumat.pack()

    bottomNavbar = tk.Canvas(root, height=40, width=Width)
    bottomNavbar.pack(side="bottom", anchor="w")
    
    # def update():
    #     root.destroy()
    #     os.system('app.py')

    # buttonReload = tk.Button(bottomNavbar, text="Reload",
    #                        relief='groove', command=update)
    # buttonReload.pack(side="left", padx=10, pady=7)

    buttonNote = tk.Button(bottomNavbar, text="To-Do | Note",
                           relief='groove', command=note)
    buttonNote.pack(side="right", padx=15, pady=7)

    buttonF = tk.Button(bottomNavbar, text="Assignment Mover",
                           relief='groove', command=StartRedirect)
    buttonF.pack(side="right", padx=15)

    root.mainloop()


window()
# pyinstaller -F --windowed --add-data "data.json;." app.py