from tkinter import ttk, Tk, constants

class EndView:
    """Pelin lopputilanteesta vastaava näkymä."""

    def __init__(self, root, handle_button_click, win):
        """Luokan konstruktori. Luo uuden loppunäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
        """
        self._root = root
        self._frame = None
        self._handle_button_click = handle_button_click
        self._current_view = None
        self.win = win
        self._initialize()
        
    
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
        
    def _initialize(self):
        self._hide_current_view()
        self._frame = ttk.Frame(master=self._root)

        if self.win:
            label_text = "Voitit!"
        else:
            label_text = "Game over"

        heading_label = ttk.Label(master=self._frame, text=label_text)  
        button = ttk.Button(master=self._frame, text="Aloita uusi peli", command=self._handle_button_click)   
        heading_label.grid(columnspan=2, sticky=constants.N, padx=5, pady=5)
        button.grid(columnspan=2, padx=5, pady=5)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)


        
   