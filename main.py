from fastapi import FastAPI
from enum import Enum

class Car(Enum):
    SEDAN = "City"
    SUV = "Pajero"
    JEEP = "THAR"


app = FastAPI()

@app.get("/")
async def root():
    return f"{int(5+6)} is the sum of five and six"

@app.post("/")
async def post_text():
    return 'Text returns from post route'

@app.get("/username/")
async def username():
    return "Beep beep you've approached username route, please add your username after the forward slash and submit the request."

@app.get("/username/abhinav")
async def abhinav():
    return "your majesty abhinav, who dareth ask your uid. you're in!!"

@app.get("/username/{uid}")
async def getuid(uid: str):
    return f"Your username is {uid}"

@app.get("/car/")
async def carhome():
    return f"you're in the car route, apend whether you have a City, Pajero, or a Thar"

@app.get("/car/{carname}")
async def cartype(carname: Car):
    match carname:
        case Car.SEDAN:
            return f"{carname.value} is a {carname.name}, great choice i love sedans are awesome"
        case Car.JEEP:
            return f"{carname.value} is a {carname.name}, take your jeep off the road and in the jungle man!"
        case Car.SUV:
            return f"{carname.value} is a {carname.name}, woohoo you were born a champion honestly."
        case _:
            return f"You probably have a cool car too!"

@app.get('/frank/{date}')
async def frankie(date: str, q: str | None = None, biscuit: bool = True):
    greeting = f"Hi {date}! My name is Frankie and i am not up for a date today, sorry!!"
    if q == "mercedes":
        return (greeting + " I guess we are going on a date afterall, nothing to do with your mercedes benz honestly!! I liked you since always")
    elif biscuit == True:
        return (greeting + " Not a fancy car but at least you have an biscuit, i guess we are going after all")
    else:
        return (greeting + " you got neither the mercedes nor the biscuit. Suck your own dick.")
    
