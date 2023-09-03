import RPi.GPIO as GPIO
import time

class Ultrasonic:
    trigger_pin: int
    echo_pin : int

    def __init__(self, trigger_pin : int, echo_pin : int) -> None:
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
    
    # Source https://stackoverflow.com/questions/54631088/function-to-check-distance-using-ultrasonic-sensor-freezes-tkinter
    def _get_distance(self) -> float :
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.0001)
        GPIO.output(self.trigger_pin, False)

        StartTime = time.time()
        StopTime = time.time()

        while GPIO.input(self.echo_pin) == 0:
            StartTime = time.time()

        while GPIO.input(self.echo_pin) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2

        return distance
    def calculate(self)-> float:
        return self._get_distance()
