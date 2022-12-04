import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print('Tap your ID')
try:
    id, text = reader.read()
    if id == 44823288530:
        {
            print("Valid ID")
        }
    else:
        {
            print("Invalid ID")
        }
    #print(id)
    print(text)
finally:
    GPIO.cleanup()
