import math
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Frontend:
    """Handles all GUI components and user interactions"""
    
    RUNNER_DATA = [
        ("Runner1", "00:00.0", "Nick1"),
        ("Runner2", "00:00.0", "Nick2"),
        ("Runner3", "00:00.0", "Nick3"),
        ("Runner4", "00:00.0", "Nick4"),
        ("Runner5", "00:00.0", "Nick5"),
        ("Runner6", "00:00.0", "Nick6"),
        ("Runner7", "00:00.0", "Nick7"),
    ]

    def __init__(self, backend):
        self.backend = backend
        self.window = tb.Window(themename="darkly")
        self.runner_entries = []
        self._configure_window()
        self._create_gui_components()

    def _configure_window(self):
        """Initializes window configuration"""
        self.window.title("StreamTexts Leaderboard")
        style = tb.Style()
        font_specs = ('Montserrat', 10)
        style.configure('.', font=font_specs)
        style.configure('success.TLabelframe.Label', font=(*font_specs, 'bold'))

    def _create_gui_components(self):
        """Creates all GUI elements"""
        container = tb.Frame(self.window, padding=20, bootstyle="dark")
        container.pack(fill="both", expand=True)
        
        for i in range(4):
            container.columnconfigure(i, weight=1)
        
        self._setup_runner_panels(container)
        self._create_save_button(container)

    def _setup_runner_panels(self, parent):
        """Creates runner panels in grid layout"""
        for idx, (name, init_time, init_nick) in enumerate(self.RUNNER_DATA):
            row, col = divmod(idx, 4)
            panel = self._create_runner_panel(parent, name, init_time, init_nick)
            panel.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    def _create_runner_panel(self, parent, name, init_time, init_nick):
        """Creates individual runner input panel"""
        panel = tb.Labelframe(
            parent,
            text=name,
            bootstyle="success",
            padding=(12, 8)
        )
        panel.columnconfigure(0, weight=1)

        time_var = tk.StringVar(value=init_time)
        nick_var = tk.StringVar(value=init_nick)
        
        self._create_entry(panel, "Time:", time_var, 0)
        self._create_entry(panel, "Nickname:", nick_var, 2)
        
        self.runner_entries.append({
            "name": name,
            "time_var": time_var,
            "nick_var": nick_var
        })
        
        return panel

    def _create_entry(self, parent, label_text, variable, row):
        """Creates a labeled entry component"""
        tb.Label(parent, text=label_text, bootstyle="light").grid(
            row=row, column=0, sticky="w")
        tb.Entry(parent, textvariable=variable, bootstyle="info", width=14).grid(
            row=row+1, column=0, sticky="ew", pady=(4, 8 if row == 0 else 4))

    def _create_save_button(self, parent):
        """Creates the save/update button"""
        save_btn = tb.Button(
            parent,
            text="SAVE ALL & UPDATE LEADERBOARD",
            bootstyle="success",
            command=self._save_all
        )
        save_btn.grid(
            row=math.ceil(len(self.RUNNER_DATA) / 4),
            column=0,
            columnspan=4,
            pady=(20, 0),
            sticky="ew"
        )

    def _save_all(self):
        """Handles save button click event"""
        results = []
        for entry in self.runner_entries:
            results.append({
                "name": entry["name"],
                "time": entry["time_var"].get(),
                "nickname": entry["nick_var"].get()
            })
        self.backend.update_leaderboard(results)

    def run(self):
        """Starts the application main loop"""
        self.window.mainloop()