#   DW3123 S 1500 21:00 21:01 <--To w prowadzam
#   DW3123   .   90.0 <-- to wychodzi
#   DW3123 . 90.00 <-- to powinno wyjść

registration_number, vehicle_type, distance_traveled, first_speed_camera, second_speed_camera = input("").split(" ")
first_speed_camera_hours = first_speed_camera[0] + first_speed_camera[1]
first_speed_camera_minutes = first_speed_camera[3] + first_speed_camera[4]
secound_speed_camera_hours = second_speed_camera[0] + second_speed_camera[1]
second_speed_camera_minutes = second_speed_camera[3] + second_speed_camera[4]

letters = {
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
    "Z",
    "X",
    "Q",
    "V"
}
numbers = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
}
numbersa = {
    "0",
    "1",
    "2"
}
numbersb = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5"
}

if first_speed_camera[0] in list(numbersa) and first_speed_camera[1] in list(numbers) and first_speed_camera[
    2] == ":" and first_speed_camera[3] in list(numbersb) and first_speed_camera[4] in list(numbers) and \
        second_speed_camera[0] in list(numbersa) and second_speed_camera[1] in list(numbers) and second_speed_camera[
    2] == ":" and second_speed_camera[3] in list(numbersb) and second_speed_camera[4] in list(numbers) and int(
        first_speed_camera_hours) < 24 and int(first_speed_camera_minutes) < 60 and int(
        secound_speed_camera_hours) < 24 and int(second_speed_camera_minutes) < 60 and registration_number[0] in list(
        letters) and registration_number[1] in list(letters) and registration_number[2] in list(numbers) and \
        registration_number[3] in list(numbers) and registration_number[4] in list(numbers) and registration_number[
    5] in list(numbers) and vehicle_type == "S" or vehicle_type == "C":
    s = int(distance_traveled)
    hours_first_speed_camera = int(first_speed_camera_hours)
    minutes_first_speed_camera = int(first_speed_camera_minutes)
    hours_secound_speed_camera = int(secound_speed_camera_hours)
    minutes_second_speed_camera = int(second_speed_camera_minutes)
    if hours_first_speed_camera > hours_secound_speed_camera:
        hours_secound_speed_camera = hours_secound_speed_camera + 24
    if minutes_first_speed_camera > minutes_second_speed_camera:
        hours_secound_speed_camera = hours_secound_speed_camera - 1
        minutes_second_speed_camera = minutes_second_speed_camera + 60
    minutes_fsc = hours_first_speed_camera * 60 + minutes_first_speed_camera
    minutes_ssc = hours_secound_speed_camera * 60 + minutes_second_speed_camera
    hours_fsc = minutes_fsc / 60
    hours_ssc = minutes_ssc / 60
    v = s / 1000 / (hours_ssc - hours_fsc)

    if round(v, 2) > 80 and vehicle_type == "C":
        mandate = "M"
    elif round(v, 2) > 140 and vehicle_type == "S":
        mandate = "M"
    else:
        mandate = "."

    print(registration_number, mandate, round(v, 3))
else:
    print("BLAD")
