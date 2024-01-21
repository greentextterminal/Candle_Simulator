import time
import random

# duty cycle values are between 0 and 65535

# constants
MAX_DUTY_CYCLE = 65535
INCREMENT = MAX_DUTY_CYCLE / 10  # segment entire duty cycle range into 10 parts
INCREMENT_RANGE = [int(INCREMENT * (i + 1)) for i in
                   range(10)]  # populate list of duty cycle range (brightness levels) with increments
print('Duty cycles list:', INCREMENT_RANGE)


def random_num_generator():
    """Returns a random number between 0 and 9 inclusive"""
    arr = range(0, 10)
    random_val = random.choice(arr)  # pick a random value from arr
    return random_val


prev_brightness = random_num_generator()  # init
while True:
    brightness_value = random_num_generator()  # brightness of 'flame'
    duration_value = random_num_generator()  # duration of 'flame'

    print(abs(brightness_value - prev_brightness))
    while abs(brightness_value - prev_brightness) >= 3:
        brightness_value = random_num_generator()

    for duration in range(duration_value):
        print('brightness value:', brightness_value)
        # print((INCREMENT_RANGE[duration],))  # tuple for serial plotter
        if brightness_value >= 8:  # bias 'flame' towards being brighter for most of the time
            pwm_duty_cycle = INCREMENT_RANGE[brightness_value]
            # time.sleep(0.1)
        elif brightness_value >= 6:  # 'flame' stays on mid brightness for less amount of time
            pwm_duty_cycle = INCREMENT_RANGE[brightness_value]
            # time.sleep(0.001)
        else:  # 'flame' periodically dips into brightness values less than 5
            pwm_duty_cycle = INCREMENT_RANGE[brightness_value]

    prev_brightness = brightness_value  # record previous brightness val

    time.sleep(0.1)
