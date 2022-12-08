import customtkinter
import os
from tkinter import CENTER
from model import Modelo


class Ventana:
    def __init__(self, ventana_root):
        self.root_tk = ventana_root
    
    # Config TK

        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        ruta = os.path.join(BASE_DIR)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        # root_tk.eval('tk::PlaceWindow . center')
        self.root_tk.geometry("450x220")
        self.root_tk.title("HM-NET | Directory Lister")
        self.root_tk.resizable(False, False)
        self.root_tk.iconbitmap(ruta+"\\icono.ico")
        self.object1 = Modelo()

        # Variables

        ruta_in = customtkinter.StringVar()
        ruta_out = customtkinter.StringVar()
        cant_arch = customtkinter.StringVar()
        cant_dirs = customtkinter.StringVar()

        # labels

        label1 = customtkinter.CTkLabel(master=self.root_tk,
                                        text="Archivos:",
                                        width=120,
                                        height=25,
                                        corner_radius=8)

        label1.place(relx=0.10, rely=0.55, anchor=CENTER)

        label2 = customtkinter.CTkLabel(master=self.root_tk,
                                        text="Carpetas:",
                                        width=120,
                                        height=25,
                                        corner_radius=8)
        label2.place(relx=0.55, rely=0.55, anchor=CENTER)

        # Entries

        fst_entry = customtkinter.CTkEntry(master=self.root_tk,
                                           width=300,
                                           height=30,
                                           corner_radius=10,
                                           textvariable=ruta_in)

        fst_entry.place(relx=0.38, rely=0.15, anchor=CENTER)

        second_entry = customtkinter.CTkEntry(master=self.root_tk,
                                              width=300,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=ruta_out)

        second_entry.place(relx=0.38, rely=0.35, anchor=CENTER)

        third_entry = customtkinter.CTkEntry(master=self.root_tk,
                                             width=80,
                                             height=30,
                                             corner_radius=10,
                                             textvariable=cant_arch,
                                             state="disabled")

        third_entry.place(relx=0.28, rely=0.55, anchor=CENTER)

        fourth_entry = customtkinter.CTkEntry(master=self.root_tk,
                                              width=80,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=cant_dirs,
                                              state="disabled")

        fourth_entry.place(relx=0.75, rely=0.55, anchor=CENTER)

        # Progress Bar

        progressbar = customtkinter.CTkProgressBar(master=self.root_tk,
                                                   width=160,
                                                   height=10,
                                                   border_width=1,
                                                   mode='determinate',
                                                   indeterminate_speed=10,
                                                   determinate_speed=10)
        progressbar.place(relx=0.5, rely=0.7, anchor=CENTER)

        progressbar.set(0)

        # Botones

        button = customtkinter.CTkButton(master=self.root_tk,
                                         corner_radius=15,
                                         width=80,
                                         height=25,
                                         # borderwidth=0,
                                         text="Source Dir",
                                         hover=True,
                                         command=lambda: self.object1.seleccion_dir(ruta_in, ruta_out))
        button.place(relx=0.85, rely=0.15, anchor=CENTER)

        button2 = customtkinter.CTkButton(master=self.root_tk,
                                          corner_radius=15,
                                          width=80,
                                          height=25,
                                          # borderwidth=0,
                                          text="Target Dir",
                                          hover=True,
                                          command=lambda: self.object1.seleccion_dir(ruta_in, ruta_out, 1))
        button2.place(relx=0.85, rely=0.35, anchor=CENTER)

        button3 = customtkinter.CTkButton(master=self.root_tk,
                                          corner_radius=15,
                                          width=150,
                                          height=25,
                                          # borderwidth=0,
                                          text="Listar Directorios",
                                          hover=True,
                                          command=lambda: self.object1.listar_dirs(cant_dirs, cant_arch, ruta_in,
                                                                                   ruta_out, progressbar))
        button3.place(relx=0.5, rely=0.85, anchor=CENTER)
