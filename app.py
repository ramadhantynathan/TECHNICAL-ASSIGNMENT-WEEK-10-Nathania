from sensors.ultrasonic import Ultrasonic
from core.ubidots import Ubidots as Ubi
from sensors.mic import mic
from dotenv import load_dotenv
import time
import os

SOUND_PIN = 27
ULTRA_TRIGGER = 4
ULTRA_ECHO = 17
DEVICE_LABEL = "burberry"

load_dotenv()

class App:
    def __init__(self) -> None:
        Ultra = Ultrasonic(ULTRA_TRIGGER, ULTRA_ECHO)
        Mic = mic(SOUND_PIN)
        Ubidots = Ubi(DEVICE_LABEL)

        while True:
            current_time = time.time()

            ultra_result = Ultra.calculate()
            mic_result = Mic.calculate()
            
            Ubidots.request(
                {
                "ultrasonic": ultra_result,
                "mic": mic_result
                }
                ,current_time)
            


App()