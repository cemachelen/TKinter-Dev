from tkinter import *
from tkinter import ttk  # Newer themed widgets


def calculate(*args):
    """
    calculate procedure, which is called either when the user presses the
    Calculate button, or hits the Return key
    """
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
# set up the main window, giving it the title "Feet to Meters"
root.title("Feet to Meters")
# create a frame widget, which will hold all the content of our user interface,
# and place that in our main window.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# The "columnconfigure"/"rowconfigure" bits just tell Tk that if the main
# window is resized, the frame should expand to take up the extra space.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# the three main widgets in our program:
#  entry where we type the number of feet
feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
# label where we put the resulting number of meters
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# Calculate button that we press to perform the calculation
ttk.Button(mainframe, text="Calculate",
           command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
# The above three lines do exactly the same thing for the three static text
# labels in our user interface; create each one, and place it onscreen in the
# appropriate cell in the grid.
# Add padding etc for each widget
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# focus at the feet entry widget
feet_entry.focus()
# Make enter key work!
root.bind('<Return>', calculate)
# Run the app:
root.mainloop()
