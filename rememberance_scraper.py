import RPi.GPIO as blink
import requests
import time
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kentucky")

soup = BeautifulSoup(response.text, "html.parser")

scraped = soup.find("div", text="Deaths")
blink_count = int(scraped.next_element.next_element.get_text())


blink.setmode(blink.BCM)
blink.setup(4, blink.OUT)

def lights(blink_count):
    for _ in range(blink_count):
        blink.output(4, True)
        time.sleep(2)
        blink.output(4, False)
    time.sleep(7)
    lights(blink_count)

lights(blink_count)
    