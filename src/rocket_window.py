from os import path
import tkinter as tk
import pandas as pd
import sys
import main
from draw_rocket import Drawer
import rocket_trajectories

class Interface:
    def __init__(self):
        self.current_file = '../resource/rocket_database.csv'
        self.window = tk.Tk()
        self.window.title("Rocket Launcher")
        self.window.geometry("1080x720")
        self.window.resizable(False, False)
        self.drawer = Drawer(self.window)
        
        self.window.bind("<KeyPress>", self.key_event)
        self.window.bind("<ButtonRelease>", self.mouse_event)
        
        self.monitor = self.drawer.get_frame()
        self.monitor.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.board = tk.Frame(self.window, bg='gray', bd=1, relief=tk.SUNKEN)
        self.board.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.window.grid_columnconfigure(0, weight=3, uniform="group1")
        self.window.grid_columnconfigure(1, weight=1, uniform="group1")
        self.window.grid_rowconfigure(0, weight=1)
        
        self.settings = tk.Frame(self.board, bg='bisque3', bd=1)
        self.buttons = tk.Frame(self.board, bg='gray', bd=1)
        self.settings.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.buttons.grid(row=1, column=0, sticky="nsew")
        
        self.board.grid_rowconfigure(0, weight=3, uniform="group1")
        self.board.grid_rowconfigure(1, weight=2, uniform="group1")
        self.board.grid_columnconfigure(0, weight=1)
        
        self.b_load = tk.Button(self.buttons, text="Charger", command=self.load) #charge .csv (clear) (affiche interface choix fusées)
        self.b_save = tk.Button(self.buttons, text="Enregistrer", command=self.save) #enregistre selectionné
        self.b_clear = tk.Button(self.buttons, text="Effacer", command=self.erase)
        self.b_traj = tk.Button(self.buttons, text="Trajectoire", command=self.trajectory) #trajectoire
        self.b_quit = tk.Button(self.buttons, text="Quitter", command=sys.exit) #trajectoire
        
        self.b_load.pack(expand=tk.YES, padx=25, pady=10, fill=tk.BOTH)
        self.b_save.pack(expand=tk.YES, padx=25, pady=10, fill=tk.BOTH)
        self.b_clear.pack(expand=tk.YES, padx=25, pady=10, fill=tk.BOTH)
        self.b_traj.pack(expand=tk.YES, padx=25, pady=10, fill=tk.BOTH)
        self.b_quit.pack(expand=tk.YES, padx=25, pady=10, fill=tk.BOTH)
        
        self.main_settings = tk.Frame(self.settings)
        self.stages_settings = tk.Frame(self.settings)
        self.stages_settings_canvas = tk.Canvas(self.stages_settings, width=300, height=140, scrollregion=(0,0,500,860))
        self.sroll_settings = tk.Scrollbar(self.stages_settings, orient=tk.VERTICAL)
        self.sroll_settings.pack(side=tk.RIGHT,fill=tk.Y)
        self.sroll_settings.config(command=self.stages_settings_canvas.yview)
        self.b_create = tk.Button(self.settings, text="Create", command=self.create);
        self.l_height = tk.Label(self.main_settings, text="Height")
        self.l_liftoff_mass= tk.Label(self.main_settings, text="Liftoff mass")
        self.l_payload_mass = tk.Label(self.main_settings, text="Payload mass")
        self.s_height = tk.Scale(self.main_settings, from_=10, to=120, orient=tk.HORIZONTAL)
        self.s_liftoff_mass = tk.Scale(self.main_settings, from_=2, to=3000, orient=tk.HORIZONTAL)
        self.s_payload_mass = tk.Scale(self.main_settings, from_=50, to=50000, orient=tk.HORIZONTAL)
          
        self.stages_settings_canvas_frame = tk.Frame(self.stages_settings_canvas)
        self.stages_settings_canvas.create_window((40,4), window=self.stages_settings_canvas_frame, anchor="nw", tags="self.frame")
        
        self.s1_length = tk.Scale(self.stages_settings_canvas_frame, from_=5, to=50, orient=tk.HORIZONTAL)
        self.s1_diameter = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=15, orient=tk.HORIZONTAL) #dixieme
        self.s1_thurst = tk.Scale(self.stages_settings_canvas_frame, from_=30, to=50000, orient=tk.HORIZONTAL)
        self.s1_lsp = tk.Scale(self.stages_settings_canvas_frame, from_=200, to=500, orient=tk.HORIZONTAL)
        self.s1_m0 = tk.Scale(self.stages_settings_canvas_frame, from_=2, to=3000, orient=tk.HORIZONTAL)
        self.s1_mp = tk.Scale(self.stages_settings_canvas_frame, from_=2, to=3000, orient=tk.HORIZONTAL)
        
        self.l_s1 = tk.Label(self.stages_settings_canvas_frame, text="Stage 1\n", fg='blue')
        
        self.l_s1_length = tk.Label(self.stages_settings_canvas_frame, text="S1 length")
        self.l_s1_diameter = tk.Label(self.stages_settings_canvas_frame, text="S1 diameter")
        self.l_s1_thurst = tk.Label(self.stages_settings_canvas_frame, text="S1 thurst")
        self.l_s1_lsp = tk.Label(self.stages_settings_canvas_frame, text="S1 lsp")
        self.l_s1_m0 = tk.Label(self.stages_settings_canvas_frame, text="S1 m0")
        self.l_s1_mp = tk.Label(self.stages_settings_canvas_frame, text="S1 mp")
        
        self.s2_length = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=50, orient=tk.HORIZONTAL)
        self.s2_diameter = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=15, orient=tk.HORIZONTAL)
        self.s2_thurst = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=10000, orient=tk.HORIZONTAL)
        self.s2_lsp = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=500, orient=tk.HORIZONTAL)
        self.s2_m0 = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=1000, orient=tk.HORIZONTAL)
        self.s2_mp = tk.Scale(self.stages_settings_canvas_frame, from_=0, to=1000, orient=tk.HORIZONTAL)
        
        self.l_s2 = tk.Label(self.stages_settings_canvas_frame, text="\nStage 2 (optional)\n", fg='red')
        
        self.l_s2_length = tk.Label(self.stages_settings_canvas_frame, text="S2 length")
        self.l_s2_diameter = tk.Label(self.stages_settings_canvas_frame, text="S2 diameter")
        self.l_s2_thurst = tk.Label(self.stages_settings_canvas_frame, text="S2 thurst")
        self.l_s2_lsp = tk.Label(self.stages_settings_canvas_frame, text="S2 lsp")
        self.l_s2_m0 = tk.Label(self.stages_settings_canvas_frame, text="S2 m0")
        self.l_s2_mp = tk.Label(self.stages_settings_canvas_frame, text="S2 mp")
        
        self.main_settings.pack(expand=True, fill=tk.BOTH)
        self.stages_settings_canvas.config(width=300, height=140)
        self.stages_settings_canvas.config(yscrollcommand=self.sroll_settings.set)
        self.stages_settings_canvas.pack()
        self.stages_settings.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.b_create.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)
        self.l_height.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        self.s_height.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        self.l_liftoff_mass.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        self.s_liftoff_mass.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        self.l_payload_mass.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        self.s_payload_mass.pack(padx=3, pady=0, expand=True, fill=tk.BOTH)
        
        self.l_s1.pack()
        
        self.l_s1_length.pack()
        self.s1_length.pack()
        self.l_s1_diameter.pack()
        self.s1_diameter.pack()
        self.l_s1_thurst.pack()
        self.s1_thurst.pack()
        self.l_s1_lsp.pack()
        self.s1_lsp.pack()
        self.l_s1_m0.pack()
        self.s1_m0.pack()
        self.l_s1_mp.pack()
        self.s1_mp.pack()
        
        self.l_s2.pack()
        
        self.l_s2_length.pack()
        self.s2_length.pack()
        self.l_s2_diameter.pack()
        self.s2_diameter.pack()
        self.l_s2_thurst.pack()
        self.s2_thurst.pack()
        self.l_s2_lsp.pack()
        self.s2_lsp.pack()
        self.l_s2_m0.pack()
        self.s2_m0.pack()
        self.l_s2_mp.pack()
        self.s2_mp.pack()

    ''' function that launch the GUI loop '''   
    def launch(self):
        self.window.mainloop()

    def exit_window_list(self):
        self.window_list.grab_release()
        self.window_list.destroy()
    
    ''' exit function of the pop-up window associoted to the button *Create* '''   
    def exit_create(self):
        name = self.e_name.get()
        info = [self.e_year.get(), self.e_country.get(), self.e_mission.get()]
        spec = [self.s_height.get(), self.s_liftoff_mass.get(), self.s_payload_mass.get(),
                self.s1_length.get(), self.s1_diameter.get(), self.s1_thurst.get(),
                self.s1_lsp.get(), self.s1_m0.get(), self.s1_mp.get(),
                self.s2_length.get(), self.s2_diameter.get(), self.s2_thurst.get(),
                self.s2_lsp.get(), self.s2_m0.get(), self.s2_mp.get()]
                
        if(main.rocket_consistence(name, info, spec)):
            self.drawer.add_rocket(name, info, spec)
            self.exit_window_list()
        else:
            self.svc.set("Inconsistent rocket, could not create")
            self.b_confirm.configure(text="Fermer", command=self.exit_window_list)

    ''' function called when *Create* button is clicked '''    
    def create(self):
        self.window_list = tk.Toplevel(self.window)
        self.window_list.resizable(False, False)
        self.window_list.grab_set()
        self.window_list.attributes('-topmost', 'true')
        
        buttons_frame = tk.Frame(self.window_list, width=300, height=300)
        
        self.svc = tk.StringVar()

        l_name = tk.Label(buttons_frame, text="Name")
        l_year = tk.Label(buttons_frame, text="Year")
        l_country = tk.Label(buttons_frame, text="Country")
        l_mission = tk.Label(buttons_frame, text="Mission")
        l_warning = tk.Label(buttons_frame, textvariable=self.svc, fg='red')
        
        self.e_name = tk.Entry(buttons_frame, fg = 'black', bg='white')
        self.e_year = tk.Entry(buttons_frame, fg = 'black', bg='white')
        self.e_country = tk.Entry(buttons_frame, fg = 'black', bg='white')
        self.e_mission = tk.Entry(buttons_frame, fg = 'black', bg='white')
        
        self.b_confirm = tk.Button(buttons_frame, text="Validate", command=self.exit_create)
        
        l_name.pack(padx=10, pady=5)
        self.e_name.pack(padx=10, pady=5)
        l_year.pack(padx=10, pady=5)
        self.e_year.pack(padx=10, pady=5)
        l_country.pack(padx=10, pady=5)
        self.e_country.pack(padx=10, pady=5)
        l_mission.pack(padx=10, pady=5)
        self.e_mission.pack(padx=10, pady=5)
        l_warning.pack()
        
        self.b_confirm.pack(padx=10, pady=20, expand=True, fill=tk.BOTH)
        buttons_frame.pack()
    
    ''' Function that list all the rocket in a csv file''' 
    def set_current(self):
        self.current_file = self.e_file.get()
        self.rl = main.load_rockets(self.current_file)
        if (self.rl == []):
            self.sv.set("File name does not exist !")
            self.list_rockets_loaded.delete(0,tk.END)
        else:
            names = main.get_names(self.rl)
            self.sv.set("")
            self.list_rockets_loaded.insert(tk.END, *names)
    
    ''' Function that select all the rocket in the popup associated to the button *Load* ''' 
    def select_all_rockets(self):
        self.list_rockets_loaded.selection_set(0,self.list_rockets_loaded.size() - 1)
    
    ''' Function that deselect all the rocket in the popup associated to the button *Load* '''   
    def deselect_all_rockets(self):
        self.list_rockets_loaded.selection_clear(0,self.list_rockets_loaded.size() - 1)

    ''' function called when *Load* button is clicked '''    
    def load(self):
        self.window_list = tk.Toplevel(self.window)
        self.window_list.resizable(False, False)
        self.list_rockets_loaded = tk.Listbox(self.window_list)
        self.list_rockets_loaded.grid(row=0, column=0, sticky="nsew")
        
        self.rl = main.load_rockets(self.current_file)
        names = main.get_names(self.rl)

        self.list_rockets_loaded.insert(tk.END, *names)
        
        buttons_frame = tk.Frame(self.window_list)
        self.e_file = tk.Entry(buttons_frame, fg = 'red', bg='blue')
        self.e_file.config(state='normal')
        self.e_file.delete(0, tk.END)
        self.e_file.insert(0, self.current_file)
        
        self.sv = tk.StringVar()
        
        b_select_all = tk.Button(buttons_frame, text="Select all", command=self.select_all_rockets)
        b_deselect = tk.Button(buttons_frame, text="Deselect", command=self.deselect_all_rockets)
        b_validate = tk.Button(buttons_frame, text="Validate", command=self.exit_load)
        b_modify = tk.Button(buttons_frame, text="Modify file", command=self.set_current)
        self.l_alert = tk.Label(buttons_frame, textvariable=self.sv, fg='red')
        
        b_select_all.grid(row=0, column=0, sticky="nsew")
        b_deselect.grid(row=0, column=1, sticky="nsew")
        self.e_file.grid(row=1, column=0, columnspan=2, sticky="nsew")
        b_modify.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.l_alert.grid(row=3, column=0, columnspan=2, sticky="nsew")
        b_validate.grid(row=4, column=0, columnspan=2, sticky="nsew")
        
        buttons_frame.grid(row=1, column=0, sticky="nsew")
        self.window_list.grab_set()
        self.window_list.attributes('-topmost', 'true')
        pass

    ''' exit function of the pop-up window associoted to the button *Load* '''   
    def exit_load(self):
        selection = self.list_rockets_loaded.curselection()
        rocket_list = [self.rl[i] for i in selection]
        self.drawer.load_rockets(rocket_list)
        self.drawer.draw()
        
        self.exit_window_list()
    
    ''' exit function of the pop-up window associoted to the button *Save all* '''   
    def exit_save_all(self):
        main.save_rockets(self.drawer.get_list(), self.current_file, True)
    
        self.exit_window_list()
        
    ''' exit function of the pop-up window associoted to the button *Save selected* '''      
    def exit_save_selected(self):
        main.save_rockets([self.drawer.get_selected()], self.current_file, False)
    
        self.exit_window_list()
        
    ''' function called when *Save* button is clicked '''    
    def save(self):
        self.window_list = tk.Toplevel(self.window)
        self.window_list.resizable(False, False)
        
        self.e_file = tk.Entry(self.window_list, fg = 'red', bg='blue')
        self.e_file.config(state='normal')
        self.e_file.delete(0, tk.END)
        self.e_file.insert(0, self.current_file)
        
        b_selected = tk.Button(self.window_list, text="Selected rocket", command=self.exit_save_selected)
        b_all = tk.Button(self.window_list, text="All rockets", command=self.exit_save_all)
        
        l_warning = tk.Label(self.window_list, text="File will be overwrited if all", fg='red')
        
        self.e_file.grid(row=0, column=0, columnspan=2, sticky="nsew")
        b_selected.grid(row=1, column=0, sticky="nsew")
        b_all.grid(row=1, column=1, sticky="nsew")
        l_warning.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        self.window_list.grab_set()
        self.window_list.attributes('-topmost', 'true')
        
    ''' exit function of the pop-up window associoted to the button *Erase all* '''
    def exit_erase_all(self):
        self.drawer.delete_all()
    
        self.exit_window_list()
        
    ''' exit function of the pop-up window associoted to the button *Erase selected* '''      
    def exit_erase_selected(self):
        self.drawer.delete_selected()
    
        self.exit_window_list()
      
    ''' function called when *Erase* button is clicked '''      
    def erase(self):
        self.window_list = tk.Toplevel(self.window)
        self.window_list.resizable(False, False)
        
        l_choice = tk.Label(self.window_list, text="Quoi effacer ?", fg='blue')
        b_selected = tk.Button(self.window_list, text="Selected rocket", command=self.exit_erase_selected)
        b_all = tk.Button(self.window_list, text="All rockets", command=self.exit_erase_all)
        
        l_choice.grid(row=0, column=0, columnspan=2, sticky="nsew")
        b_selected.grid(row=1, column=0, sticky="nsew")
        b_all.grid(row=1, column=1, sticky="nsew")
        
        self.window_list.grab_set()
        self.window_list.attributes('-topmost', 'true')
    
    ''' exit function of the pop-up window associoted to the button *Trajectory* '''      
    def exit_trajectory(self):
        try:
            rocket_trajectories.affichage_trajectoire(self.fs, float(self.e_angle.get()))
        except ValueError:
            pass
        self.exit_window_list()

    ''' function called when *Trajectory* button is clicked '''    
    def trajectory(self):
        if (self.drawer.get_selected() == None):
            return
        self.window_list = tk.Toplevel(self.window)
        self.window_list.resizable(False, False)
        rc = self.drawer.get_selected()
        self.fs = [rc.get_name()] + rc.get_info() + rc.get_spec()
        l_angle = tk.Label(self.window_list, text="Angle (in radian)", fg='blue')
        self.e_angle = tk.Entry(self.window_list, fg = 'red', bg='blue')
        self.e_angle .config(state='normal')
        
        b_selected = tk.Button(self.window_list, text="Draw trajectory", command=self.exit_trajectory)
        
        l_angle.pack()
        self.e_angle.pack()
        b_selected.pack()
        
        self.window_list.grab_set()
        self.window_list.attributes('-topmost', 'true')
        
    ''' function that check the keyboard event '''    
    def key_event(self, event):
        if(event.keycode == 114):
            self.drawer.select_next(1)
        if(event.keycode == 113):
            self.drawer.select_next(-1)
        if(event.keycode == 119):
            self.drawer.delete_selected()
    
    ''' function that check the mouse event '''    
    def mouse_event(self, event):
        self.drawer.mouse(event.x, event.y)
            


if __name__ == '__main__':
    interface = Interface()
    interface.launch()

