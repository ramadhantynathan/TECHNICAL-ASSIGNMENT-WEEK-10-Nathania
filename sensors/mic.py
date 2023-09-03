import RPi.GPIO as GPIO

SOUND_COUNTER_LIMIT = 1000
SOUND_COUNTER_MAX = 1000
SOUND_MAX = 5000

class mic:
    sound_pin: int
    counter = 0
    sound = 0
    
    def __init__(self,sound_pin: int) -> None:
        self.sound_pin = sound_pin  
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sound_pin, GPIO.IN)
    
    def calculate(self) -> int: 
        sound_value = GPIO.input(self.sound_pin)

        if sound_value == GPIO.HIGH:
            if self.counter < SOUND_COUNTER_MAX:
                self.counter += 10 
            # Cek jika counter melebihi yang sehaursnya
            # Jika iya. maka tambahkan value dari sound
            
            if self.counter < SOUND_COUNTER_LIMIT:
                if self.counter < SOUND_MAX:
                    self.sound += 10
        elif sound_value == GPIO.LOW:
            # Turunkan value counter sedikit demi sedikit jika tidak ada suara
            if self.counter > 0:
                self.counter -= 1
                self.sound -= 1

            if self.counter <= 0: 
                self.counter = 0  
                self.sound = 0
        
        return self.sound