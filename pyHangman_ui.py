from tkinter import *
from tkinter import ttk,font, messagebox
import string
import random

def get_word():
    file = open('words.txt', 'r')
    words = file.readlines()
    return str. rstrip(random.choice(words)).upper() # remove "\n" from word

WIDTH=3
class Hangman_ui(Frame):
    def __init__(self,word):
        super().__init__()

        self.lives_var = StringVar()
        self.word_var = StringVar()
        self.guesses_var = StringVar()
        
        self.word = word
        self.word_letters = set(word)
        self.alphabet = set(string.ascii_uppercase)
        self.used_letters = set()
        self.lives = 7
        
        self.initUI()

    def initUI(self):
        self.master.title("pyHangman")
        self.master.resizable(False, False)

        self.lives_var.set(f"Lives: {self.lives}")
        livesLabel = Label(textvariable=self.lives_var,anchor="e",font=font.Font(size=14))
        livesLabel.pack(fill=X, padx=10)

        frame = Frame()
        frame.pack(fill=X, padx=10,expand=1)

        self.canvas = Canvas(frame,width=220, height=220)
        # init canva
        self.canvas.create_line(10, 200, 210, 200, width=WIDTH)
        self.canvas.create_line(45, 200, 45, 10, width=WIDTH)
        self.canvas.create_line(45, 10, 145, 10, width=WIDTH)
        self.canvas.create_line(45, 60, 95, 10, width=WIDTH)

        self.canvas.pack(side="left",padx=10)

        wordLabel = Label(frame,anchor="center", textvariable=self.word_var,font=font.Font(size=20))
        wordLabel.pack(side="right",fill=X,expand=1)
        word_list = [letter if letter in self.used_letters else '-' for letter in self.word]
        self.word_var.set(' '.join(word_list))

        guessesLabel = Label(textvariable=self.guesses_var,font=font.Font(size=14))
        guessesLabel.pack(fill=X,padx=20)

        self.input_field = Entry(font=font.Font(size=14))
        self.input_field.pack(fill=X,padx=50,pady=20)
        self.guesses_var.set(' '.join(self.used_letters))
        
        self.master.bind("<Return>", self.callback)

    
    def callback(self, event):
        user_letter = self.input_field.get().upper()
        if len(self.word_letters) > 0 and self.lives > 0:
            if user_letter in self.alphabet - self.used_letters:
                self.used_letters.add(user_letter)
                self.guesses_var.set(' '.join(self.used_letters))
                if user_letter in self.word_letters:
                    self.word_letters.remove(user_letter)
                    word_list = [letter if letter in self.used_letters else '-' for letter in self.word]
                    self.word_var.set(' '.join(word_list))
                    if len(self.word_letters) == 0:
                        messagebox.showinfo("Congrats", "You win")
                else:
                    self.lives = self.lives - 1
                    self.lives_var.set(f"Lives: {self.lives}")
                    if self.lives == 6:
                        self.canvas.create_line(145, 10, 145, 40, width=WIDTH)
                    if self.lives == 5:
                        self.canvas.create_oval(145-23, 40, 145+23, 40+46, width=WIDTH)
                    if self.lives == 4:
                        self.canvas.create_line(145, 86, 145, 131, width=WIDTH)
                    if self.lives == 3:
                        self.canvas.create_line(145, 131, 112, 164, width=WIDTH)
                    if self.lives == 2:
                        self.canvas.create_line(145, 131, 178, 164, width=WIDTH)
                    if self.lives == 1:
                        self.canvas.create_line(145, 104, 115, 104, width=WIDTH)
                    if self.lives == 0:
                        self.canvas.create_line(145, 104, 175, 104, width=WIDTH)
                    
            elif user_letter in self.used_letters:
                messagebox.showerror("Error","You have already used that letter. Guess another letter")

            else:
                messagebox.showerror("Error","That is not a valid letter")
        
        if self.lives == 0:
            self.word_var.set(self.word)
            messagebox.showinfo("Sorry", "You loose")

        self.input_field.delete(0, 'end')


def main():
    word = get_word()
    word = "python".upper()
    root = Tk()
    app = Hangman_ui(word)
    root.geometry("600x400")
    root.mainloop()


if __name__ == '__main__':
    main()