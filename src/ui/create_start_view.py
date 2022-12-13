from tkinter import ttk, constants

class CreateStartView:
    """Aloitusnäkymästä vastaava näkymä."""

    def __init__(self, root, handle_button_click):
        """Luokan konstruktori. Luo uuden pelinäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
        """   
        self._root = root
        self._frame = None
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
        heading_label = ttk.Label(master=self._frame, text="Tervetuloa!")
        label = ttk.Label(master=self._frame, text="Tähän tulee peliohjeet")
        button = ttk.Button(master=self._frame, text="Aloita peli", command=self._handle_button_click)
        
       
        heading_label.grid(columnspan=2, sticky=constants.N, padx=5, pady=5)
        label.grid(sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, padx=5, pady=5)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)
    
   