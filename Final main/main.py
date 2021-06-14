##########################################
#   Title: Blockchain Black Magic        #
##########################################


from tkinter import *
from tkinter import messagebox
import log
import threading

index = 5 #This global element is used in order to unlock more elements as time passes

#Moves the user to a different window while also destroying the current window, another change could be allowing the map, potion book, and security logs
def moveMenu(root, num):
    root.destroy()
    if num == 1:
        getMap()
    elif num == 2:
        checkBlockchain()
    elif num == 3:
        potionBook()
    elif num == 4:
        page2()
    elif num == 5:
        makeSure()
    else :
        mainMenu()


#Open the Map tab in order to show the student the paths and ingridient locations
def getMap():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.geometry("700x600")
    root.resizable(width=False, height=False) #Used in order to prevent the students from changing the window because of limited picture size
    root.title("Map of Tennessee Tech")
    canvas = Canvas(root, width = 700, height = 380)
    canvas.pack()
    img = PhotoImage(file= "graphv3.ppm") #ppm files are the only ones that Tkinter is able to open (To my knowledge)
    img = img.subsample(3,3) #Image was too large, so this command is used in order to change the size
    canvas.create_image(0,0, anchor=NW, image=img)
    root.title("Map")

    Message(root, text='VALERIAN SPRIGS is at TVE, HOOP, SLH, ESTA, VARS', font=('Times', 10, 'bold'), width=450).pack(anchor='nw') #Message blocks are packed in the direction of the anchor
    Message(root, text='ALIHOSTY LEAVES is at MBRC, LIBR, RUC', font=('Times', 10, 'bold'), width=450).pack(anchor='nw')
    Message(root, text='BILLYWIG STRINGS is at SWH, CRAW', font=('Times', 10, 'bold'), width=450).pack(anchor='nw')
    Message(root, text='PEARL DUST is at RMH, USVC, FNDH', font=('Times', 10, 'bold'), width=450).pack(anchor='nw')
    Message(root, text='DITTANY is at MNTO, PRSC, LEWS', font=('Times', 10, 'bold'), width=450).pack(anchor='nw')
    Button(root, text = 'Main Menu', bd=5, pady=4, command =lambda : moveMenu(root, 0)).pack(side = 'top', pady=4)
    root.mainloop() #mainloop is the final command that you use in order to make the menu appear on the screen

#The security logs tab that shows the Counselor name, Clock-in and Clock-out times, Location, Previous and Current Hash, Nonce value
def checkBlockchain():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.title("Security Logs")
    root.geometry("1400x400")
    root.resizable(width=False, height=False)
    root.config(bg='black')

    frame = Frame(root)
    frame.pack(anchor='nw')

    scrollbar = Scrollbar(frame) #The scrollbar allows the students to look through the Security Logs as they are released
    scrollbar.pack(side = "right", fill = Y)
    

    myList = Listbox(frame, yscrollcommand = scrollbar.set, height=18, width=240, bg='black', fg='lightgreen')
    
    
    #Pre-generated paths that equal potion recipes so that each counselor corresponds with a potion
    l1 = [(2,0),(10,8),(7,5),(5,5),(6,5)]       # Start at node 2 (HOOP)
    l2 = [(11,0),(10,5),(7,5),(3,5),(5,5)]      # Start at node 11 (ESTA)
    l3 = [(1,0),(5,6),(9,5),(15,8),(13,5)]      # Start at node 1 (TVE)
    l4 = [(14,0),(12,8),(9,8),(13,8),(16,8)]    # Start at node 14 (VARS)
    locations = ["None", "TVE", "HOOP", "MNTO", "MBRC", "SWH", "RMH", "PRSC", "SLH", "LEWS", "LIBR", "ESTA", "CRAW", "RUC", "VARS", "USVC", "FNDH"]

    #The log is pre-generated so the timers show off more and more of the array as it goes, using the updateBlocks() function
    l = log.Log("Colin", "Mimi", "Alex", "Andrew")
    l.create_log(l1, l2, l3, l4)
    #Looping through the log outputting the information in a specific format
    #Tkinter is very limited in the formatting that it can do so it didn't look the way that was intended
    for i in range(1,index):
        myList.insert(END, '{0:<20}{1:<20}{2:<15}{3:<80}{4:<90}{5:<3}'.format(
            'Counselor: '+ l.get_ID(i), 'Location: ' + locations[int(l.get_location(i))], 'Time: '+ l.get_time(i), 'Hash: ' + l.get_hash(i),
            'Previous Hash: ' + l.get_p_hash(i), 'Nonce: ' + l.get_nonce(i)))
        myList.insert(END, "")
    
    myList.pack(anchor = 'nw')
    scrollbar.config(command= myList.yview)
    
    Button(root, text = 'Main Menu', bd=5, command =lambda : moveMenu(root, 0)).pack(anchor='nw')
    Button(root, text="Refresh", bd = 5, command = lambda : moveMenu(root,2)).pack(anchor='nw', side = 'left')


    root.mainloop()

