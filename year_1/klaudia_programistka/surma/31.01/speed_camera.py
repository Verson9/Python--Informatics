#   DW3123 S 1500 21:00 21:01 <--To w prowadzam
#   DW3123   .   90.0 <-- to wychodzi
#   DW3123 . 90.00 <-- to powinno wyjść

import datetime


def get_data_from_speed_cameras():
    first_speed_camera_register: str

    registration_number, vehicle_type, distance_traveled, first_speed_camera_register, second_speed_camera_register = input_file.read().split(
        " ")
    input_file.close()
    first_speed_camera_time = datetime.time(int(str(first_speed_camera_register).split(':')[0]),
                                            int(str(first_speed_camera_register).split(':')[1]))
    second_speed_camera_time = datetime.time(int(str(second_speed_camera_register).split(':')[0]),
                                             int(str(second_speed_camera_register).split(':')[1]))
    return registration_number, vehicle_type, distance_traveled, first_speed_camera_time, second_speed_camera_time


def check_registered_data(registered_data):
    registration_number = str(registered_data[0])
    for i in range(len(registration_number)):
        if (i < 2 and registration_number[i].isalpha()) \
                or (1 < i < 6 and registration_number[i].isnumeric()):
            continue
        else:
            print("Blad")
            main()


def count_time_in_minutes_between(first_speed_camera_time, second_speed_camera_time):
    time_between = float((datetime.timedelta(hours=float(second_speed_camera_time.hour),
                                     minutes=float(
                                         second_speed_camera_time.minute)) -
                  datetime.timedelta(hours=float(first_speed_camera_time.hour), minutes=float(
                      first_speed_camera_time.minute))).seconds) / 3600
    return time_between


def calculate_data(registered_data):
    distance_traveled = float(registered_data[2]) / 1000
    first_speed_camera_time = registered_data[3]
    second_speed_camera_time = registered_data[4]
    time_between_speed_cameras = count_time_in_minutes_between(first_speed_camera_time, second_speed_camera_time)
    velocity = distance_traveled / time_between_speed_cameras
    return velocity


def check_if_good_driver_or_fucking_pirate(registered_data, velocity):
    if registered_data[1] == "C" and round(velocity, 2) > 90:
        return "M"
    elif registered_data[1] == "S" and round(velocity, 2) > 140:
        return "M"
    else:
        return "."


def output_data(registered_data, velocity, good_driver):
    registration_number = registered_data[0]
    log = str(registration_number) + ' ' + str(good_driver) + ' ' + str(velocity)
    output_file.write(log)
    output_file.close()
    print(log)


def main():
    registered_data = get_data_from_speed_cameras()
    check_registered_data(registered_data)
    velocity = calculate_data(registered_data)
    good_driver = check_if_good_driver_or_fucking_pirate(registered_data, velocity)
    output_data(registered_data, velocity, good_driver)


input_file = open("data_for_speed_camera", 'r')
output_file = open("output_log", 'a')
main()
