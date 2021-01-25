import tkinter as TK

class App():
    def __init__(self, title, pokemons):
        self.app = None
        self.title = title
        self.pokemons = pokemons
        self.nbrPokemons = 0
        self.downloadEnabled = True
        
    def initFrame(self, title):
        canvas = TK.Canvas(self.app, width=1000, height=750)
        canvas.pack()
        img = TK.PhotoImage(file="./Pokemon-Images/1.png")
        canvas.create_image(0, 0, anchor='nw', image=img)
        self.app.title(title)
        self.app.wm_iconbitmap("./pokeball_logo.ico")
        self.centerApp()
        self.app.mainloop()

    def setNbrPokemons(self, num):
        self.nbrPokemons = num
        
    def start(self):
        print("All Pokemons are registered")
        self.app = TK.Tk()
        self.initFrame(self.title)

    def centerApp(self):
        windowWidth = self.app.winfo_reqwidth()
        windowHeight = self.app.winfo_reqheight()
        positionRight = int(self.app.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.app.winfo_screenheight() / 2 - windowHeight / 2)
        self.app.geometry("+{}+{}".format(positionRight, positionDown))
