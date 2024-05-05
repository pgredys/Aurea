import tkinter

import customtkinter
from PIL import Image

from src.forecast_api import ForecastAPI
from src.weather import Weather
from src.weather_api import WeatherAPI


class App(customtkinter.CTk):
    """ The main application window """

    def __init__(self):
        self.weather_response = None
        self.weather = None
        self.weather_api = WeatherAPI()
        self.forecast_api = ForecastAPI()

        super().__init__()

        self.canvas = tkinter.Canvas(self)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('./themes/orange.json')
 
        self.geometry("400x840")
        self.title('Aurëa')
        self.resizable(False, False)

        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure((0, 0), weight=0)

        self.scrollable_frame = None
        self.city_text = customtkinter.StringVar()

        # city entry
        self.city_entry = customtkinter.CTkEntry(self, textvariable=self.city_text, width=325)
        self.city_entry.grid(row=1, column=0, padx=(20, 0), pady=20)

        # search button
        self.search_btn = customtkinter.CTkButton(self, text="Search", command=self.search_btn_callback)
        self.search_btn.grid(row=1, column=1, padx=(20, 20), pady=20)

        # location label
        self.location_lbl = customtkinter.CTkLabel(self, text='Location', font=('Bolt', 26))
        self.location_lbl.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), columnspan=2)

        # weather icon
        self.weather_img = customtkinter.CTkImage(Image.open('icons/01d.png'), size=(150, 150))
        self.image_label = customtkinter.CTkLabel(self, image=self.weather_img, text="")
        self.image_label.grid(row=3, column=0, padx=(20, 20), pady=(0, 0), columnspan=2)

        # weather description label
        self.weather_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 18))
        self.weather_lbl.grid(row=4, column=0, padx=(20, 20), pady=(0, 0), columnspan=2)

        # temperature label
        self.temperature_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 21))
        self.temperature_lbl.grid(row=5, column=0, padx=(20, 20), pady=(20, 20), columnspan=2)

        # feels like temp label
        self.feels_like_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.feels_like_lbl.grid(row=6, column=0, padx=(100, 45), pady=(0, 0), columnspan=1, sticky=tkinter.N)
        self.feels_like_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.feels_like_value_lbl.grid(row=6, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

        # pressure label
        self.pressure_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.pressure_lbl.grid(row=7, column=0, padx=(100, 45), pady=(0, 0), columnspan=1, sticky=tkinter.N)
        self.pressure_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.pressure_value_lbl.grid(row=7, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

        # pressure label
        self.humidity_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.humidity_lbl.grid(row=8, column=0, padx=(100, 45), pady=(0, 0), columnspan=1, sticky=tkinter.N)
        self.humidity_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.humidity_value_lbl.grid(row=8, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

        # wind label
        self.wind_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.wind_lbl.grid(row=9, column=0, padx=(100, 52), pady=(0, 0), columnspan=1, sticky=tkinter.E)
        self.wind_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.wind_value_lbl.grid(row=9, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

        # clouds label
        self.clouds_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.clouds_lbl.grid(row=10, column=0, padx=(100, 52), pady=(0, 0), columnspan=1, sticky=tkinter.E)
        self.clouds_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.clouds_value_lbl.grid(row=10, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

        # sun label
        self.sun_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.sun_lbl.grid(row=11, column=0, padx=(100, 52), pady=(0, 0), columnspan=1, sticky=tkinter.E)
        self.sun_value_lbl = customtkinter.CTkLabel(self, text='', font=('Bolt', 15))
        self.sun_value_lbl.grid(row=11, column=1, padx=(0, 0), pady=(0, 0), columnspan=1, sticky='w')

    def search_btn_callback(self):
        self.city_text.set(self.city_entry.get())
        self.weather_request()

        if self.scrollable_frame:
            self.scrollable_frame.grid_forget()

        if self.weather_response['cod'] == 200:
            self.forecast_request()

    def update_weather_labels(self):
        self.location_lbl.configure(text=self.city_entry.get())
        self.temperature_lbl.configure(text=str(self.weather.temp) + ' ℃')

        icon_img = Image.open(f'icons/{self.weather.weather['icon']}.png')
        new_icon = customtkinter.CTkImage(dark_image=icon_img,
                                          light_image=icon_img.point(lambda p: p - 45 if p > 45 else p),
                                          size=(150, 150))
        self.image_label.configure(image=new_icon)
        self.weather_lbl.configure(text=self.weather.weather['description'].title())

        self.feels_like_lbl.configure(text='Feels like:')
        self.feels_like_value_lbl.configure(text=str(self.weather.feels_like) + ' ℃')

        self.pressure_lbl.configure(text='Pressure:')
        self.pressure_value_lbl.configure(text=str(self.weather.pressure) + '  hPa')

        self.humidity_lbl.configure(text='Humidity:')
        self.humidity_value_lbl.configure(text=str(self.weather.humidity) + '  %')

        self.wind_lbl.configure(text='Wind:')
        self.wind_value_lbl.configure(text=str(self.weather.wind['speed']) + '  m/s  ', compound=tkinter.LEFT)
        wind_icon = customtkinter.CTkImage(dark_image=Image.open('icons/dir_d.png').rotate(self.weather.wind['deg']),
                                           light_image=Image.open('icons/dir_l.png').rotate(self.weather.wind['deg']),
                                           size=(20, 20))
        self.wind_value_lbl.configure(image=wind_icon, compound=tkinter.RIGHT)

        self.clouds_lbl.configure(text='Clouds:')
        self.clouds_value_lbl.configure(text=str(self.weather.clouds) + '  %')

        self.sun_lbl.configure(text='Day:')
        self.sun_value_lbl.configure(text=self.weather.sunrise + ' → ' + self.weather.sunset)

    def weather_request(self):
        self.weather_response = self.weather_api.get(self.city_text.get())
        if self.weather_response:
            if self.weather_response['cod'] == 200:
                self.weather = Weather(self.weather_response)
                self.update_weather_labels()
            else:
                self.location_lbl.configure(text=self.weather_response['message'])
        else:
            self.location_lbl.configure(text='No Internet Connection')

    def forecast_request(self):
        """ Forecast request"""
        data_list = self.forecast_api.get_forecast(lat=self.weather_response['coord']['lat'],
                                                   lon=self.weather_response['coord']['lon'])
        self.scrollable_frame = MyScrollableFrame(self, data_list=data_list, width=350, height=245,
                                                  orientation='horizontal')
        self.scrollable_frame.grid(row=12, column=0, pady=(20, 20), columnspan=2)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * event.delta), "units")


class MyScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, data_list=None, **kwargs):
        super().__init__(master, **kwargs)

        self.label = None
        self.my_frame = None

        if data_list:
            for index, data in enumerate(data_list):
                self.add_item(index, data)

    def add_item(self, index: int, data: dict):
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=index, padx=10, pady=10, sticky="nsew")

        self.label = customtkinter.CTkLabel(self.my_frame, text=data['datetime'], font=('Bolt', 15), width=145)
        self.label.grid(row=0, column=index, padx=5, pady=(10, 0))
        icon = customtkinter.CTkImage(Image.open(f'icons/{data['icon']}.png'), size=(120, 120))
        self.label = customtkinter.CTkLabel(self.my_frame, text='', image=icon)
        self.label.grid(row=2, column=index, padx=5, pady=0)
        self.label = customtkinter.CTkLabel(self.my_frame, text=data['description'].title())
        self.label.grid(row=3, column=index, padx=5, pady=0)
        self.label = customtkinter.CTkLabel(self.my_frame, text=data['temp'], font=('Bolt', 18))
        self.label.grid(row=4, column=index, padx=10, pady=10)


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(border_width=2)


if __name__ == '__main__':
    app = App()
    app.mainloop()
