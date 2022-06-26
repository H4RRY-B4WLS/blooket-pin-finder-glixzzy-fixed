#H4RRY-B4WLS
 
import random
import requests

def getRndInt():
    for _ in range(999999):
        value = random.randint(100000, 999999)
        response = requests.get(
            f"https://fb.blooket.com/c/firebase/id?id={value}")
        data = response.json()

        if data["success"] == True:
            print('Valid Game Pin: ' + str(value))
            quit("Pin Found!")
            
getRndInt();
