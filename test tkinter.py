import tkinter as tk
import tkinter.messagebox

class welcome_window:
    ''' MAIN WINDOW'''

    def __init__(self):
        #Window
        self.window = tk.Tk()
        self.window.resizable(width=False, height=False) #fix window size
        self.window.geometry('{}x{}'.format(1080, 760)) #window size
        self.window.title("Welcome!")
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (1080 / 2)
        y = (hs / 2) - (760 / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (800, 600, x, y))

        #Text
        label = tk.Label(self.window, text="Welcom to python", font=("Helvetica", 32)).place(x=230, y=10)
        #Button
        button1 = tk.Button(self.window, text='Text', font=("Helvetica", 20), bg='#00b300', width=10, height=1, command=self.fill_buttton).place(x=120, y=300)
        button2 = tk.Button(self.window, text='Graph', font=("Helvetica", 20), bg='#faf800',  width=10, height=1, command=self.graph_button).place(x=500, y=300)
        button3 = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='red', width=5, height=1, command=self.exit_button).place(x=680, y=520)

        self.window.size()
        self.window.mainloop()

    def fill_buttton(self):
        #insert information
        print("Fill in the blank.")

    def graph_button(self):
        #show graph
        print("Showing graphs!")

    def exit_button(self):
        #exit
        result = tkinter.messagebox.askquestion("Are you sure?", "Do you want to exit?", icon='warning')
        if result == 'yes':
            self.window.destroy()
        else:
            pass

welcome_window()
