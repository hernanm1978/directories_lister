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

root_tk = customtkinter.CTk()

# Variables

ruta_in = customtkinter.StringVar()
ruta_out = customtkinter.StringVar()
cant_arch = customtkinter.StringVar()
cant_dirs = customtkinter.StringVar()

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR)


# Config TK

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# root_tk.eval('tk::PlaceWindow . center')
root_tk.geometry("450x220")
root_tk.title("HM-NET | Directory Lister")
root_tk.resizable(False, False)
root_tk.iconbitmap(ruta+"\\icono.ico")


# labels

label1 = customtkinter.CTkLabel(master=root_tk,
                                text="Archivos:",
                                width=120,
                                height=25,
                                corner_radius=8)

label1.place(relx=0.10, rely=0.55, anchor=CENTER)

label2 = customtkinter.CTkLabel(master=root_tk,
                                text="Carpetas:",
                                width=120,
                                height=25,
                                corner_radius=8)
label2.place(relx=0.55, rely=0.55, anchor=CENTER)


# Entries

fst_entry = customtkinter.CTkEntry(master=root_tk,
                                   width=300,
                                   height=30,
                                   corner_radius=10,
                                   textvariable=ruta_in)

fst_entry.place(relx=0.38, rely=0.15, anchor=CENTER)

second_entry = customtkinter.CTkEntry(master=root_tk,
                                      width=300,
                                      height=30,
                                      corner_radius=10,
                                      textvariable=ruta_out)

second_entry.place(relx=0.38, rely=0.35, anchor=CENTER)

third_entry = customtkinter.CTkEntry(master=root_tk,
                                     width=80,
                                     height=30,
                                     corner_radius=10,
                                     textvariable=cant_arch,
                                     state="disabled")

third_entry.place(relx=0.28, rely=0.55, anchor=CENTER)

fourth_entry = customtkinter.CTkEntry(master=root_tk,
                                      width=80,
                                      height=30,
                                      corner_radius=10,
                                      textvariable=cant_dirs,
                                      state="disabled")

fourth_entry.place(relx=0.75, rely=0.55, anchor=CENTER)


# Progress Bar

progressbar = customtkinter.CTkProgressBar(master=root_tk,
                                           width=160,
                                           height=10,
                                           border_width=1,
                                           mode='determinate',
                                           indeterminate_speed=10,
                                           determinate_speed=10)
progressbar.place(relx=0.5, rely=0.7, anchor=CENTER)

progressbar.set(0)


# Funciones


def seleccion_dir(opc=None):
    global ruta_in
    global ruta_out
    if not opc:
        ruta_sel = askdirectory()
        ruta_normalizada = os.path.abspath(ruta_sel)
        ruta_in.set(ruta_normalizada)
    else:
        ruta_sel = askdirectory()
        ruta_normalizada = os.path.abspath(ruta_sel)
        ruta_out.set(ruta_normalizada)


def listar_dirs():

    global cant_arch
    global cant_dirs
    cant_dirs.set("0")
    cant_arch.set("0")

    def listar_dirs2():

        rootdir = ruta_in.get()
        # handler = open(ruta_out.get() + "/Directory_Lister.txt", "a", encoding="utf-8")
        lista = [carpeta for carpeta in os.walk(rootdir)]
        ficheros_cont = 0
        with open(ruta_out.get() + "/Directory_Lister.txt", "a", encoding="utf-8") as f:
            progressbar.start()

            for carpeta in os.walk(rootdir):
                a = f'\nEn Carpeta "{carpeta[0]}" Hay {len(carpeta[2])} Archivos:'
                b = "-" * 50 + "\n"
                f.write(str(a) + "\n" + b)
                cant_dirs.set(str(len(lista)))

                for fichero in carpeta[2]:
                    b = f' ---> {fichero}'
                    ficheros_cont += 1
                    f.write(str(b) + "\n")
                    cant_arch.set(str(ficheros_cont))

            report = "*" * 80 + "\n" + f"{ficheros_cont} archivos encontrados en {len(lista)} carpetas."
            f.write(report + "\n")
            progressbar.stop()
            progressbar.set(100)

    if ruta_in.get() and ruta_out.get() != "":
        time_ahora = datetime.now()
        dir_in_var = "-"*80 + "\nCarpeta a analizar:\n".title() + ruta_in.get() + "\n"
        dir_out_var = "carpeta destino reporte:\n".title() + ruta_out.get() + "\n" + "-" * 80 + "\n" + \
                      str(time_ahora) + "\n" + "-" * 80
        with open(ruta_out.get() + "/Directory_Lister.txt", "w", encoding="utf-8") as ff:
            ff.write(dir_in_var + "\n" + dir_out_var + "\n")
            threading.Thread(target=listar_dirs2).start()

    else:
        showwarning("Error en seleccion de directorios".title(),
                    message="deben seleccionarse tanto el directorio source como el target antes de la "
                            "ejecucion !".title())


# Botones

button = customtkinter.CTkButton(master=root_tk,
                                 corner_radius=15,
                                 width=80,
                                 height=25,
                                 # borderwidth=0,
                                 text="Source Dir",
                                 hover=True,
                                 command=lambda: seleccion_dir())
button.place(relx=0.85, rely=0.15, anchor=CENTER)

button2 = customtkinter.CTkButton(master=root_tk,
                                  corner_radius=15,
                                  width=80,
                                  height=25,
                                  # borderwidth=0,
                                  text="Target Dir",
                                  hover=True,
                                  command=lambda: seleccion_dir(1))
button2.place(relx=0.85, rely=0.35, anchor=CENTER)


button3 = customtkinter.CTkButton(master=root_tk,
                                  corner_radius=15,
                                  width=150,
                                  height=25,
                                  # borderwidth=0,
                                  text="Listar Directorios",
                                  hover=True,
                                  command=lambda: listar_dirs())
button3.place(relx=0.5, rely=0.85, anchor=CENTER)


root_tk.mainloop()
