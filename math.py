import math

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return 4/3 * math.pi * radius**3

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

# Prompt user for input
sphere_radius = float(input("What is the radius for the sphere portion: "))
cylinder_radius = float(input("What is the radius for the cylinder portion: "))
cylinder_height = float(input("What is the height for the cylinder portion: "))

# Calculate the volume of the sphere and cylinder
sphere_vol = sphere_volume(sphere_radius)
cylinder_vol = cylinder_volume(cylinder_radius, cylinder_height)

# Calculate the total volume of the water tower
total_vol = sphere_vol/2 + cylinder_vol

# Print the total volume
print("Volume:", total_vol)