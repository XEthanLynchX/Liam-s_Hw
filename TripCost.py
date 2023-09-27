def roomCost(nights, room_type):
    room_prices = {
        1: 375,
        2: 350,
        3: 525,
        4: 475
    }
    return room_prices.get(room_type, 0) * nights

def mealCost(brunches, dinners):
    brunch_price = 25
    dinner_price = 75
    gratuity_rate = 0.15
    total_cost = (brunch_price + dinner_price) * (brunches + dinners)
    gratuity = total_cost * gratuity_rate
    return total_cost + gratuity

def excursionCost(picnic, snorkeling, guided_hike, boat_dinner):
    excursion_prices = {
        'Picnic': 50,
        'Snorkeling': 25,
        'Guided Hike': 17,
        'Boat Dinner': 200
    }
    total_cost = 0
    total_cost += excursion_prices.get('Picnic', 0) if picnic == 'y' else 0
    total_cost += excursion_prices.get('Snorkeling', 0) * snorkeling
    total_cost += excursion_prices.get('Guided Hike', 0) * guided_hike
    total_cost += excursion_prices.get('Boat Dinner', 0) if boat_dinner == 'y' else 0
    return total_cost

print("Number of nights: ")
nights = int(input())
print("Number of people: ")
people = int(input())

print("Room Types:")
print("(1) - Two Queen Beds")
print("(2) - One King Bed")
print("(3) - Queen Suite")
print("(4) - King Suite")
print("Select Type: ")
room_type = int(input())

print("How many Brunches: ")
brunches = int(input())
print("How many Dinners: ")
dinners = int(input())

print("Picnic?: ")
picnic = input()
print("Snorkeling?: ")
snorkeling = int(input())
print("Guided Hike?: ")
guided_hike = int(input())
print("Boat Dinner?: ")
boat_dinner = input()

room_cost = roomCost(nights, room_type)
meal_cost = mealCost(brunches, dinners)
excursion_cost = excursionCost(picnic, snorkeling, guided_hike, boat_dinner)

total_cost = room_cost + meal_cost + excursion_cost

print(f"Room Cost: ${room_cost}")
print(f"Meal Cost: ${meal_cost}")
print(f"Excursion Cost: ${excursion_cost}")
print(f"Total Cost: ${total_cost}")