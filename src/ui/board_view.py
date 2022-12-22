from tkinter import ttk, Tk, constants, StringVar
import tkinter as tk
import tkinter.messagebox
from repositories.player_repository import (player_repository as default_player_repository)
from services.mastermind import Mastermind
from services.player_service import PlayerService, NameExistsError




class BoardView:
    """Pelinäkymästä vastaava näkymä."""

    def __init__(self, root, handle_click):
        """Luokan konstruktori. Luo uuden pelinäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
        """    
        self.root = root
        self.canvas =  None
        self.width = 420
        self.height = 770
        self.ball_size = 70
        self.peg_size = 35
        self.colours = ["red", "blue", "yellow", "green", "orange", "purple"]
        self.mastermind = Mastermind()
        self._handle_click = handle_click
        self.current_view = None

        self.draw_board_view()
        

    def pack(self):
        self.canvas.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.canvas.destroy()

    def draw_board_view(self):
        """"Näyttää pelinäkymän."""
        self.mastermind = Mastermind()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.create_ovals()
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
        y1 = self.height - self.ball_size
        colour = self.colours[index]
        self.mastermind.add_guess(index)
        y1 = self.mastermind.turn * self.ball_size
        y2 = (self.mastermind.turn + 1) * self.ball_size
        i = len(self.mastermind.guess)
        self.canvas.create_oval(self.ball_size*(i-1), y1, self.ball_size*(i), y2, fill=colour, outline=colour)

        if len(self.mastermind.guess) < 4:
            return
        self.canvas.unbind("<Button-1>")
        self.check()


    def check(self, event=None):
        """Luo oikeita värejä ja paikkoja kuvaavat pallot."""
        feedback = self.mastermind.compare(self.mastermind.guess, self.mastermind.code)
        self.draw_feedback(feedback)
        self.mastermind.add_turn()

        if feedback == ["black", "black", "black", "black"]:
            self.canvas.unbind("<Button-1>")    
            self.show_result(True) 

       
        if self.mastermind.turn >= 2:
            self.canvas.unbind("<Button-1>")
            self.show_result(False)
          
        self.mastermind.guess = []
        self.canvas.bind("<Button-1>", self.handle_guess)
        

    def draw_feedback(self, feedback):
        x1 =  4 * self.ball_size
        y1 = self.mastermind.turn * self.ball_size
        x2 = x1 + self.peg_size
        y2 = y1 + self.peg_size

        for colour in feedback:
            self.canvas.create_oval(x1, y1, x2, y2, fill=colour, outline=colour)
            x1 += self.peg_size
            x2 += self.peg_size


    def show_result(self, win, event=None):
        self.canvas.unbind("<Button-1>")
        if win:
            text="OIKEIN!"
        else:
            text="GAME OVER"
        message_box = tk.messagebox.showinfo(title="Mastermind", message=text)   
        self.canvas.pack()
        self.show_end()       
    

    def show_end(self):
        #TODO (tkinter.TclError: bad window path name ".!canvas2")
        self.canvas.delete(all)
        s = ShowTopPlayers(self.root, self.mastermind.turn, self._handle_click)
        s.pack()
        
    


class ShowTopPlayers:
    """Pelaajalistauksen näyttävä näkymä."""

    def __init__(self, root, turns, handle_button_click, player_repository=default_player_repository):
        """Luokan konstruktori. Luo uuden pelaajalistausnäkymän
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_button_click: Arvo,  jota kutsutaan, kun siirrytään seuraavaan näkymään
        """
        self._root = root
        self._frame = None
        self._handle_button_click = handle_button_click
        self._player_repository = player_repository
        self._name_entry = None
        self.turns = turns
        self._error_variable = None
        self._error_label = None
        self._initialize()
            
        
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
            
    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(master=self._frame, text="Nimimerkki")
        self._name_entry = ttk.Entry(master=self._frame)
        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="OK",
            command=self._handle_player
        )
        
        name_label.grid(row=0, padx=5, pady=5, sticky=constants.EW)
        self._name_entry.grid(row=0,padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(row=1, padx=5, pady=5, sticky=constants.EW)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)


    def _handle_player(self):
        name = self._name_entry.get()
        if len(name) == 0 or len(name) > 20:
            self._show_error("Nimimerkin tulee olla 1-20 merkin pituinen")

        player_service = PlayerService()
        try:
        
            player_service.create_player(name, self.turns)
        except NameExistsError:
            #TODO: error
            self._show_error("Nimimerkki on jo käytössä")

        players = player_service.top_players()
        heading_label = ttk.Label(master=self._frame, text="Top 5")  
        heading_label.grid(columnspan=2, sticky=constants.N, padx=5, pady=5)

        for player in players:
            ttk.Label(self._frame, text=player).grid()

        return_button = ttk.Button(
            master=self._frame,
            text="Palaa alkuun",
            command=self._handle_button_click
        )
        
        return_button.grid(padx=5, pady=5, sticky=constants.EW)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)


    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    

    def _hide_error(self):
        self._error_label.grid_remove()