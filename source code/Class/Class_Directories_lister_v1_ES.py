"""
HM-NET Directory Lister es un simple contador de carpetas, subcarpetas y archivos,
El conteo puede verse directamente en la interfaz, adicionalmente se creara un
archivo txt (Directory_Lister.txt) donde se registraran todas las rutas con sus nombres
de carpetas, nombres de archivos contenidos en ellas y conteos de archivos por carpeta
y totales.
"""

import customtkinter
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning
from tkinter import CENTER
import os
import threading
from datetime import datetime


class DirectoriesLister:
    def __init__(self, ventana, path):

        # Variables atr inst
        self.root_tk = ventana
        self.__ruta_in = customtkinter.StringVar()
        self.__ruta_out = customtkinter.StringVar()
        self.__cant_arch = customtkinter.StringVar()
        self.__cant_dirs = customtkinter.StringVar()
        self.__ruta = path

        # Config TK

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        # root_tk.eval('tk::PlaceWindow . center')
        self.root_tk.geometry("450x220")
        self.root_tk.title("HM-NET | Directory Lister")
        self.root_tk.resizable(False, False)
        self.root_tk.iconbitmap(self.__ruta + "\\icono.ico")

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
                                           textvariable=self.__ruta_in)

        fst_entry.place(relx=0.38, rely=0.15, anchor=CENTER)

        second_entry = customtkinter.CTkEntry(master=self.root_tk,
                                              width=300,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=self.__ruta_out)

        second_entry.place(relx=0.38, rely=0.35, anchor=CENTER)

        third_entry = customtkinter.CTkEntry(master=self.root_tk,
                                             width=80,
                                             height=30,
                                             corner_radius=10,
                                             textvariable=self.__cant_arch,
                                             state="disabled")

        third_entry.place(relx=0.28, rely=0.55, anchor=CENTER)

        fourth_entry = customtkinter.CTkEntry(master=self.root_tk,
                                              width=80,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=self.__cant_dirs,
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

        button = customtkinter.CTkButton(master=root_tk,
                                         corner_radius=15,
                                         width=80,
                                         height=25,
                                         # borderwidth=0,
                                         text="Source Dir",
                                         hover=True,
                                         command=lambda: self.__seleccion_dir())
        button.place(relx=0.85, rely=0.15, anchor=CENTER)

        button2 = customtkinter.CTkButton(master=root_tk,
                                          corner_radius=15,
                                          width=80,
                                          height=25,
                                          # borderwidth=0,
                                          text="Target Dir",
                                          hover=True,
                                          command=lambda: self.__seleccion_dir(1))
        button2.place(relx=0.85, rely=0.35, anchor=CENTER)

        button3 = customtkinter.CTkButton(master=root_tk,
                                          corner_radius=15,
                                          width=150,
                                          height=25,
                                          # borderwidth=0,
                                          text="Listar Directorios",
                                          hover=True,
                                          command=lambda: self.__listar_dirs(progressbar))
        button3.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Funciones

    def __seleccion_dir(self, opc=None):

        if not opc:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            self.__ruta_in.set(ruta_normalizada)
        else:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            self.__ruta_out.set(ruta_normalizada)

    def __listar_dirs(self, progressbar):

        self.__cant_dirs.set("0")
        self.__cant_arch.set("0")

        def listar_dirs2():

            rootdir = self.__ruta_in.get()
            lista = [carpeta for carpeta in os.walk(rootdir)]
            ficheros_cont = 0
            with open(self.__ruta_out.get() + "/Directory_Lister.txt", "a", encoding="utf-8") as f:
                progressbar.start()

                for carpeta in os.walk(rootdir):
                    a = f'\nEn Carpeta "{carpeta[0]}" Hay {len(carpeta[2])} Archivos:'
                    b = "-" * 50 + "\n"
                    f.write(str(a) + "\n" + b)
                    self.__cant_dirs.set(str(len(lista)))

                    for fichero in carpeta[2]:
                        b = f' ---> {fichero}'
                        ficheros_cont += 1
                        f.write(str(b) + "\n")
                        self.__cant_arch.set(str(ficheros_cont))

                report = "*" * 80 + "\n" + f"{ficheros_cont} archivos encontrados en {len(lista)} carpetas."
                f.write(report + "\n")
                progressbar.stop()
                progressbar.set(100)

        if self.__ruta_in.get() and self.__ruta_out.get() != "":
            time_ahora = datetime.now()
            dir_in_var = "-" * 80 + "\nCarpeta a analizar:\n".title() + self.__ruta_in.get() + "\n"
            dir_out_var = "carpeta destino reporte:\n".title() + self.__ruta_out.get() + "\n" + "-" * 80 + "\n" + str(
                time_ahora) + "\n" + "-" * 80
            with open(self.__ruta_out.get() + "/Directory_Lister.txt", "w", encoding="utf-8") as ff:
                ff.write(dir_in_var + "\n" + dir_out_var + "\n")
                threading.Thread(target=listar_dirs2).start()

        else:
            showwarning("Error en seleccion de directorios".title(),
                        message="deben seleccionarse tanto el directorio source como el target antes de la "
                                "ejecucion !".title())


if __name__ == "__main__":

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR)
    root_tk = customtkinter.CTk()
    app = DirectoriesLister(root_tk, ruta)
    root_tk.mainloop()
