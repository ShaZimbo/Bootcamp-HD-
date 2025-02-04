# Functions for for city options
def city_options():
    print("City destinations:")
    print("z = Zimbabwe")
    print("c = Crete")
    print("m = Manchester")
    print("p = Paris")
    print("e = Exit")


def plane_cost(destination):
    plane_price = {"z":750, "c":325, "m":100, "p":250}
    return plane_price.get(destination, "Destination not found.")


# Functions for total holiday, including flight, hotel, and car costs
def city_destination(city):
    destination = {
        "z":"Zimbabwe",
        "c":"Crete",
        "m":"Manchester",
        "p":"Paris"}
    return destination.get(city,"Unknown destination")


def hotel_cost(nights):
    hotel_price = nights * 550
    return hotel_price


def car_rental(days):
    car_price = days * 125
    return car_price


def holiday_cost(f, h, c):
    holiday_price = f + h + c
    return holiday_price


# Calculate costs based on user selection
print("This programme will calculate the cost of your holiday:")
destination = ""
city_options()

while destination != "e":
    destination= input("Please enter your destination: ").lower()
  
    if destination in ["z", "c", "m", "p"]:
        plane_cost(destination)
        city_destination(destination)
        break
    elif destination == "e":
        print("You have exited")
        exit()
    else:
        print("That destination is not recognised")

nights = int(input
("Please enter the number of nights you will stay in the hotel: "))
hotel_cost(nights)

days = int(input
("Please enter the number of days you will be renting a car: "))
car_rental(days)

plane_price = plane_cost(destination)
hotel_price = hotel_cost(nights)
car_price = car_rental(days)

# Add to get the total cost of the holiday
print(f"\nYour travel arrangements and costs:\n"
      f"You will be travelling to {city_destination(destination)}.\n"
      f"Flight costs: £{plane_price}\n"
      f"Hotel stay for {nights} nights will cost: £{hotel_price}\n"
      f"Car rental for {days} days will cost: £{car_price}\n"
      f"This holiday will cost a total of: £"
      f"{holiday_cost(plane_price, hotel_price, car_price)}"
      )
