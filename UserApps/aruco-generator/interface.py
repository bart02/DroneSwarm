from Tkinter import *
import tkFileDialog

x = 0
y = 0
l = 0
first = 0
side = 0
sep = 0
mocap = 0
origin = 0




def waitInterace():
    global x, y, l, first, side, sep, mocap, origin, fp

    def buttoncb(w):
        global x, y, l, first, side, sep, mocap, origin, fp
        x = TkX.get()
        y = TkY.get()
        l = TkL.get()
        first = TkFirst.get()
        side = TkSide.get()
        sep = TkSep.get()
        mocap = mcp.get()
        origin = org.get()
        file_path = tkFileDialog.asksaveasfilename(initialdir="", title="Select file")
        w.destroy()
        fp = file_path

    root = Tk()
    root.resizable(False, False)

    LX = Label(root, text='X: ')
    LX.grid(row=0, column=0, sticky=E)
    TkX = Entry(root, width=30)
    TkX.grid(row=0, column=1)

    LY = Label(root, text='Y: ')
    LY.grid(row=1, column=0, sticky=E)
    TkY = Entry(root, width=30)
    TkY.grid(row=1, column=1)

    LL = Label(root, text='Length of column: ')
    LL.grid(row=2, column=0, sticky=E)
    TkL = Entry(root, width=30)
    TkL.grid(row=2, column=1)

    LFirst = Label(root, text='First: ')
    LFirst.grid(row=3, column=0, sticky=E)
    TkFirst = Entry(root, width=30)
    TkFirst.grid(row=3, column=1)

    LSide = Label(root, text='Side: ')
    LSide.grid(row=4, column=0, sticky=E)
    TkSide = Entry(root, width=30)
    TkSide.grid(row=4, column=1)

    LSep = Label(root, text='Sep: ')
    LSep.grid(row=5, column=0, sticky=E)
    TkSep = Entry(root, width=30)
    TkSep.grid(row=5, column=1)

    LMocap = Label(root, text='Mocap: ')
    LMocap.grid(row=6, column=0, sticky=E)
    mcp = IntVar()
    TkMocap = Checkbutton(root, variable=mcp)
    TkMocap.select()
    TkMocap.grid(row=6, column=1)

    LOrigin = Label(root, text='Origin: ')
    LOrigin.grid(row=7, rowspan=2, column=0, sticky=E)
    org = IntVar()
    rbutton1 = Radiobutton(root, text='local_origin', variable=org, value=0)
    rbutton2 = Radiobutton(root, text='local_origin_upside_down', variable=org, value=1)
    rbutton1.grid(row=7, column=1, sticky=W)
    rbutton2.grid(row=8, column=1, sticky=W)

    button = Button(root, text="OK", command=lambda: buttoncb(root))
    button.grid(row=999, column=0, columnspan=999)
    root.mainloop()
    return x, y, l, first, side, sep, mocap, origin, fp


