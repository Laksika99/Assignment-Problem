# Hotel Room Booking System

rooms = []

# เพิ่มห้องพัก
def add_room():
    room_id = input("Enter Room ID: ")
    room_type = input("Enter Room Type: ")
    price = input("Enter Price: ")

    room = {
        "id": room_id,
        "type": room_type,
        "price": price,
        "status": "Available"
    }

    rooms.append(room)
    print("Room added successfully!")

# แสดงห้องพักทั้งหมด
def show_rooms():
    if len(rooms) == 0:
        print("No rooms available")
        return

    for room in rooms:
        print("----------------------")
        print("Room ID:", room["id"])
        print("Type:", room["type"])
        print("Price:", room["price"])
        print("Status:", room["status"])

# ค้นหาห้องพัก
def search_room():
    search_id = input("Enter Room ID to search: ")

    for room in rooms:
        if room["id"] == search_id:
            print("Room Found!")
            print(room)
            return

    print("Room not found")

# จองห้องพัก
def book_room():
    room_id = input("Enter Room ID to book: ")

    for room in rooms:
        if room["id"] == room_id:
            if room["status"] == "Available":
                room["status"] = "Booked"
                print("Room booked successfully!")
            else:
                print("Room already booked")
            return

    print("Room not found")

# ยกเลิกการจอง
def cancel_booking():
    room_id = input("Enter Room ID to cancel booking: ")

    for room in rooms:
        if room["id"] == room_id:
            if room["status"] == "Booked":
                room["status"] = "Available"
                print("Booking cancelled")
            else:
                print("Room is not booked")
            return

    print("Room not found")


# เมนูหลัก
while True:
    print("\n===== Hotel Booking System =====")
    print("1. Add Room")
    print("2. Show Rooms")
    print("3. Search Room")
    print("4. Book Room")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("Select menu: ")

    if choice == "233":
        add_room()

    elif choice == "234":
        show_rooms()

    elif choice == "235":
        search_room()

    elif choice == "236":
        book_room()

    elif choice == "237":
        cancel_booking()

    elif choice == "238":
        print("Exit Program")
        break

    else:
        print("Invalid choice")

