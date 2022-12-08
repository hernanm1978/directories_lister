"""
A simple Folders and Files counter. The output file (Directory_Lister.txt)
will show the folders, subfolders and files names, also the number of files
in each folder.

"""
import customtkinter
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning
from tkinter import CENTER
import os
import threading
from datetime import datetime


class DirectoriesLister:

    def __init__(self, window):

        self.__root_tk = window
        self.__path_in = customtkinter.StringVar()
        self.__path_out = customtkinter.StringVar()
        self.__amount_files = customtkinter.StringVar()
        self.__amount_folders = customtkinter.StringVar()
        self.__BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        self.__ruta = os.path.join(self.__BASE_DIR)

        # Config TK

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        # root_tk.eval('tk::PlaceWindow . center')
        self.__root_tk.geometry("450x220")
        self.__root_tk.title("HM-NET | Directory Lister")
        self.__root_tk.resizable(False, False)
        self.__root_tk.iconbitmap(self.__ruta+"\\icono.ico")

        # labels

        label1 = customtkinter.CTkLabel(master=self.__root_tk,
                                        text="Files :",
                                        width=120,
                                        height=25,
                                        corner_radius=8)

        label1.place(relx=0.10, rely=0.55, anchor=CENTER)

        label2 = customtkinter.CTkLabel(master=self.__root_tk,
                                        text="Folders :",
                                        width=120,
                                        height=25,
                                        corner_radius=8)
        label2.place(relx=0.55, rely=0.55, anchor=CENTER)

        # Entries

        fst_entry = customtkinter.CTkEntry(master=self.__root_tk,
                                           width=300,
                                           height=30,
                                           corner_radius=10,
                                           textvariable=self.__path_in)

        fst_entry.place(relx=0.38, rely=0.15, anchor=CENTER)

        second_entry = customtkinter.CTkEntry(master=self.__root_tk,
                                              width=300,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=self.__path_out)

        second_entry.place(relx=0.38, rely=0.35, anchor=CENTER)

        third_entry = customtkinter.CTkEntry(master=self.__root_tk,
                                             width=80,
                                             height=30,
                                             corner_radius=10,
                                             textvariable=self.__amount_files,
                                             state="disabled")

        third_entry.place(relx=0.28, rely=0.55, anchor=CENTER)

        fourth_entry = customtkinter.CTkEntry(master=self.__root_tk,
                                              width=80,
                                              height=30,
                                              corner_radius=10,
                                              textvariable=self.__amount_folders,
                                              state="disabled")

        fourth_entry.place(relx=0.75, rely=0.55, anchor=CENTER)

        # Progress Bar

        progressbar = customtkinter.CTkProgressBar(master=self.__root_tk,
                                                   width=160,
                                                   height=10,
                                                   border_width=1,
                                                   mode='determinate',
                                                   indeterminate_speed=10,
                                                   determinate_speed=10)
        progressbar.place(relx=0.5, rely=0.7, anchor=CENTER)

        progressbar.set(0)

        # Botones

        button = customtkinter.CTkButton(master=self.__root_tk,
                                         corner_radius=15,
                                         width=80,
                                         height=25,
                                         # borderwidth=0,
                                         text="Source Dir",
                                         hover=True,
                                         command=lambda: self.__seleccion_dir())
        button.place(relx=0.85, rely=0.15, anchor=CENTER)

        button2 = customtkinter.CTkButton(master=self.__root_tk,
                                          corner_radius=15,
                                          width=80,
                                          height=25,
                                          # borderwidth=0,
                                          text="Target Dir",
                                          hover=True,
                                          command=lambda: self.__seleccion_dir(1))
        button2.place(relx=0.85, rely=0.35, anchor=CENTER)

        button3 = customtkinter.CTkButton(master=self.__root_tk,
                                          corner_radius=15,
                                          width=150,
                                          height=25,
                                          # borderwidth=0,
                                          text="List Directories",
                                          hover=True,
                                          command=lambda: self.__listar_dirs(progressbar))
        button3.place(relx=0.5, rely=0.85, anchor=CENTER)

    def __seleccion_dir(self, opc=None):

        if not opc:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            self.__path_in.set(ruta_normalizada)
        else:
            ruta_sel = askdirectory()
            ruta_normalizada = os.path.abspath(ruta_sel)
            self.__path_out.set(ruta_normalizada)

    def __listar_dirs(self, progressbar):

        self.__amount_folders.set("0")
        self.__amount_folders.set("0")

        def __listar_dirs2():
            rootdir = self.__path_in.get()
            # handler = open(ruta_out.get() + "/Directory_Lister.txt", "a", encoding="utf-8")
            lista = [carpeta for carpeta in os.walk(rootdir)]
            ficheros_cont = 0
            with open(self.__path_out.get() + "/Directory_Lister.txt", "a", encoding="utf-8") as f:
                progressbar.start()

                for carpeta in os.walk(rootdir):
                    a = f'\nIn Folder "{carpeta[0]}" Are {len(carpeta[2])} Files:'
                    b = "-" * 80 + "\n"
                    f.write(str(a) + "\n" + b)
                    self.__amount_folders.set(str(len(lista)))

                    for fichero in carpeta[2]:
                        b = f' ---> {fichero}'
                        ficheros_cont += 1
                        f.write(str(b) + "\n")
                        self.__amount_files.set(str(ficheros_cont))

                report = "*" * 80 + "\n" + f"{ficheros_cont} Files Found In {len(lista)} Folders."
                f.write(report + "\n")
                progressbar.stop()
                progressbar.set(100)

        if self.__path_in.get() and self.__path_out.get() != "":
            time_ahora = datetime.now()
            dir_in_var = "-" * 80 + "\nfolder to analyze:\n".title() + self.__path_in.get() + "\n"
            dir_out_var = "report target folder:\n".title() + self.__path_out.get() + "\n" + "-" * 80 + "\n" + str(
                time_ahora) + "\n" + "-" * 80
            with open(self.__path_out.get() + "/Directory_Lister.txt", "w", encoding="utf-8") as ff:
                # handler = open(ruta_out.get() + "/Directory_Lister.txt", "w", encoding="utf-8")
                ff.write(dir_in_var + "\n" + dir_out_var + "\n")
                threading.Thread(target=__listar_dirs2).start()

        else:
            showwarning("Error in Directories selection".title(),
                        message="source and taget must be selected before execution !".title())


if __name__ == "__main__":

    root_tk = customtkinter.CTk()
    app = DirectoriesLister(root_tk)
    root_tk.mainloop()
