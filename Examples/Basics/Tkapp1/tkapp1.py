# -*- coding: utf-8 -*-
"""
.. module:: App1
    :platform: Unix/ Windows
    :synopis:
.. moduleauthors: Helen Burns (UoL).
.. description: This module was developed as part of
                Global Challenges Research Fund (GCRF) African SWIFT
                (Science for Weather Information and Forecasting Techniques.
   :copyright: © 2019 University of Leeds.
   :license: BSD-2 Clause.
Example:
    To use::
Memebers:
.. cemachelen_TK-dev:
   https://github.com/cemachelen/TKinter-Dev
"""
import tkinter as tk


class App1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == "__main__":
    root = tk.Tk()
    App1(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
