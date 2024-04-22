import tkinter
from PIL import Image

import customtkinter

from weather import Weather
from weather_api import WeatherAPI


class App(customtkinter.CTk):
    """ The main application window """

    def __init__(self):
        self.weather = None
        self.weather_api = WeatherAPI()

        super().__init__()

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.geometry("400x550")
        self.title('Weather App')

        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure((0, 0), weight=0)

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
        self.image_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), columnspan=2)

        # weather description label
        self.weather_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 18))
        self.weather_lbl.grid(row=4, column=0, padx=(20, 20), pady=(0, 0), columnspan=2)

        # temperature label
        self.temperature_lbl = customtkinter.CTkLabel(self, text='', font=('italic', 21))
        self.temperature_lbl.grid(row=5, column=0, padx=(20, 20), pady=(20, 10), columnspan=2)

        # feels like label
        self.feels_like_lbl = customtkinter.CTkLabel(self, text='', font=('italic', 15))
        self.feels_like_lbl.grid(row=6, column=0, padx=(25, 25), pady=(0, 0), columnspan=1, sticky=tkinter.E)
        self.feels_like_value_lbl = customtkinter.CTkLabel(self, text='', font=('italic', 15))
        self.feels_like_value_lbl.grid(row=6, column=1, padx=(0, 0), pady=(0, 0), columnspan=1,sticky='w')

    def search_btn_callback(self):
        self.city_text.set(self.city_entry.get())
        self.weather_request()

    def update_weather_labels(self):
        self.location_lbl.configure(text=self.city_entry.get())
        self.temperature_lbl.configure(text=str(self.weather.temp) + ' ℃')
        new_icon = customtkinter.CTkImage(Image.open(f'icons/{self.weather.weather['icon']}.png'), size=(150, 150))
        self.image_label.configure(image=new_icon)
        self.weather_lbl.configure(text=self.weather.weather['description'].title())
        self.feels_like_lbl.configure(text='Feels like:')
        self.feels_like_value_lbl.configure(text=str(self.weather.feels_like) + ' ℃')

    def weather_request(self):
        weather_response = self.weather_api.get(self.city_text.get())
        if weather_response:
            self.weather = Weather(weather_response)
            self.update_weather_labels()
        else:
            self.location_lbl.configure(text='non response')
            # self.weather = Weather_MockUp()
            pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
