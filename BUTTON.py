try:
    from Tkinter import Label
    from ttk import Style
    from tkFont import Font, nametofont
except ImportError:
    from tkinter import Label
    from tkinter.ttk import Style
    from tkinter.font import Font, nametofont

def get_background_of_widget(widget):
    try:
        # We assume first tk widget
        background = widget.cget("background")
    except:
        # Otherwise this is a ttk widget
        style = widget.cget("style")

        if style == "":
            # if there is not style configuration option, default style is the same than widget class
            style = widget.winfo_class()

        background = Style().lookup(style, 'background')

    return background

class Link_Button(Label, object):
    def __init__(self, master, text, background=None, font=None, familiy=None, size=None, underline=True, visited_fg = "#551A8B", normal_fg = "#0000EE", visited=False, action=None):
        self._visited_fg = visited_fg
        self._normal_fg = normal_fg

        if visited:
            fg = self._visited_fg
