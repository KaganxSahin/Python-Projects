import math

def apparent_magnitude(absolute_magnitude, distance_ly):
    distance_pc = distance_ly / 3.262  
    return absolute_magnitude + 5 * math.log10(distance_pc / 10)

def calculate_absolute_magnitude(apparent_magnitude, distance_ly):
    distance_pc = distance_ly / 3.262  
    return apparent_magnitude - 5 * math.log10(distance_pc / 10)

def main():
    try:
        absolute_magnitude_input = float(input("Enter the star's absolute magnitude (in magnitudes): "))
        distance_ly = float(input("Enter the distance to the star (in light years): "))

        apparent_magnitude_value = apparent_magnitude(absolute_magnitude_input, distance_ly)
        calculated_absolute_magnitude = calculate_absolute_magnitude(apparent_magnitude_value, distance_ly)

        print(f"Absolute Magnitude: {calculated_absolute_magnitude:.2f} magnitudes")
        print(f"Apparent Magnitude: {apparent_magnitude_value:.2f} magnitudes")
    except ValueError:
        print("Please enter valid numerical values for both the absolute magnitude and the distance in light years.")

if __name__ == "__main__":
    main()
