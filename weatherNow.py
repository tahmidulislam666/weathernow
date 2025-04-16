import requests
import tkinter as tk
from tkinter import messagebox

def get_loc():
    response = requests.get('https://ipinfo.io')
    if response.status_code == 200:
        data = response.json()
        return data.get('city')
    return None

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Unable to retrieve location.")
        return
    api_key = "5217f404c8594bc3b97121456251404"
    base_url = "http://api.weatherapi.com/v1/current.json"
    para = {
        "key": api_key,
        "q": city,
        "aqi": "yes"
    }
    response = requests.get(base_url, params=para)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']
        aqi = data["current"]["air_quality"]["pm2_5"]
                
        result = (f"Location: {location}, {country}\n"
                        f"Temperature: {temp_c}°C\n"
                        f"Condition: {condition}\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_kph} kph\n"
                        f"Air Quality (PM2.5): {aqi:.2f} µg/m³")
        
        messagebox.showinfo("Weather Information", result)
    else:   
        messagebox.showerror("Error", "Unable to retrieve weather data.")

root = tk.Tk()
root.title("WeatherNow")
root.geometry("400x250")
root.configure(bg="lightblue")

title_label = tk.Label(root, text="🌤️WeatherNow", font=("Helvetica", 14, "bold"))
title_label.pack(pady=20)
city_entry = tk.Entry(root, width=35, font=("Helvetica", 12),justify="center")
city_entry.pack(pady=10)
detect_city=get_loc()
if detect_city:
    city_entry.insert(0, detect_city)
else:
    city_entry.insert(0, "Enter your city")
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="lightgreen")
get_weather_button.pack(pady=10)
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), bg="red")
exit_button.pack(pady=10)
root.mainloop()    