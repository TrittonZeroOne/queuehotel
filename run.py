class HotelReservation:
    def __init__(self):
        self.rooms = {"Single": [], "Double": [], "Suite": []}

    def display_available_rooms(self):
        print("Available Rooms:")
        for room_type, room_list in self.rooms.items():
            print(f"{room_type}: {len(room_list)} available")

    def reserve_room(self, room_type, guest_name):
        if room_type in self.rooms and self.rooms[room_type]:
            booked_room = self.rooms[room_type].pop(0)
            print(f"Room {booked_room} has been reserved for {guest_name}.")
        else:
            print(f"Sorry, no available {room_type} rooms.")

    def add_room(self, room_type, room_number):
        if room_type in self.rooms:
            self.rooms[room_type].append(room_number)
            print(f"Added room {room_number} ({room_type})")
        else:
            print("Invalid room type.")

if __name__ == "__main__":
    hotel = HotelReservation()
    while True:
        print("\nWelcome to Hotel Reservation System")
        print("1. Display available rooms")
        print("2. Reserve a room")
        print("3. Add a room")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.display_available_rooms()
        elif choice == "2":
            room_type = input("Enter room type (Single/Double/Suite): ").capitalize()
            guest_name = input("Enter guest name: ")
            hotel.reserve_room(room_type, guest_name)
        elif choice == "3":
            room_type = input("Enter room type (Single/Double/Suite): ").capitalize()
            room_number = input("Enter room number: ")
            hotel.add_room(room_type, room_number)
        elif choice == "4":
            print("Thank you for using Hotel Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")
