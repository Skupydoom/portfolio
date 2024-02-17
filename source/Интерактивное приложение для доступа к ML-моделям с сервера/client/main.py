import tkinter as tk
import customtkinter as ctk
from login import Login
from register import Register
from models import Models


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.appearance_mode = "System"
        
        self.eval('tk::PlaceWindow . center')

        self.geometry("270x350")
        self.title("MLModelsApp")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.quit)

        self.main_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, padx=25, pady=30)

        self.btn_login = ctk.CTkButton(master=self.main_frame, text="Войти", width=220, height=100,
                                       font=("Merriweather", 20, "bold"),
                                       command=self.login)
        self.btn_register = ctk.CTkButton(master=self.main_frame, text="Зарегистрироваться", width=220, height=100,
                                          font=("Merriweather", 20, "bold"),
                                          command=self.register)
        
        self.btn_login.grid(row=0, column=0, pady=5)
        self.btn_register.grid(row=1, column=0)

        self.settings_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.settings_frame.grid(row=1, column=0, padx=20)

        self.appearance_mode_label = ctk.CTkLabel(master=self.settings_frame, text="Тема:",
                                                  font=("Merriweather", 20, "bold"), width=80, height=40,)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master=self.settings_frame, values=["Light", "Dark", "System"],
                                                             font=("Merriweather", 20, "bold"), width=150, height=40,
                                                             command=self.change_appearance_mode_option)
        
        self.appearance_mode_label.grid(row=0, column=0)
        self.appearance_mode_option_menu.grid(row=0, column=1)

        self.appearance_mode_option_menu.set(self.appearance_mode)

    def login(self):
        geo = self.geometry().split('+')
        x=geo[-2]
        y=geo[-1]

        login_window = Login(self, x, y)
        login_window.focus()
        login_window.attributes("-topmost", True)
        login_window.update()
        self.withdraw()
        login_window.mainloop()
        self.appearance_mode = login_window.appearance_mode_option_menu.get()

        if login_window.redirect_to_register:
            self.register()
        if login_window.redirect_to_models:
            self.models()
        if login_window.closed:
            self.quit()

    def register(self):
        geo = self.geometry().split('+')
        x=geo[-2]
        y=geo[-1]

        register_window = Register(self, x, y)
        register_window.focus()
        register_window.attributes("-topmost", True)
        register_window.update()
        self.withdraw()
        register_window.mainloop()
        self.appearance_mode = register_window.appearance_mode_option_menu.get()

        if register_window.redirect_to_login:
            self.login()
        if register_window.redirect_to_models:
            self.models()
        if register_window.closed:
            self.quit()
    
    def models(self):
        geo = self.geometry().split('+')
        x=geo[-2]
        y=geo[-1]

        models_window = Models(self, x, y)
        models_window.focus()
        models_window.attributes("-topmost", True)
        models_window.update()
        self.withdraw()
        models_window.mainloop()
        self.appearance_mode = models_window.appearance_mode_option_menu.get()

        if models_window.closed:
            self.quit()
    
    def change_appearance_mode_option(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        self.appearance_mode = new_appearance_mode


if __name__ == "__main__":
    app = App()
    app.mainloop()
