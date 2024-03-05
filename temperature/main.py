from converter_package.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converter_package.distance import feet_to_meters, meters_to_feet


def read_temperature_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data, distance, reading = line.strip().split(',')
            temperature = float(reading[:-2])
            data.append((data, distance, temperature))
    return data


def main():
    filename = 'temperature_data.csv'
    temperature_data = read_temperature_data(filename)

    for date, distance, temp in temperature_data:
        if '°C' in temp:
            celsius = float(temp[:-2])
            fahrenheit = celsius_to_fahrenheit(celsius)
            meters = float(distance[:-1])
            feet = meters_to_feet(meters)
            print(f"{date}: {celsius:.1f}°C = {fahrenheit:.1f}°F, {meters:.1f} meters = {feet:.1f} feet")
        elif '°F' in temp:
            fahrenheit = float(temp[:-2])
            celsius = fahrenheit_to_celsius(fahrenheit)
            feet = float(distance[:-2])
            meters = feet_to_meters(feet)
            print(f"{date}: {fahrenheit:.1f}°F = {celsius:.1f}°C, {feet:.1f} feet = {meters:.1f} meters")


if __name__ == '__main__':
    main()
