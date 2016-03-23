from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from sqlite3 import connect
import login
import parser
import os

class AeriesAppException(Exception):

    def __init__(self, message):
        self.prefix = "Error"
        messagebox.showerror(self.prefix, message)

class AeriesApp(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()

        self.email_label = Label(self, text="Email:", padx="70", pady="5")
        self.pass_label = Label(self, text="Password:", padx="70", pady="5")
        self.email_input = Entry(self)
        self.pass_input = Entry(self, show="\u2022")
        self.submit = Button(self, text="Submit",
                            command=self.validate_form, pady="10")

        self.pack_widgets()

    def validate_form(self):
        user_email = self.email_input.get()
        user_pass = self.pass_input.get()

        if len(user_email) == 0 or len(user_pass) == 0:
            raise AeriesAppException("No email or password entered")

        try:
            a = login.AeriesLogin(user_email, user_pass)
            self.display_grades()
        except login.AeriesLoginException:
            raise AeriesAppException("Failed to login")

    def get_grades(self):
        conn = connect("grades.db")
        c = conn.cursor()
        parser.run(conn, c)
        return [line for line in c.execute("SELECT * FROM grades")]

    def display_grades(self):
        for course in self.get_grades():
            if len(course[1]) != 0:
                string = "%s\t%s" % (course[0], course[1])
            else:
                string = "%s\t%s" % (course[0], "NA")
            Label(text=string).pack()

    def pack_widgets(self):
        self.email_label.pack()
        self.email_input.pack()
        self.pass_label.pack()
        self.pass_input.pack()
        self.submit.pack()

if __name__ == "__main__":
    temp_files = ["ghostdriver.log", "source.txt", "grades.db"]
    for item in os.listdir():
        if item in temp_files:
            os.remove(item)

    root = Tk()
    app = AeriesApp(root)
    app.parent.title("Aeries")
    app.mainloop()
