from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def read_temperature_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data, reading = line.strip().split(',')
            temperature = float(reading[:-2])
            data.append((data, temperature))
    return data


def main():
    filename = 'temperature_data.csv'
    temperature_data = read_temperature_data(filename)

    for date, temp in temperature_data:
        if '°C' in temp:
            celsius = float(temp[:-2])
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{date}: {celsius:.1f}°C = {fahrenheit:.1f}°F")
        elif '°F' in temp:
            fahrenheit = float(temp[:-2])
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{date}: {fahrenheit:.1f}°F = {celsius:.1f}°C")


if __name__ == '__main__':
    main()
