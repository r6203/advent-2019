import math

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

if __name__ == "__main__":
    with open("day1-input.txt", "r") as file:
        upper_fuel_limit = 0

        for mass in file.readlines():
            fuel = calc_fuel(int(mass))
            additional_fuel = fuel

            while additional_fuel > 0:
                additional_fuel = calc_fuel(additional_fuel)

                if additional_fuel > 0:
                    fuel = fuel + additional_fuel

            upper_fuel_limit = upper_fuel_limit + fuel

        print(upper_fuel_limit)