#This opens two ppm files (Only picture files that Tkinter can open), Can be changed into a Canvas object to allow for random potion recipes
def potionBook():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.title("Page 1")
    root.geometry("512x360")
    root.resizable(width=False, height=False) 

    canvas = Canvas(root, width = 512, height = 360)
    canvas.pack()
    img = PhotoImage(file= "page1.ppm")
    img = img.subsample(2,2)
    canvas.create_image(0,0, anchor=NW, image=img)
    btn = Button(root, text='>', height=1, width=1, command = lambda : moveMenu(root, 4))  #(command = lamda :) is used to send commands with arguments
    canvas.create_window( 480, 50, window = btn)
    btn = Button(root, text='Main Menu', command = lambda : moveMenu(root, 0))
    canvas.create_window( 256, 20, window = btn)

    root.mainloop()     

#This is the second page of the potion book that includes the last two potions, possible changes include changing it from a constant image to a randomized potion recipe
def page2():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.title("Page 2")
    root.geometry("512x360")
    root.resizable(width=False, height=False)

    canvas = Canvas(root, width = 512, height = 360)
    canvas.pack()
    img = PhotoImage(file= "page2.ppm")
    img = img.subsample(2,2)
    canvas.create_image(0,0, anchor=NW, image=img)
    btn = Button(root, text='<', height=1, width=1, command = lambda : moveMenu(root, 3))  #(command = lamda :) is used to send commands with arguments
    canvas.create_window( 15, 50, window = btn)
    btn = Button(root, text='Main Menu', command = lambda : moveMenu(root, 0))
    canvas.create_window( 256, 20, window = btn)

    root.mainloop()   
    
#The main menu of the program, the actual main is just calling this function at the beginning
def mainMenu():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.title("Blockchain Black Magic")
    root.geometry("600x328")
    root.resizable(width=False, height=False)
    bg = PhotoImage(file = "padlock.ppm")
    bg = bg.subsample(2,2)
  
# Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400) #Canvas' have very specific commands that limit the capabilities of the window
    canvas1.pack(fill = "both", expand = True)
  
# Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#Creates the buttons and connects them to their paths
    btn = Button(root, text = 'See map', bd=5, command =lambda : moveMenu(root, 1))
    btn2 = Button(root, text = 'Check Blockchain', bd=5, command =lambda : moveMenu(root, 2))
    btn3 = Button(root, text = 'Open Potion Book', bd=5, command=lambda : moveMenu(root, 3))
    btn5 = Button(root, text="Exit", bd=5, fg="red", command= lambda : moveMenu(root, 5))

#Creates elements that allow the buttons so overlay the background
    canvas1.create_window( 0, 15, anchor = "w", window = btn)   #Each button is being placed into the canvas on top of the image
    canvas1.create_window( 0, 55, anchor = "w", window = btn2)
    canvas1.create_window( 0, 95, anchor = "w", window = btn3)
    canvas1.create_window( 0, 135, anchor = "w", window = btn5)
    root.mainloop()

def disableEvents(): #This command is used to prevent the users from closing window in order to not destroy the threads
    pass

#This is used to essentially childproof the program to prevent problems with the timer
def makeSure():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", disableEvents) #This command prevents the students from closing the window randomly because the timers are used in a different thread
    root.title("Be careful!!!")
    root.geometry('400x100')
    root.resizable(width=False, height=False)
    Label(root, text="Has the activity completed? If not DO NOT close the application").pack() #Question placed in there to add one final protection against them closing it
    Button(root, text='yes', command= lambda : root.destroy()).pack()
    Button(root, text='no', command= lambda : moveMenu(root, 0)).pack()

    root.mainloop()

    
#We open different threads in order to update each of the blocks as the timer hits the certain time period
def updateBlocks():
    messagebox.showinfo(title='', message="The Blockchain has been updated, you can check the log in the Blockchain tab") #This is just a small pop up to inform the students
    global index
    index += 4
    

if __name__ == "__main__":
    
    try:  #The try finally is used in order to make sure that the code closes each of the threads
        threads= [] #Opens an array of threads and places each one in there in order to have multiple running at the same time
        for i in range(1,10):
            threads.append(threading.Timer(i*180, updateBlocks)) #The timer is set to 180 seconds (3 minutes) and there are multiple all opened at the same time
            threads[i-1].start() #The array has to start at 1 but the threads start at 0

        mainMenu()
    finally:
        for i in range(1,10):
            threads[i-1].cancel() #This closes each of the threads within the arrays
    
    
