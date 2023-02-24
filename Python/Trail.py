import tkinter as Graphics #Import tkinter module as Graphics variable
Screen = Graphics.Tk() #create windows as Screen
Screen.geometry("800x500") #open windows of 800x500
Screen.minsize(100, 100)
Screen.maxsize(1000, 1000)
Screen.title("My First GUI") #Rename windows to "My First GUI"
Text = Graphics.Label(Screen, text="Hello world", font=('arial, 18')) #Text variable will store  what to print, font color, font size and screen is telling that is part of screen
Text.pack(padx=50, pady=90) #It will pack variable text and excecute it. setting x as 50 and y as 90
TextBox = Graphics.Text(Screen,height=5, font='arial, 20') #TextBox variable will stora all info about text box to be crated. it ia part of Screen. Font size is 20. height is 5
TextBox.pack() #it will pack text box and excecute it
oneline = Graphics.Entry(Screen) #This is for one line text
oneline.pack() #it will pack oneline variable and run it
Button = Graphics.Button(Screen, text="Click Me!", font='arial, 10') #Button variable will all info about Button
Button.pack() #Pack Button and run it
Button_Frame = Graphics.Frame(Screen) #Arrange button in frame
Button_Frame.columnconfigure(0, weight=1) #column name, weight is width
Button_Frame.columnconfigure(1, weight=1)
Button_Frame.columnconfigure(2, weight=1)
but1 = Graphics.Button(Button_Frame, text=1) #info about button
but1.grid(row=0, column=0, sticky=Graphics.W+Graphics.E) # grid to pack. sticky to arrange lenght width in west and east

but2 = Graphics.Button(Button_Frame, text=2)
but2.grid(row=0, column=1, sticky=Graphics.W+Graphics.E)

but3 = Graphics.Button(Button_Frame, text=3)
but3.grid(row=0, column=2, sticky=Graphics.W+Graphics.E)

but4 = Graphics.Button(Button_Frame, text=4)
but4.grid(row=1, column=0, sticky=Graphics.W+Graphics.E)

but5 = Graphics.Button(Button_Frame, text=5)
but5.grid(row=1, column=1, sticky=Graphics.W+Graphics.E)

but6 = Graphics.Button(Button_Frame, text=6)
but6.grid(row=1, column=2, sticky=Graphics.W+Graphics.E)

Button_Frame.pack(fill='x')

wight = Graphics.Button(Screen, text="Weight")
wight.place(x=200, y=500)


Screen.mainloop()  #Close windows if pressed close button

#Label
# bg - backgroung image
#fg - text color
#borderwidth - is for width of border
#anchor - nw "it will align label to north west"
# relief - Sunken "relief is for styling border, Sunken is type of border"