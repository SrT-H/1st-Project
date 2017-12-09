import tkinter as tk
import tkinter.messagebox
import demo

class main_window:
    ''' MAIN WINDOW'''
    def __init__(self):
        #Window
        self.window = tk.Tk()
        self.window.resizable(width=False, height=False) #fix window size
        self.window.geometry('{}x{}'.format(1080, 760)) #window size
        self.window.title("Welcome")
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.x = (ws / 2) - (1080 / 2)
        self.y = (hs / 2) - (760 / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (800, 600, self.x, self.y))

        #Text
<<<<<<< HEAD
        label = tk.Label(self.window, text="Welcom to \nlittle worm PSIT project",\
                         font=("Helvetica", 32)).place(x=180, y=50)

        #Button
        graph_button = tk.Button(self.window, text='Graphs', font=("Helvetica", 20), bg='#faf800', width=10, height=1, \
                                 command=self.graph_action).place(x=300, y=260)
        fill_button = tk.Button(self.window, text='About us', font=("Helvetica", 20), bg='#00b300', width=10, height=1,\
                            command=self.about_us).place(x=300, y=400)
=======
        label = tk.Label(self.window, text="Welcom to python", font=("Helvetica", 32)).place(x=230, y=10)

        #Button
        fill_button = tk.Button(self.window, text='Text', font=("Helvetica", 20), bg='#00b300', width=10, height=1,\
                            command=self.fill_action).place(x=120, y=300)
        graph_button = tk.Button(self.window, text='Graph', font=("Helvetica", 20), bg='#faf800',  width=10, height=1,\
                            command=self.graph_action).place(x=500, y=300)
>>>>>>> fb26470b967dd7b25b216950d503f14783be98bb
        exit_button = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='red', width=5, height=1,\
                            command=self.exit_action).place(x=680, y=520)

        self.window.size()
        self.window.mainloop()

<<<<<<< HEAD
    def about_us(self):
        #insert information
        print("About us")
=======
    def fill_action(self):
        #insert information
        print("Fill in the blank.")
>>>>>>> fb26470b967dd7b25b216950d503f14783be98bb

    def graph_action(self):
        #show graph
        print("Showing graphs!")
        self.window.destroy()
        showing_gragh()

    def exit_action(self):
        #exit
        result = tkinter.messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if result == 'yes':
            self.window.destroy()
        else:
            pass

class showing_gragh:
    ''' FILL IN THE BOX'''
    def __init__(self):
        #Window
        self.window = tk.Tk()
        self.window.resizable(width=False, height=False)  # fix window size
        self.window.geometry('{}x{}'.format(1080, 760))  # window size
        self.window.title("Stock Graphs")
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.x = (ws / 2) - (1080 / 2)
        self.y = (hs / 2) - (760 / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (800, 600, self.x, self.y))

        # Text
        label = tk.Label(self.window, text="Graph", font=("Helvetica", 32)).place(x=350, y=10)

        #Button
        back_button = tk.Button(self.window, text='<<', font=("Helvetica", 20, 'bold'), width=5, height=1, \
                            command=self.back_action).place(x=30, y=520)
        showing_graph = tk.Button(self.window, text='Set50', font=("Helvetica", 20, 'bold'), width=6, height=1, \
                                command=self.set50).place(x=100, y=100)
        exit_button = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='red', width=5, height=1, \
                                command=self.exit_action).place(x=680, y=520)
        self.window.size()
        self.window.mainloop()

    def set50(self):
        temp = demo.set50()
        temp.create_graph()

    def back_action(self):
        #back to main menu
        self.window.destroy()
        main_window()
        print("back to main menu")

    def exit_action(self):
        #exit
        result = tkinter.messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if result == 'yes':
            self.window.destroy()
        else:
            pass
main_window()
