import tkinter
from PIL import Image

import customtkinter


class App(customtkinter.CTk):
    """ The main application window """

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.geometry("400x550")
        self.title('Weather App')

        self.grid_columnconfigure((0, 1), weight=1)

        self.city_text = tkinter.StringVar()

        # city entry
        self.city_entry = customtkinter.CTkEntry(self, textvariable=self.city_text, width=325)
        self.city_entry.grid(row=1, column=0, padx=(20, 0), pady=20)

        # search button
        self.search_btn = customtkinter.CTkButton(self, text="Search", command=self.search_btn_callback)
        self.search_btn.grid(row=1, column=1, padx=(20, 20), pady=20)

        # location label
        self.location_lbl = customtkinter.CTkLabel(self, text='Location', font=('Bolt', 26))
        self.location_lbl.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), columnspan=2)

        # weather icon
        self.weather_img = customtkinter.CTkImage(Image.open('icons/01d.png'), size=(150, 150))
        self.image_label = customtkinter.CTkLabel(self, image=self.weather_img, text="")
        self.image_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), columnspan=2)

        # temperature label
        self.temperature_lbl = customtkinter.CTkLabel(self, text='Temperature', font=('italic', 16))
        self.temperature_lbl.grid(row=4, column=0, padx=(20, 20), pady=(20, 20), columnspan=2)

    def search_btn_callback(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
