def convertRoomNumber(room_number, starting_floor, reference_starting_floor):
    offset = starting_floor - reference_starting_floor
    adjusted_room_number = room_number - offset
    return adjusted_room_number
room_number = 105
starting_floor = 5
reference_starting_floor = 1
adjusted_room_number = convertRoomNumber(room_number, starting_floor, reference_starting_floor)
print(adjusted_room_number)  # Output: 101
