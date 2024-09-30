import requests
import json
import subprocess
import platform
import os

def main():
    os_name = platform.system()
    print("\tWELCOME TO WEATHER UPDATE\n")

    if os_name == "Windows":
          speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('HELLO USER AND WELCOME TO WEATHER UPDATE, ENTER THE LOCATION FOR KNOW WEATHER DETAILS')"
          subprocess.run(["powershell","-command",speaker],stdout = subprocess.DEVNULL)
    if os_name == "Darwin":
         speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('HELLO USER AND WELCOME TO WEATHER UPDATE, ENTER THE LOCATION FOR KNOW WEATHER DETAILS')"
         subprocess.run(['say',speaker])

    print("TYPE \"exit\" FOR EXIT FROM THE WEATHER UPDATE")
    while True:
        location = input("Enter the location:\n")
        try:
            if location == "exit":
                 speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('thankyou for using weather update')"
                 subprocess.run(["powershell","-command",speaker],stdout = subprocess.DEVNULL)
                 exit(0)
                 
            url = f"https://api.weatherapi.com/v1/current.json?key=6866933ecc054aeaabd121853242909&q={location}"

            #getting data from api
            responce = requests.get(url)
   
            #check the data is correct or not
            if responce.status_code == 200:
                pass

            weatherDictonary = responce.json()
            if "error" in weatherDictonary:
                message = weatherDictonary["error"]["message"]
                if os_name == "Windows":
                        # speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('It's {celcius} degree with {condition} weather in {location}')"
                        speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('ENTER THE VALID LOCATION')"
                        subprocess.run(["powershell","-command",speaker],stdout = subprocess.DEVNULL)
        
                    #text to speech for mac
                if os_name == "Darwin":
                        speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('ENTER THE VALID LOCATION')"
                        subprocess.run(['say',speaker])
                print(message,"\n")
            else:
                #identify that location exits or not
                if "current" in weatherDictonary and "temp_c" in weatherDictonary["current"]:

                    #get the details from api
                    celcius = weatherDictonary["current"]["temp_c"]
                    ferenhit = weatherDictonary["current"]["temp_f"]
                    condition = weatherDictonary["current"]["condition"]["text"]
                    wind = weatherDictonary["current"]["wind_kph"]
                    cloud = weatherDictonary["current"]["cloud"] 

                    cityName = weatherDictonary["location"]["name"]
                    cityRegion = weatherDictonary["location"]["region"]
                    cityCountry = weatherDictonary["location"]["country"]
                    cityTime = weatherDictonary["location"]["localtime"]
                    currentDateTime = cityTime.split(" ")
        
                    #print details to the useer
                    # if(city == cityName):
                    print("\nLOCATION DETAILS :-")
                    print(f"City name: {cityName}")
                    print(f"City region: {cityRegion}")
                    print(f"Country name: {cityCountry}")
                    print(f"Current date: {currentDateTime[0]}")
                    print(f"Current time: {currentDateTime[1]}")

                    print(f"\nWEATHER DETAILS:-")
                    print(f"Temptature in Celcius: {celcius}°C")
                    print(f"Temptature in Fahrenheit: {ferenhit}°F")
                    print(f"Condition: {condition}")
                    print(f"Wind: {wind} km/h")
                    print(f"Cloud: {cloud}\n")
                    
                    #text to speech for windows
                    if os_name == "Windows":
                        # speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('It's {celcius} degree with {condition} weather in {location}')"
                        speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('It is {celcius} degree {condition} weather in {location}')"
                        subprocess.run(["powershell","-command",speaker],stdout = subprocess.DEVNULL)
        
                    #text to speech for mac
                    if os_name == "Darwin":
                        speaker = f"(New-Object -ComObject SAPI.SpVoice).Speak('It is {celcius} degree {condition} weather in {location}')"
                        subprocess.run(['say',speaker])

        except Exception as error:
            print(f"Some error accured: {error}")
main()

