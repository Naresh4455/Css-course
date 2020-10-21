import tkinter as tk 
window =tk.Tk()

window.title("My Awesome APP")

window.geometry("300x300")

prompt = tk.Label(text="This is naresh.\n welcome to my awesom app!", font=("Times New Roman", 20))
prompt.grid()

entry_field =tk.Entry()
entry_field.grid()

buttonl = tk.Button(text="Click ME!", bg="blue")

buttonl.grid()

text_field=tk.Text(height=10, width=30)
text_field.grid()





window.mainloop()