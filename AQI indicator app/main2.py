from tkinter import *
from tkinter import font
import math
import requests
import json

root=Tk()

def getaqi_index(lat,lng,waqi_api_key):
    getaqi_url=f"https://api.waqi.info/feed/geo:{lat};{lng}/?token={waqi_api_key}"
    response=requests.get(getaqi_url)
    data=response.json()
    # print(data)
    if data['data']:
        aqi=data['data']['aqi']
        print(aqi)
        name_of_org=data['data']['attributions'][0]['name']
        print(name_of_org)
        city=data['data']['city']['name']
        City=str(city).split('(')[0]
        print(City)

    else:
        raise Exception('Error in finding the AQI of the region.')

    window=Tk()
    if aqi>=0 and aqi<=50:
        aqi_results='Good'
        bg_color='green'
        fg_color='black'
    elif aqi>=51 and aqi<=100:
        aqi_results='Moderate'
        bg_color='yellow'
        fg_color='black'
    elif aqi>=101 and aqi<=150:
        aqi_results='Unhealthy for Sensitive Groups'
        bg_color='Orange'
        fg_color='black'
    elif aqi>=151 and aqi<=200:
        aqi_results='Unhealthy'
        bg_color='red'
        fg_color='white'
    elif aqi>=201 and aqi<=300:
        aqi_results='Very Unhealthy'
        bg_color='purple'
        fg_color='white'
    elif aqi>=301:
        aqi_results='Hazardous'
        bg_color=(128,0,0)
        fg_color='white'
    frame=Frame(window,bg=f'{bg_color}')
    frame.pack(padx=100,pady=100)
    
    aqi_label=Label(frame,text=aqi,font=font.Font(size=40,weight='bold'),fg=f'{fg_color}',bg=f'{bg_color}')
    aqi_label.grid(row=0,column=0,rowspan=4,columnspan=4,padx=40,pady=40)

    air_pollution_results=Label(frame,text=aqi_results,fg=f'{fg_color}',bg=f'{bg_color}')
    air_pollution_results.grid(row=2,column=0,columnspan=4,rowspan=2,padx=10,pady=10)

    source_results=Label(frame,text=f'Source : {name_of_org}',fg=f'{fg_color}',bg=f'{bg_color}')
    source_results.grid(row=4,column=0,columnspan=4,rowspan=2,padx=10,pady=10)

    city_results=Label(frame,text=f'City : {City}',fg=f'{fg_color}',bg=f'{bg_color}')
    city_results.grid(row=6,column=0,columnspan=4,rowspan=2,padx=10,pady=10)

    

def search():
    zipcode=zipcode_entry.get()
    geocoding_api_key="your_geocoding_api_key"
    waqi_api_key='your_waqi_api_key'
    lat,lng=getcoords(zipcode,geocoding_api_key)
    
    print(f"latitude={lat},longitude={lng}")
    getaqi_index(lat,lng,waqi_api_key)
    # print(type(lat),type(lng))

def  getcoords(zipcode,geocoding_api_key):
    getcoord_url=f"https://api.opencagedata.com/geocode/v1/json?q={zipcode}&key={geocoding_api_key}"
    response=requests.get(getcoord_url)
    data=response.json()
    if data['results']:
        lat=data['results'][0]['geometry']['lat']
        lng=data['results'][0]['geometry']['lng']
        # print(lat)
        # print(lng)
    else:
        raise Exception('No coordinates found at the given ZipCode.')
    return round(lat,4),round(lng,4)
    

f=LabelFrame(root,text='Search for Your Region AQI')
f.pack(padx=100,pady=100)
zipcode_label=Label(f,text='Enter your Zipcode:')
zipcode_label.grid(row=0,column=0,padx=40,pady=40)
zipcode_entry=Entry(f)
zipcode_entry.grid(row=0,column=1,columnspan=2,padx=40,pady=40)
button=Button(f,text='Search AQI',command=search)
button.grid()



root.mainloop()