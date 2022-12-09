import os
import threading
from tkinter.messagebox import showwarning
from tkinter.filedialog import askdirectory
from datetime import datetime


class Modelo:

    # Funciones

    @staticmethod
    def seleccion_dir(rutain, rutaout, opc=None):

        if not opc:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            rutain.set(ruta_normalizada)
        else:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            rutaout.set(ruta_normalizada)

    @staticmethod
    def listar_dirs(cantdirs, cantarchs, rutain, rutaout, pbar):

        cantdirs = cantdirs
        cantdirs.set("0")
        cantarch = cantarchs
        cantarch.set("0")
        root_in = rutain.get()
        rootdir = root_in
        root_out = rutaout.get()
        progressbar = pbar

        def listar_dirs2():

            progressbar.start()
            ficheros_cont = 0
            carpetas_cont = 0
            with open(root_out + "/Directory_Lister.txt", "a", encoding="utf-8") as f:
                for carpeta in os.walk(rootdir):
                    a = f'\nEn Carpeta "{carpeta[0]}" Hay {len(carpeta[2])} Archivos:'
                    b = "-" * 50 + "\n"
                    carpetas_cont += 1
                    f.write(str(a) + "\n" + b)
                    cantdirs.set(str(carpetas_cont))

                    for fichero in carpeta[2]:
                        b = f' ---> {fichero}'
                        ficheros_cont += 1
                        f.write(str(b) + "\n")
                        cantarch.set(str(ficheros_cont))

                report = "*" * 80 + "\n" + f"{ficheros_cont} archivos encontrados en {carpetas_cont} carpetas."
                f.write(report + "\n")
                progressbar.stop()
                progressbar.set(100)

        if root_in and root_out != "":
            time_ahora = datetime.now()
            dir_in_var = "-"*80 + "\nCarpeta a analizar:\n".title() + root_in + "\n"
            dir_out_var = "carpeta destino reporte:\n".title() + root_out + "\n" + "-" * 80 + "\n" + str(time_ahora)\
                          + "\n" + "-" * 80
            with open(root_out + "/Directory_Lister.txt", "w", encoding="utf-8") as ff:
                ff.write(dir_in_var + "\n" + dir_out_var + "\n")
                threading.Thread(target=listar_dirs2).start()

        else:
            showwarning("Error en seleccion de directorios".title(),
                        message="deben seleccionarse tanto el directorio source como el target antes de la "
                                "ejecucion !".title())
