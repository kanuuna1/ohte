from tkinter import ttk, constants
from repositories.player_repository import (player_repository as default_player_repository)
from services.mastermind import Mastermind

class EndView:
    """Pelin lopputilanteesta vastaava näkymä."""

    def __init__(self, root, win, handle_button_click, player_repository=default_player_repository):
        """Luokan konstruktori. Luo uuden loppunäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            player_repository:
                Vapaaehtoinen, oletusarvoltaan PlayerRepository-olio.
        """
        self._root = root
        self._frame = None
        self._handle_button_click = handle_button_click
        self.win = win
        self._player_repository = player_repository
        self._name_entry = None
        self._player_list_view = None
        self._player_list_frame = None
        self._initialize()
        
    
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
       
    
        
    def _initialize(self):    
        self._frame = ttk.Frame(master=self._root)
        #self._player_list_frame = ttk.Frame(master=self._frame) 
        
        
    
        name_label = ttk.Label(master=self._frame, text="Nimimerkki")
        self._name_entry = ttk.Entry(master=self._frame)

        create_user_button = ttk.Button(
            master=self._frame,
            text="OK",
            command=self._handle_player
        )
        
        name_label.grid(row=0, padx=5, pady=5, sticky=constants.W)
        self._name_entry.grid(row=0,padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(row=1, padx=5, pady=5, sticky=constants.EW)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)


    def _handle_player(self):
        if self._player_list_view:
            self._player_list_view.destroy()
        name = self._name_entry.get()
        #TODO: ERROR jos epäsopiva
        

        self._player_repository.create(name)
        
        players = self._player_repository.find_best()
        #self.destroy()
        #self._player_list_frame.grid()

        
        #self._player_list_view = ShowPlayerList(self._player_list_frame, players, self._handle_button_click)
        #self._player_list_view.pack()
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
    



class ShowPlayerList:
    """Pelaajalistauksen näyttävä näkymä."""

    def __init__(self, root, player_list, handle_button_click):
        """Luokan konstruktori. Luo uuden pelaajalistausnäkymän
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            player_list:
                lista, jonka tiedot olio näyttää

        """
        self._root = root
        self._frame = None
        self._player_list = player_list
        self._name_entry = None
        self._handle_button_click = handle_button_click
        self._initialize()
            
        
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
            
    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Top 5")  
        heading_label.grid(columnspan=2, sticky=constants.N, padx=5, pady=5)

        for player in self._player_list:
            ttk.Label(self._frame, text=player).grid()

        return_button = ttk.Button(
            master=self._frame,
            text="Palaa alkuun",
            command=self._handle_button_click
        )
        
        return_button.grid(padx=5, pady=5, sticky=constants.EW)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)
    