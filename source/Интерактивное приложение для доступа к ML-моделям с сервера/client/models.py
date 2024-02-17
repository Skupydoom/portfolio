import tkinter as tk
import customtkinter as ctk
import requests


model1_test = {"name": "House pricing",
              "description": "This is a cool model that predicts price of the house according to the specified parameters, bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla. Dot.",
              "parameters": {"param1": "1",
                             "param2": "2",
                             "param3": "3",
                             "param4": "zbababadfg"}}

models_set = {"Not selected": {"name": "Not selected",
                               "description": "Please choose a model",
                               "parameters": "Please choose a model to see parameters"}, model1_test["name"]: model1_test}

for i in range(20):
    models_set[f"'unique' model number {i}"] = {"name": f"'unique' model number {i}",
                                                "description": f"unique description for model number {i}",
                                                "parameters": "some cool things"}

# print(models_set["'unique' model number 5"]["description"])
# for i in models_set:
#     print(models_set[i])

class Models(ctk.CTkToplevel):

    def __init__(self, *args):
        params = iter(args)
        parent = next(params)
        parent_x = next(params)
        parent_y = next(params)

        super().__init__(parent)

        self.appearance_mode = parent.appearance_mode

        self.closed = False
        self.chosen_model_var = ctk.StringVar(value="Not selected")

        self.geometry(f"650x400+{parent_x}+{parent_y}")
        self.title("MLModelsApp")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.quit_me)


        self.model_selection_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.model_selection_frame.grid(row=0, column=0, pady=(0, 10), sticky="n")

        self.model_selection_label = ctk.CTkLabel(master=self.model_selection_frame, text="Choose a model",
                                        font=("Merriweather", 15), width=80)
        self.model_selection_combobox = ctk.CTkComboBox(master=self.model_selection_frame,
                                                        values=[i for i in models_set.keys()],
                                                        command=self.model_selection_combobox_callback,
                                                        variable=self.chosen_model_var)
        
        self.model_selection_label.grid(row=0, column=0, padx=(0, 10))
        self.model_selection_combobox.grid(row=1, column=0, padx=10)
        


        self.model_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.model_frame.grid(row=0, column=1)

        self.model_description_label = ctk.CTkLabel(master=self.model_frame, fg_color="transparent", text="Model description:",
                                                    font=("Merriweather", 15), width=400)
        self.model_description_textbox = ctk.CTkTextbox(master=self.model_frame, fg_color="transparent", width=400, height=70,
                                                        state="disable")

        self.model_description_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(0, 10))
        self.model_description_textbox.grid(row=1, column=0, columnspan=2, pady=(0, 10))


        self.settings_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.settings_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(220, 0))

        self.appearance_mode_label = ctk.CTkLabel(master=self.settings_frame, text="Тема:",
                                                  font=("Merriweather", 20, "bold"), width=80, height=40,)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master=self.settings_frame, values=["Light", "Dark", "System"],
                                                             font=("Merriweather", 20, "bold"), width=150, height=40,
                                                             command=self.change_appearance_mode_option)
        
        self.appearance_mode_label.grid(row=0, column=0)
        self.appearance_mode_option_menu.grid(row=0, column=1)

        self.appearance_mode_option_menu.set(self.appearance_mode)
    
    def model_selection_combobox_callback(self, choice="Not selected"):
        print(choice)
        self.model_description_textbox.configure(state="normal")
        self.model_description_textbox.delete("0.0", "end")
        self.model_description_textbox.insert("0.0", models_set[choice]["description"])
        self.model_description_textbox.configure(state="disabled")

    def change_appearance_mode_option(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        self.appearance_mode = new_appearance_mode
    
    def quit_me(self):
        self.closed = True
        self.quit()
        self.destroy()
