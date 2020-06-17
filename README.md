# Drip by team "Cot Topic"

[Video Demo Here](https://youtu.be/i41RImNvX9M)

## Roles

Pratham Rawat
- Project Manager

Junhee Lee
- Routing

David Xie Deng
- HTML and CSS

Manfred Tan
- Backend and database

## Project Description

Many of us lead busy lives, with fashion being an integral part of our identity. However, fashion can often be cumbersome, especially when waking up early and rushing to leave on time for our responsibilities. That’s why we invented “Drip”, a weather based fashion app. 

The flow starts with creating an account. Drip automatically has a preset wardrobe with common items of clothing: pants, shorts, hoodies, etc. However, it is easy to add or remove these items, and easier still to dive deeper and add all of your different items of clothing. Drip will work well either way. 

Drip also learns from your preferences, every morning it greets you with a number of wardrobe ideas. You choose which one you go with in the app, or none of them. Drip will take the combinations you have into account, and tailor your suggestions to your choices. 

## API Used

[IP Geolocation](https://docs.google.com/document/d/1FazBlCH4SoM5bKaCs5vr4B7aEgTUVlvFv-1W-LoQmUA/edit?usp=drivesdk)
- Used to get the user's location from their IP (if possible) to feed into weather forecasting

[MetaWeather](https://docs.google.com/document/d/18uyXB5XPFQoGFJpoa2yQvRPhevc3HaBU4kO-OYN-ieY/edit?usp=drivesdk)  
- Used to get the location at which to use weather forecasts that power this app, from either the user's IP location, or an inputted location
 
## Running Instructions

Clone the repository, and in the repository root, run `pip3 install -r requirements.txt`, which will install the python packages required for this project.

Afterwards, simply use python3 to run the main project file as follows:
`python3 app/__init__.py`

The site can be found on `http:/localhost:5000`

Happy Drip!