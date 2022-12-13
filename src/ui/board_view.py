from tkinter import ttk, Tk, constants
import tkinter as tk
from services.mastermind import Mastermind
from ui.end_view import EndView



class BoardView:
    """Pelinäkymästä vastaava näkymä."""

    def __init__(self, root, handle_click):
        """Luokan konstruktori. Luo uuden pelinäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
        """    
        self.root = root
        self.canvas =  tk.Canvas(root)
        self.width = 420
        self.height = 770
        self.ball_size = 70
        self.peg_size = 35
        self.status = tk.Label(root)
        self.colours = ["red", "blue", "yellow", "green", "orange", "purple"]
        self.turn = 0
        self.mastermind = Mastermind()
        self._handle_click = handle_click
    
        self.draw_board_view()
        

    def pack(self):
        self.canvas.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.canvas.destroy()
        self.status.destroy()

    def draw_board_view(self):
        """"Näyttää pelinäkymän."""
        self.destroy()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.create_ovals()
        self.status = tk.Label(self.root)
        self.status.pack()
        self.canvas.bind("<Button-1>", self.handle_guess)
        

    def create_ovals(self):
        """"Luo värivaihtoehtoja kuvaavat pallot."""
        y1 = self.height-self.ball_size
        for i in range(6):
            colour = self.colours[i]
            self.canvas.create_oval(i*self.ball_size, y1, (i+1)*self.ball_size, self.height, fill=colour, outline=colour)
        
    def handle_guess(self, event=None):
        """"Luo pelaajan arvausta kuvaavat pallot."""
        index = self.canvas.find_withtag("current")[0] - 1
        y1 = self.height-self.ball_size
        colour = self.colours[index]
        self.mastermind.add_guess(index)
        y1 = self.turn * self.ball_size
        y2 = (self.turn + 1) * self.ball_size
        i = len(self.mastermind.guess)
        self.canvas.create_oval(self.ball_size*(i-1), y1, self.ball_size*(i), y2, fill=colour, outline=colour)
        

        if len(self.mastermind.guess) >= 4:
            #self.canvas.unbind("<Button-1>")
            # miten seuraavaan näkymään?
            self.canvas.bind("<Button-1>", self.check)
           
       
    def check(self, event=None):
        """Luo oikeita värejä ja paikkoja kuvaavat pallot."""
        feedback = self.mastermind.compare(self.mastermind.guess, self.mastermind.code)
        self.draw_feedback(feedback)
        self.turn += 1
        #print(f"vuoro {self.turn}")
        if self.turn >= 2:
            # TODO: game over -näkymä ja näytä oikea rivi
            # miten seuraavaan näkymään?
            print("GAME OVER") 
            self.status.config(text="game over")
            self.canvas.unbind("<Button-1>")
            self.status.pack()
            #self.draw_end(False)
            self.show_end(False)
        if feedback == ["black", "black", "black", "black"]:
            # miten seuraavaan näkymään?
            print("You won")
            self.status.config(text="You won!")
            self.canvas.unbind("<Button-1>")
            self.status.pack()
            self.show_end(True)
            #self.draw_end(True)
        
        self.mastermind.guess = []
        self.canvas.bind("<Button-1>", self.handle_guess)
        

    def draw_feedback(self, feedback):
        x1 =  4* self.ball_size
        y1 = self.turn * self.ball_size
        x2 = x1 + self.peg_size
        y2 = y1 + self.peg_size

        for colour in feedback:
            self.canvas.create_oval(x1, y1, x2, y2, fill=colour, outline=colour)
            x1 += self.peg_size
            x2 += self.peg_size

    def show_end(self, win, event=None):

        #self.status.config(text="game over")
        #self.status.pack()
        print("loppu")
        if win:
            label_text = "Oikein!"
        else:
            label_text = "Game over"
        label = tk.Label(self.canvas,text=label_text, fg="white", bg="black")
        label.pack()
        self.canvas.pack()
        """ self._frame = ttk.Frame(master=self._root)

        if win:
            label_text = "Oikein!"
        else:
            label_text = "Game over"

        heading_label = ttk.Label(master=self.canvas, text=label_text)  
        button = ttk.Button(master=self._frame, text="Aloita uusi peli", command=self._handle_click)   
        heading_label.grid(columnspan=2, sticky=constants.N, padx=5, pady=5)
        button.grid(columnspan=2, padx=5, pady=5)
        self._root.grid_columnconfigure(1, weight=1, minsize=300) """
    
    def draw_end(self, win):
        self.destroy()
        e = EndView(self.root, self._handle_click, win)
        e.pack()
        