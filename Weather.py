import customtkinter as ctk
import requests

# Setup GUI
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("white")

app = ctk.CTk()
app.geometry("400x400")
app.title("Weather 🌦️")

# Function to fetch weather data
def get_weather():
    city = city_entry.get().strip()
    api_key = "8519639e38ba592c0cc9e0e4f322ffd0"  # Your API Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            result_label.configure(
                text=f"📍 City: {city.title()}\n🌡️ Temp: {temp}°C\n💧 Humidity: {humidity}%\n🌤️ {desc.title()}"
            )
        else:
            result_label.configure(text="❌ City not found!")
    except:
        result_label.configure(text="⚠️ Error fetching data")

# GUI Components
city_entry = ctk.CTkEntry(app, placeholder_text="Enter city name")
city_entry.pack(pady=20)

get_btn = ctk.CTkButton(app, text="Get Weather", command=get_weather)
get_btn.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16), justify="left")
result_label.pack(pady=20)

# Start GUI loop
app.mainloop()