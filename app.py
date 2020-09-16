import tkinter as tk
import subprocess


def note():
        subprocess.call('C:\Developing\App\Jadwal\Sticky Notes.lnk', shell=True)


def window():
    Width = str(700)
    Height = str(450)

    root = tk.Tk()
    root.title("Jadwal X MIPA 4")
    window = root.resizable(False, False)
    master = tk.Canvas(root, width = Width, height = Height, bg = 'lightgrey', bd = 0, )
    master.pack()

    waktu = tk.LabelFrame(master, text = "Waktu", font = ('open sans', 10, "bold"))
    waktu.grid(column = 0, row = 1)
    lWaktu = tk.Listbox(waktu) 
    lWaktu.insert(1, '07.30 – 09.30')
    lWaktu.insert(2, '10.00 – 11.30') 
    lWaktu.insert(3, '12.30 – 14.00')
    lWaktu.insert(4, '14.00 – 14.45/15.30(Rabu)')
    lWaktu.itemconfigure(0, background="#ffcccb")
    lWaktu.itemconfigure(2, background="#ffcccb")
    lWaktu.pack()

    senin = tk.LabelFrame(master, text = "Senin", font = ('open sans', 10, "bold"))
    senin.grid(column = 1, row = 1)
    lSenin = tk.Listbox(senin) 
    lSenin.insert(1, 'Sejarah Indonesia') 
    lSenin.insert(2, 'Fisika') 
    lSenin.insert(3, 'Sosiologi')
    lSenin.itemconfigure(0, background="#d6f0ff")
    lSenin.itemconfigure(2, background="#d6f0ff")
    lSenin.pack()

    selasa = tk.LabelFrame(master, text = "Selasa", relief = "groove", font = ('open sans', 10, "bold"))
    selasa.grid(column = 2, row = 1)
    lSelasa = tk.Listbox(selasa, highlightcolor = "white") 
    lSelasa.insert(1, 'Penjasorkes') 
    lSelasa.insert(2, 'Geografi (LM)') 
    lSelasa.insert(3, 'Kimia')
    lSelasa.insert(4, 'BK/BK TIK')
    lSelasa.itemconfigure(0, background="#d6f0ff")
    lSelasa.itemconfigure(2, background="#d6f0ff")
    lSelasa.pack()

    rabu = tk.LabelFrame(master, text = "Rabu", relief = "groove", font = ('open sans', 10, "bold"))
    rabu.grid(column = 3, row = 1)
    lRabu = tk.Listbox(rabu, highlightcolor = "white") 
    lRabu.insert(1, 'Matematika Wajib') 
    lRabu.insert(2, 'Bhs. Inggris') 
    lRabu.insert(3, 'Bhs. Jawa')
    lRabu.insert(4, 'Prakarya(PKWU)')
    lRabu.itemconfigure(0, background="#d6f0ff")
    lRabu.itemconfigure(2, background="#d6f0ff")
    lRabu.pack()

    kamis = tk.LabelFrame(master, text = "Kamis", relief = "groove", font = ('open sans', 10, "bold"))
    kamis.grid(column = 4, row = 1)
    lKamis = tk.Listbox(kamis, highlightcolor = "white") 
    lKamis.insert(1, 'Matematika Minat') 
    lKamis.insert(2, 'Biologi') 
    lKamis.insert(3, 'Seni Budaya (Musik)')
    lKamis.itemconfigure(0, background="#d6f0ff")
    lKamis.itemconfigure(2, background="#d6f0ff")
    lKamis.pack()

    jumat = tk.LabelFrame(master, text = "Jum'at", relief = "groove", font = ('open sans', 10, "bold"))
    jumat.grid(column = 5, row = 1)
    lJumat = tk.Listbox(jumat, highlightcolor = "white") 
    lJumat.insert(1, 'Bhs. Indonesia') 
    lJumat.insert(2, 'PPKn') 
    lJumat.insert(3, 'Agama') 
    lJumat.itemconfigure(0, background="#d6f0ff")
    lJumat.itemconfigure(2, background="#d6f0ff")
    lJumat.pack()


    bottomNavbar = tk.Canvas(root, height = 40, width = Width)
    bottomNavbar.pack(side= "bottom")
    buttonTask = tk.Button(bottomNavbar, text = "To-Do | Note", relief = 'groove', command = note)
    buttonTask.place(relx = 0.45, rely = 0.2)

    root.mainloop()

window()