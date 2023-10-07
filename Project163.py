from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Doctor`s Check')
root.minsize(650, 650)
root.configure(background = 'salmon2')

radios = []
def makeQuestion(text2):
    radio = []
    rb = StringVar(value = '_')
    lbl = Label(root, text = text2, bg = 'light blue', fg = 'black')
    lbl.pack()
    r1 = Radiobutton(root, text = 'Yes', variable = rb, value = 'yes', bg = 'salmon2')
    r1.pack()
    r2 = Radiobutton(root, text = 'No', variable = rb, value = 'no', bg = 'salmon2')
    r2.pack()

    radio.append(rb)
    radio.append(lbl)
    radio.append(r1)
    radio.append(r2)
    radios.append(radio)

makeQuestion('Do you get shortness of breath during regular activites?')
makeQuestion('Do you have any swelling?')
makeQuestion('Do you feel confused, disoriented, or loss of memory?')
makeQuestion('Do you get shortness of breath when you lie down?')
makeQuestion('Do you experience wheezing or coughing?')

def check():
    count = 0
    for i in range(len(radios)):
        if radios[i][0].get() == 'yes':
            count += 1

    if count <= 1:
        messagebox.showinfo('Report', 'You don`t need a checkup.')
    elif count <= 3:
        messagebox.showinfo('Report', 'You might want to checkup.')
    else:
        messagebox.showinfo('Report', 'You really might need a checkup!')

btnCheck = Button(root, text = 'Check', command = lambda: check())
btnCheck.pack()

root.mainloop()