from tkinter import *
from tkinter import ttk,font

class Hangman_ui(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("pyHangman")
        self.master.resizable(False, False)
        self.lives_var = StringVar()
        self.word_var = StringVar()
        self.guesses_var = StringVar()

        livesLabel = Label(textvariable=self.lives_var,anchor="e",font=font.Font(size=14))
        self.lives_var.set("Lives: 7")
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

        wordLabel = Label(frame,anchor="center", textvariable=self.word_var,font=font.Font(size=20))
        self.word_var.set("H _ L L _")
        wordLabel.pack(side="right",fill=X,expand=1)

        guessesLabel = Label(textvariable=self.guesses_var,font=font.Font(size=14))
        self.guesses_var.set("H L P K")
        guessesLabel.pack(fill=X,padx=20)

        self.input_field = Entry(font=font.Font(size=14))
        self.input_field.pack(fill=X,padx=50,pady=20)
        
        self.master.bind("<Return>", self.callback)

    def callback(self, event):
        txt = self.input_field.get()
        self.guesses_var.set(txt)
        self.input_field.delete(0, 'end')


def main():

    root = Tk()
    app = Hangman_ui()
    root.geometry("600x400")
    root.mainloop()


if __name__ == '__main__':
    main()