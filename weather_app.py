import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "YOUR_API_KEY" #Add API key Here

def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"#Add API key Here
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        messagebox.showerror("Error", "City not found.")
    else:
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        messagebox.showinfo("Weather", f"Temperature: {temperature}°C\nWeather: {weather}")

# Main window
window = tk.Tk()
window.title("Weather App")

# Create and place the widgets
city_label = tk.Label(window, text="City:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Start the GUI main loop
window.mainloop()
