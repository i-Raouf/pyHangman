from tkinter import *
from tkinter import ttk,font

class Hangman_ui(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("pyHangman")
        self.master.resizable(False, False)

        livesLabel = Label(text="Lives: 7",anchor="e",font=font.Font(size=14))
        livesLabel.pack(fill=X, padx=10)

        frame = Frame()
        frame.pack(fill=X, padx=10,expand=1)

        canvas = Canvas(frame,width=220, height=220)
        WIDTH=3
        # 0
        canvas.create_line(10, 200, 210, 200, width=WIDTH)
        canvas.create_line(45, 200, 45, 10, width=WIDTH)
        canvas.create_line(45, 10, 145, 10, width=WIDTH)
        canvas.create_line(45, 60, 95, 10, width=WIDTH)

        # 1
        canvas.create_line(145, 10, 145, 40, width=WIDTH)
        # 2
        canvas.create_oval(145-23, 40, 145+23, 40+46, width=WIDTH)
        # 3
        canvas.create_line(145, 86, 145, 131, width=WIDTH)
        # 4
        canvas.create_line(145, 131, 112, 164, width=WIDTH)
        # 5
        canvas.create_line(145, 131, 178, 164, width=WIDTH)
        # 6
        canvas.create_line(145, 104, 115, 104, width=WIDTH)
        # 7
        canvas.create_line(145, 104, 175, 104, width=WIDTH)

        canvas.pack(side="left",padx=10)

        wordLabel = Label(frame,anchor="center", text="H _ L L _",font=font.Font(size=20))
        wordLabel.pack(side="right",fill=X,expand=1)

        guessesLabel = Label(text="H L P K",font=font.Font(size=14))
        guessesLabel.pack(fill=X,padx=20)

        input_field = Entry(font=font.Font(size=14))
        input_field.pack(fill=X,padx=50,pady=20)


def main():

    root = Tk()
    app = Hangman_ui()
    root.geometry("600x400")
    root.mainloop()


if __name__ == '__main__':
    main()