from tkinter import *
from tkinter import filedialog
from audit_parser import parse_audit_file



class SecurityBenchmarkingTool(Frame): # SBT class inherits from the Frame container widget which is used
    def __init__(self, parent):        # to group and organize other widgets
        Frame.__init__(self, parent)
        self.pack(side=BOTTOM)
        self.parent = parent
        self.parent.configure(background='black')

        self.openButton = Button(self, text="Open .audit file", command=self.openFile,  # button used to open .audit files
                                 width=15, height=1, bg="black", fg="#dd4814", font=("Helvetica", "18"))
        self.openButton.pack(side=LEFT)

        self.saveButton = Button(self, text="Save .audit file", command=self.saveFile,  # button used to save parsed .audit files
                                 width=15, height=1, bg="black", fg="green", font=("Helvetica", "18"))
        self.saveButton.pack(side=RIGHT)

        self.textBox = Text(bg="black", fg="white", font=("Helvetica", "12")) # widget used for output  
        self.textBox.pack(fill=BOTH, expand=1)

    def openFile(self):  # func to open .audit files and parse them using parse_audit_file func from audit_parser.py
        file = filedialog.askopenfile(mode="r", defaultextension=".audit")

        if not file:
            return
        
        f = open(file.name, "r")

        structure = parse_audit_file(f.read())

        form = '{}{}'

        self.textBox.config(state=NORMAL) # allows to insert parsed .audit file into text widget

        for (line, depth, text) in structure:
                self.textBox.insert(END, form.format('.  '*depth, text))
                self.textBox.insert(END, '\n')

        self.textBox.config(state=DISABLED) # makes widget read-only


    def saveFile(self):  # func to save .audit(or .txt) files
        file = filedialog.asksaveasfile(mode="w", defaultextension=".audit")
        f = open(file.name, "w")
        f.write(self.textBox.get("1.0", END))  # The '1.0' means grab the text from line one, characters zero
        f.close()  # and END means go right to the end of the text area


def main():
    root = Tk()  # creates a new window
    app = SecurityBenchmarkingTool(root)
    root.title("Security Benchmarking Tool")
    root.geometry("1000x600")
    root.mainloop()  # tells Python to run the Tkinter event loop


if __name__ == '__main__':
    main()