import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json

API_KEY = "9586b94eb90e9611d1a9a18bd9a076c4"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
data = response.json()

# Extract weather info
weather = {
    'City': data['name'], 
    'Temperature (C)': data['main']['temp'],
    'Humidity (%)': data['main']['humidity'],
    'Pressure (hPa)': data['main']['pressure'],
    'Weather': data['weather'][0]['description']
}

print(weather)


#for json file
df = pd.DataFrame([weather])
df.to_csv("weather_data.csv", index=False)
print("Weather data saved to weather_data.csv")


# --- Option 1: Simple Matplotlib bar chart ---
labels = list(weather.keys())[1:-1]  # Skip 'City' and 'Weather'
values = list(weather.values())[1:-1]

plt.bar(labels, values, color='skyblue')
plt.title(f"Weather Report: {weather['City']}")
plt.ylabel("Values")
plt.show()


# --- Option 2: Seaborn barplot ---
# df = pd.DataFrame([weather])
# sns.barplot(
#     data=df.melt(id_vars=['City', 'Weather'], var_name='Parameter', value_name='Value'),
#     x='Parameter', y='Value'
# )
# plt.title(f"Weather Conditions in {CITY}")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# for table format 

# Table view in terminal
df = pd.DataFrame([weather])
print("\nWeather Report Table:\n" + "-"*30)
print(df.to_string(index=False))


