from tkinter import Tk
from services.mastermind import Mastermind
from ui.board_view import BoardView
from ui.create_start_view import CreateStartView
from ui.ui import UI






def main():
    window = Tk()
    window.title("Mastermind")

    ui = UI(window)
    ui.start()

    window.mainloop()
 


if __name__ == "__main__":
    main()
