from tkinter import Tk, ttk, constants
from services.mastermind import Mastermind
from ui.board_view import BoardView
from ui.create_start_view import CreateStartView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            root:
                TKinter-elementti, johon käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None


    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_start_view()
            
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()
        self._current_view = CreateStartView(self._root, self._show_board_view)
        self._current_view.pack()
    
    def _show_board_view(self):
        self._hide_current_view()
        self._current_view = BoardView(self._root, self._show_start_view)
        self._current_view.pack()       


