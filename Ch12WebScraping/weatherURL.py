#! python3
# weatherURL.py - Open the browser to the URL for your local weather.
# python3 weatherURL.py New York, NY, United States
# python3 weatherURL.py Istanbul, Turkey
# python3 weatherURL.py Helsinki

import webbrowser, sys

import pyperclip

if len(sys.argv) > 1:
    address = (" ".join(sys.argv[1:])).split(",")

else:
    # Get address from command line.
    address = (pyperclip.paste()).split(",")

if len(address) == 3:
    # Get address from command line.
    city = (address[0]).lower()
    state = (address[1][1:]).lower()
    country = (address[2][1:]).lower()
    webbrowser.open(
        "https://en.ilmatieteenlaitos.fi/local-weather/"
        + state
        + ", "
        + country
        + "/"
        + city
    )
elif len(address) == 2:
    # Get address from command line.
    city = (address[0]).lower()
    country = (address[1][1:]).lower()
    webbrowser.open(
        "https://en.ilmatieteenlaitos.fi/local-weather/" + country + "/" + city
    )
elif len(address) == 1:
    city = (address[0]).lower()
    webbrowser.open("https://en.ilmatieteenlaitos.fi/local-weather/" + city)
