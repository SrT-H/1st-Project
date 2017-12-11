import tkinter as tk
import tkinter.messagebox
import BTS as bts
import CPN as cpn
import KBANK as kbank
import PTT as ptt
import TRUE as tru

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
        label = tk.Label(self.window, text="Welcom to \nlittle worm PSIT project",\
                         font=("Helvetica", 32)).place(x=180, y=50)

        #Button
        graph_button = tk.Button(self.window, text='Graphs', font=("Helvetica", 20), bg='#ffff66', width=10, height=1, \
                                 command=self.graph_action).place(x=300, y=260)
        fill_button = tk.Button(self.window, text='About us', font=("Helvetica", 20), bg='#66ff66', width=10, height=1,\
                            command=self.about).place(x=300, y=400)
        exit_button = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='#ff4d4d', width=5, height=1, \
                                command=self.exit_action).place(x=680, y=520)

        self.window.size()
        self.window.mainloop()

    def about(self):
        #insert information
        print("About us")
        self.window.destroy()
        about_us()

    def graph_action(self):
        #show graph
        print("Showing graphs!")
        self.window.destroy()
        showing_gragh()

    def exit_action(self):
        #exit
        print("Do you want to exit?")
        result = tkinter.messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if result == 'yes':
            print("EXIT")
            self.window.destroy()
        else:
            print("Continue")
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
        label = tk.Label(self.window, text="Graphs", font=("Helvetica", 32, 'bold')).place(x=330, y=20)

        #Graph Button
        bts_graph = tk.Button(self.window, text='BTS', font=("Helvetica", 20), width=6, height=1, \
                                command=self.show_bts).place(x=300, y=130)
        cpn_graph = tk.Button(self.window, text='CPN', font=("Helvetica", 20), width=6, height=1, \
                                   command=self.show_cpn).place(x=300, y=230)
        kbank_graph = tk.Button(self.window, text='KBANK', font=("Helvetica", 20), width=6, height=1, \
                                   command=self.show_kbank).place(x=300, y=330)
        ptt_graph = tk.Button(self.window, text='PTT', font=("Helvetica", 20), width=6, height=1, \
                                   command=self.show_ptt).place(x=450, y=130)
        true_graph = tk.Button(self.window, text='TRUE', font=("Helvetica", 20), width=6, height=1, \
                                   command=self.show_true).place(x=450, y=230)
        #Action Button
        back_button = tk.Button(self.window, text='<<', font=("Helvetica", 20, 'bold'), width=5, height=1, \
                                command=self.back_action).place(x=30, y=520)
        exit_button = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='#ff4d4d', width=5, height=1, \
                                command=self.exit_action).place(x=680, y=520)

        self.window.size()
        self.window.mainloop()

    def show_bts(self):
        temp = bts.bts_graph()
        temp.show()

    def show_cpn(self):
        temp = cpn.cpn_graph()
        temp.show()

    def show_kbank(self):
        temp = kbank.kbank_graph()
        temp.show()

    def show_ptt(self):
        temp = ptt.ptt_graph()
        temp.show()

    def show_true(self):
        temp = tru.true_graph()
        temp.show()

    def back_action(self):
        #back to main menu
        self.window.destroy()
        main_window()
        print("back to main menu")

    def exit_action(self):
        #exit
        result = tkinter.messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if result == 'yes':
            print("EXIT")
            self.window.destroy()
        else:
            print("Continue")
            pass

class about_us:
    ''' ABOUT US'''
    def __init__(self):
        #Window
        self.window = tk.Tk()
        self.window.resizable(width=False, height=False) #fix window size
        self.window.geometry('{}x{}'.format(1080, 760)) #window size
        self.window.title("About us")
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
        description = "This GUI is use to make all user get access to the graphs easily " \
                      "\nby just clicking the bottons. Its contains all of the contents " \
                      "\nthat we will represent in the presentation sequence."
        name1 = "Pathompong Subtechitmanee\t60070172"
        name2 = "Phubodee Thaneerat\t60070174"
        name3 = "Weeranan Kitpuangsuwan\t60070178"
        name4 = "Theerut Sirichia\t\t60070179"
        name5 = "RinlitaPatsinchongsuk\t60070180"

        label = tk.Label(self.window, text="About us", font=("Helvetica", 32)).place(x=300, y=30)
        label2 = tk.Label(self.window, text=description, font=("Helvetica", 18)).place(x=70, y=120)
        label2_1 = tk.Label(self.window, text="Member", font=("Helvetica", 18, "bold")).place(x=300, y=280)
        label3 = tk.Label(self.window, text=name1, font=("Helvetica", 15)).place(x=180, y=320)
        label4 = tk.Label(self.window, text=name2, font=("Helvetica", 15)).place(x=180, y=360)
        label5 = tk.Label(self.window, text=name3, font=("Helvetica", 15)).place(x=180, y=400)
        label6 = tk.Label(self.window, text=name4, font=("Helvetica", 15)).place(x=180, y=440)
        label7 = tk.Label(self.window, text=name5, font=("Helvetica", 15)).place(x=180, y=480)
        #Button
        back_button = tk.Button(self.window, text='<<', font=("Helvetica", 20, 'bold'), width=5, height=1, \
                                command=self.back_action).place(x=30, y=520)
        exit_button = tk.Button(self.window, text='EXIT', font=("Helvetica", 20, 'bold'), bg='#ff4d4d', width=5, height=1, \
                                command=self.exit_action).place(x=680, y=520)

        self.window.size()
        self.window.mainloop()

    def back_action(self):
        # back to main menu
        self.window.destroy()
        main_window()
        print("back to main menu")

    def exit_action(self):
        # exit
        result = tkinter.messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if result == 'yes':
            print("EXIT")
            self.window.destroy()
        else:
            print("Continue")
            pass



#call main window
main_window()