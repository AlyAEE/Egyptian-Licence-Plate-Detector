# from project import *


# dataBase = []
# dataBase_b = []
# buildDB_b()
# buildDB_D()

# buildDB()    
# fileName = ""
# def data1():
#     global fileName
#     fileName = e0.get()
	
#     plateText = main5(fileName)
#     # print(plateText)
#     # messagebox.showinfo('output', plateText)


	
# master = Tk(className='Plate Detector')
# master.geometry('500x500')
# label0 = Label(master, text='File Name')
# label0.place(x=80, y=130)
# e0 = Entry(master)
# e0.place(x=240,y=130)


# b = Button(master, text='OK', width=20, bg='brown', fg='white', command=data1)
# b.place(x=180, y=380)
# mainloop()

from ipywidgets import Text, Button, VBox, Output
from IPython.display import display
from project import *

# Initialize databases
dataBase = []
dataBase_b = []

buildDB_b()
buildDB_D()
buildDB()

output = Output()

def on_button_click(b):
    with output:
        output.clear_output()
        file_name = text_input.value
        plate_text = main5(file_name)
        print("Detected Plate Text:", plate_text)

text_input = Text(description="File:")
button = Button(description="Detect")
button.on_click(on_button_click)

display(VBox([text_input, button, output]))
