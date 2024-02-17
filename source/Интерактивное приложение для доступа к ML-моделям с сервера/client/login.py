import tkinter as tk
import customtkinter as ctk
import requests
from constants import SERVER_ADDRESS


class Login(ctk.CTkToplevel):

    def __init__(self, *args):
        params = iter(args)
        parent = next(params)
        parent_x = next(params)
        parent_y = next(params)

        super().__init__(parent)

        self.appearance_mode = parent.appearance_mode

        self.redirect_to_register = False
        self.redirect_to_models = False
        self.closed = False

        self.geometry(f"270x350+{parent_x}+{parent_y}")
        self.title("Вход")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.quit_me)

        self.data_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.data_frame.grid(row=0, column=0, pady=(40, 0))

        self.email_label = ctk.CTkLabel(master=self.data_frame, text="Email",
                                        font=("Merriweather", 15), width=80, height=40,)
        self.email_entry = ctk.CTkEntry(master=self.data_frame, width=150, height=40,)

        self.password_label = ctk.CTkLabel(master=self.data_frame, text="Пароль",
                                           font=("Merriweather", 15), width=80, height=40,)
        self.password_entry = ctk.CTkEntry(master=self.data_frame, width=150, height=40, show="*")

        self.email_label.grid(row=0, column=0, pady=10)
        self.email_entry.grid(row=0, column=1, pady=10)
        self.password_label.grid(row=1, column=0, sticky="n")
        self.password_entry.grid(row=1, column=1)

        self.login_button = ctk.CTkButton(master=self.data_frame, text="Войти",
                                          font=("Merriweather", 20, "bold"),
                                          width=150, height=40, command=self.send_data)
        self.login_button.grid(row=2, column=1, pady=10)

        self.not_registered_label = ctk.CTkLabel(master=self.data_frame, text="Ещё не зарегистрированы?",
                                           font=("Merriweather", 14), width=80, height=40,)
        self.redirect_to_register_button = ctk.CTkButton(master=self.data_frame, text="Зарегистрироваться",
                                          font=("Merriweather", 14, "bold"),
                                          width=100, height=25, command=self.redirect_to_register_command)
        
        self.not_registered_label.grid(row=4, column=0, columnspan=2, pady=(0, 0), sticky="e")
        self.redirect_to_register_button.grid(row=5, column=0, columnspan=2, pady=(0, 0), sticky="e")

        self.settings_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.settings_frame.grid(row=2, column=0, padx=10, pady=20)

        self.appearance_mode_label = ctk.CTkLabel(master=self.settings_frame, text="Тема:",
                                                  font=("Merriweather", 20, "bold"), width=80, height=40,)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master=self.settings_frame, values=["Light", "Dark", "System"],
                                                             font=("Merriweather", 20, "bold"), width=150, height=40,
                                                             command=self.change_appearance_mode_option)
        
        self.appearance_mode_label.grid(row=0, column=0)
        self.appearance_mode_option_menu.grid(row=0, column=1)

        self.appearance_mode_option_menu.set(self.appearance_mode)

    def change_appearance_mode_option(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        self.appearance_mode = new_appearance_mode
    
    def send_data(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = requests.post(f"{SERVER_ADDRESS}/login", auth=(email, password))
        print(response.text)
        print(response.json().keys())
        if "logged" in dict(response.json()).keys():
            self.redirect_to_models_command()
    
    def redirect_to_register_command(self):
        self.redirect_to_register = True
        self.quit_me()
    
    def redirect_to_models_command(self):
        self.redirect_to_models = True
        self.quit_me()
    
    def quit_me(self):
        self.closed = True
        self.quit()
        self.destroy()
