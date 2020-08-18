from Creator import Char
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

win = Tk()
win['background'] = '#2E4053'


def b_start_click():
    b_start.destroy()
    b_settings.destroy()
    b_quit.destroy()

    def b_create_char_job_click():
        char_name = str(c_n.get())
        char_age = int(c_a.get())
        char_genre = str(c_g.get())
        char_job = str(c_j.get())

        p1 = Char(char_name, char_age, char_genre, char_job)
        lb_char = Label(win, text=f'{p1.char_name()} \n{p1.char_age()} \n{p1.char_genre()} \n{p1.char_job()}')
        lb_char.place(x=150, y=50)

    # Char Creator Entries
    c_n = Entry(win)
    c_n.place(x=250, y=200)

    c_a = Entry(win)
    c_a.place(x=250, y=250)

    c_j = Entry(win)
    c_j.place(x=250, y=350)

    # Char Creator Comboboxes
    c_g = ttk.Combobox(win, values=['Male', 'Female'])
    c_g.place(x=250, y=300)

    # Char Creator Buttons
    b_create = Button(win, text='Create Character', command=b_create_char_job_click)
    b_create.place(x=450, y=250)

    # Char Creator Labels
    lb_name = Label(win, text="Character's name")
    lb_name.place(x=260, y=175)

    lb_age = Label(win, text="Character's age")
    lb_age.place(x=260, y=225)

    lb_genre = Label(win, text="Character's genre")
    lb_genre.place(x=260, y=275)

    lb_job = Label(win, text="Character's job")
    lb_job.place(x=260, y=325)


def settings_click():
    set_win = Toplevel()
    set_win['background'] = '#2E4053'
    set_win.title('Settings Window')

    def b_win_dimensions_click():
        heigh_value = Scale(set_win, from_=800, to=1920, orient=HORIZONTAL)
        heigh_value.place(x=250, y=150)

        width_value = Scale(set_win, from_=600, to=1080, orient=HORIZONTAL)
        width_value.place(x=400, y=150)

        def save_settings_click():
            heigh = str(heigh_value.get())
            width = str(width_value.get())
            win_geometry = heigh + 'x' + width
            win.geometry(win_geometry)

        # Windows Settings Buttons
        b_save_settings = Button(set_win, text='Save Settings', command=save_settings_click)
        b_save_settings.place(x=350, y=250)

        # Windows Settings Labels
        lb_heigh = Label(set_win, text='Heigh')
        lb_heigh.place(x=280, y=110)

        lb_width = Label(set_win, text='Width')
        lb_width.place(x=430, y=110)

    def b_change_background_color_click():
        color_chooser = colorchooser.askcolor(title='Select the background color')
        win.configure(background=color_chooser[1])

    # SETTINGS BUTTONS
    b_win_dimensions = Button(set_win, text="Window's dimensions", command=b_win_dimensions_click)
    b_win_dimensions.place(x=50, y=50)

    b_change_background_color = Button(set_win, text='Change Background Color', command=b_change_background_color_click)
    b_change_background_color.place(x=200, y=50)

    set_win.geometry('800x600')
    set_win.mainloop()


def b_quit_click():
    win.destroy()


# Main Page GUI
b_start = Button(win, text='Start', command=b_start_click, width=10)
b_start.place(x=350, y=280)

b_settings = Button(win, text='Settings', command=settings_click, width=10)
b_settings.place(x=350, y=330)

b_quit = Button(win, text='Quit', command=b_quit_click, width=10)
b_quit.place(x=350, y=380)

win.geometry('800x600')
win.mainloop()
