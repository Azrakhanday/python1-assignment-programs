
    hotel={"small_room":300,
           "large_room":800,
           "extra-large_room":2000}

def booking_hotel():

            for room,amount in hotel.items():
                print(f"{room},{amount}/night")
            room_type=input("enter your room type")
            num_nights=int(input("enter how many nights you want to spend"))
            if room_type in hotel:
                total_cost=hotel[room_type]*num_nights







