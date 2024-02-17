import tkinter as tk
import customtkinter as ctk
import requests
from constants import SERVER_ADDRESS


class Register(ctk.CTkToplevel):

    def __init__(self, *args):
        params = iter(args)
        parent = next(params)
        parent_x = next(params)
        parent_y = next(params)

        super().__init__(parent)

        self.appearance_mode = parent.appearance_mode

        self.redirect_to_login = False
        self.redirect_to_models = False
        self.closed = False

        self.geometry(f"300x350+{parent_x}+{parent_y}")
        self.title("Регистрация")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.quit_me)

        self.data_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.data_frame.grid(row=0, column=0, pady=(0, 0))

        self.email_label = ctk.CTkLabel(master=self.data_frame, text="Email",
                                        font=("Merriweather", 15), width=80, height=40,
                                        anchor="e")
        self.email_entry = ctk.CTkEntry(master=self.data_frame, width=150, height=40,)

        self.password_label = ctk.CTkLabel(master=self.data_frame, text="Пароль",
                                           font=("Merriweather", 15), width=80, height=40,
                                           anchor="e")
        self.password_entry = ctk.CTkEntry(master=self.data_frame, width=150, height=40, show="*")

        self.confirm_password_label = ctk.CTkLabel(master=self.data_frame, text="Повтор пароля",
                                           font=("Merriweather", 15), width=80, height=40,
                                           anchor="e")
        self.confirm_password_entry = ctk.CTkEntry(master=self.data_frame, width=150, height=40, show="*")

        self.email_label.grid(row=0, column=0, padx=(20, 5), pady=(10, 10))
        self.email_entry.grid(row=0, column=1, padx=(5, 20), pady=(15, 10))
        self.password_label.grid(row=1, column=0, padx=(20, 5), pady=(0, 10))
        self.password_entry.grid(row=1, column=1, padx=(5, 20), pady=(0, 10))
        self.confirm_password_label.grid(row=2, column=0, padx=(20, 5))
        self.confirm_password_entry.grid(row=2, column=1, padx=(5, 20))

        self.register_button = ctk.CTkButton(master=self.data_frame, text="Зарегистрироваться",
                                          font=("Merriweather", 20, "bold"),
                                          width=150, height=40, command=self.send_data)
        self.register_button.grid(row=3, columnspan=2, pady=(15, 0), padx=(45, 0))

        self.registered_label = ctk.CTkLabel(master=self.data_frame, text="Уже Есть аккаунт?",
                                           font=("Merriweather", 14), width=80, height=40,)
        self.redirect_to_login_button = ctk.CTkButton(master=self.data_frame, text="Войти",
                                          font=("Merriweather", 14, "bold"),
                                          width=100, height=25, command=self.redirect_to_login_command)
        
        self.registered_label.grid(row=4, column=0, columnspan=2, padx=21, pady=(0, 0), sticky="e")
        self.redirect_to_login_button.grid(row=5, column=0, columnspan=2, padx=21, pady=(0, 0), sticky="e")


        self.settings_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.settings_frame.grid(row=2, column=0, padx=10, pady=10)

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
        confirm_password = self.confirm_password_entry.get()
        entire_password = password + confirm_password

        response = requests.post(f"{SERVER_ADDRESS}/register", auth=(email, entire_password))
        print(response.text)
        if "registered" in response.json().keys():
            self.redirect_to_models_command()
    
    def redirect_to_login_command(self):
        self.redirect_to_login = True
        self.quit_me()
    
    def redirect_to_models_command(self):
        self.redirect_to_models = True
        self.quit_me()
    
    def quit_me(self):
        self.closed = True
        self.quit()
        self.destroy()
