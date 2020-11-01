import time
import datetime

print("Please type your text after 3 seconds")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Go!")
time.sleep(0.2)

before = datetime.datetime.now()
kelime=input("Type here:")

zaman = datetime.datetime.now()
hiz = zaman - before
seconds = round(hiz.total_seconds(),2)

letter_per_second = round(len(kelime) / seconds,1)
print("You typed in : {} seconds.".format(seconds))

print("{} letters per second.".format(letter_per_second))