from view import Ventana
import customtkinter


class ControllerClass:
    def __init__(self, ventana):
        self.root_controller = ventana
        self.object_view = Ventana(self.root_controller)


if __name__ == "__main__":

    root_tk = customtkinter.CTk()
    miapp = ControllerClass(root_tk)
    root_tk.mainloop()
