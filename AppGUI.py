
import customtkinter

from DatosCandidaturas import CANDIDATURAS


class AppGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.geometry("400x240")
        self.minsize(350,200)
        self.title("Elecciones 2023")

        button = customtkinter.CTkButton(self, text="Generar informes", command=self.button_click)
        self.grid_columnconfigure(0, weight=1)
        button.grid(row=0, column=0, padx=20, pady=20)

        self.opt_menu_var = customtkinter.StringVar(value=CANDIDATURAS[1])
        option_menu = customtkinter.CTkOptionMenu(self, values=CANDIDATURAS, command=self.option_menu_callback,
                                                  variable=self.opt_menu_var)
        self.grid_columnconfigure(1, weight=1)
        option_menu.grid(row=0, column=1, padx=20, pady=20)


    def option_menu_callback(self, choice):
        print("Partido elegido:", choice)

    def button_click(self):
        print("Generando informes por Provincia y Municipios", self.opt_menu_var.get())


app = AppGUI()
app.mainloop()
