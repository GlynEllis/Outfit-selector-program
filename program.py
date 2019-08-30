import json
import random#Random when outfits have been added.
import requests

with open('clothing.txt','r') as incoming_data:
    clothing_informaion = json.load(incoming_data)

possible_choices = {}
final_outfit = {}
temp = []
wind_speed = []
description = []
#Need to save the data within the dictionaries and load them again as necessary so that they don't need to be added every time
hats = clothing_informaion[0]
jackets = clothing_informaion[1]
jumpers = clothing_informaion[2]
tees = clothing_informaion[3]
bottoms = clothing_informaion[4]
socks = clothing_informaion[5]
shoes = clothing_informaion[6]

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Stockholm&APPID=76852765b5d0777aa3af09938f379342")
forecast = r.json()

def get_data():
    counter = 0
    while counter < 8:#Data is captured every 3 hours, 8 is a day(24hrs).
        temp.append(forecast['list'][counter]['main']['temp']-273.15) #Need to convert from kelvin to celcius.
        description.append(forecast['list'][counter]['weather'][0]['main'])
        wind_speed.append(forecast['list'][counter]['wind']['speed']*2.3)
        counter += 1
    

def get_forecast():
    counter = 0
    print 'LOCATION:',forecast['city']['name']
    while counter < 8:#Data is captured every 3 hours, 8 is a day(24hrs).
        
        print '*****************************************************************'

        print 'FORECAST TIME:',forecast['list'][counter]['dt_txt']
        print "TEMP:",forecast['list'][counter]['main']['temp']-273.15 #Need to convert from kelvin to celcius.
        print 'DESCRIPTION:',forecast['list'][counter]['weather'][0]['main']
        print 'DETAILED DESCRIPTION:',forecast['list'][counter]['weather'][0]['description']
        print 'WIND SPEED(M/S):',forecast['list'][counter]['wind']['speed']
        print 'WIND SPEED(MPH):',forecast['list'][counter]['wind']['speed']*2.3 #Converting to mph.

        counter += 1
    
def get_averages():
    print 'LOCATION:',forecast['city']['name']
    temp_average = sum(temp)/len(temp)
    print "AVERAGE TEMP:",'%.2f' % temp_average,'DEGREES'#'%' used to display to 'n' numbers after decimal.

    windspeed_average = sum(wind_speed)/len(wind_speed)
    print 'AVERAGE WINDSPEED:','%.2f' % windspeed_average,'MPH'

    print 'THE WEATHER DESCRIPTIONS FOR THE NEXT 24 HOURS:'
    for x in range(len(description)):
        print '(',forecast['list'][x]['dt_txt'],')',description[x]
    print '\n'


def add_clothing():
    #Need a menu loop to add different items to a dictionary list thing...
    choice = 0
    while True:
        print '*****************************************************************'
        print'What item of clothing are you adding?'
        print'1.Hat...'
        print'2.Jacket...'
        print'3.Jumpers...'
        print'4.T-shirt...'
        print'5.Bottoms...'
        print'6.Socks...'
        print'7.Shoes...'
        print'8.Accessories...'
        print'9.Save and exit...'
        print '*****************************************************************'

        choice = int(raw_input())
        if choice == 1:
            add_hat()
        elif choice == 2:
            add_jacket()
        elif choice == 3:
            add_jumper()
        elif choice == 4:
            add_tee()
        elif choice == 5:
            add_bottoms()
        elif choice == 6:
            add_socks()
        elif choice == 7:
            add_shoes()
        elif choice == 9:
            with open('clothing.txt', 'w') as outfile:  
                json.dump([hats,jackets,jumpers,tees,bottoms,socks,shoes], outfile)
            break
    

def add_hat():
    item = len(hats)+1
    hats[item] = {}
    print 'What is the name of the item?'
    name = (raw_input())
    hats[item]['Name'] = name

    print 'Is it a cap or a beanie?'
    item_type = (raw_input())#Don't really need the variable stuff can do it straight.
    if item_type == 'cap':
        hats[item]['Type'] = 'cap'
    else:
        hats[item]['Type'] = 'beanie'
    
    print 'What colour is the item?'
    colour = (raw_input())
    hats[item]['Colour'] = colour

    print 'Is it formal? yes/no'
    decision = (raw_input())
    if decision == 'yes':
        hats[item]['Formal'] = True
    else:
        hats[item]['Formal'] = False
    print hats


def add_jacket():
    item = len(jackets)+1
    jackets[item] = {}

    print 'What is the name of the item?'
    name = (raw_input())
    jackets[item]['Name'] = name

    print 'Is it heavy or light?'
    weight = (raw_input())
    if weight == 'heavy':
        jackets[item]['Weight'] = 'heavy'
    else:
        jackets[item]['Weight'] = 'light'
        
    print 'What colour is the item?'
    colour = (raw_input())
    jackets[item]['Colour'] = colour

    print 'Is it formal? yes/no'
    decision = (raw_input())
    if decision == 'yes':
        jackets[item]['Formal'] = True
    else:
        jackets[item]['Formal'] = False
        
    print 'Is it waterproof? yes/no'
    decision = (raw_input())
    if decision == 'yes':
        jackets[item]['Waterproof'] = True
    else:
        jackets[item]['Waterproof'] = False
        
    print jackets


def add_jumper():
    item = len(jumpers)+1
    jumpers[item] = {}
    print 'What is the name of the item?'
    name = (raw_input())
    jumpers[item]['Name'] = name

    print 'is it a hoodie or a jumper?'
    item_type = (raw_input())
    if item_type == 'hoodie':
        jumpers[item]['Type'] = 'hoodie'
    else:
        jumpers[item]['Type'] = 'jumper'
        
    print 'What colour is the item?'
    colour = (raw_input())
    jumpers[item]['Colour'] = colour

        #Don't need to ask if it's formal as jumpers are taken as formal at all times, may change.

def add_tee():
    item = len(tees)+1
    tees[item] = {}

    print 'What is the name of the item?'
    name = (raw_input())
    tees[item]['Name'] = name

    print 'Is it short/long sleeve?'
    item_type = (raw_input())
    if item_type == 'short':
        tees[item]['Type'] = 'short sleeved'
    else:
        tees[item]['Type']= 'long sleeved'
    
    print 'What colour is the item?'
    colour = (raw_input())
    tees[item]['Colour'] = colour

    print 'Is it formal? yes/no'
    decision = (raw_input())
    if decision == 'yes':
        tees[item]['Formal'] = True
    else:
        tees[item]['Formal'] = False

def add_bottoms():
    item = len(bottoms)+1
    bottoms[item] = {}

    print 'What is the name of the item?'
    name = (raw_input())
    bottoms[item]['Name'] = name

    print 'Are they shorts or trousers?'
    item_type = (raw_input())
    if item_type == 'shorts':
        bottoms[item]['Type'] = 'shorts'
    else:
        print 'Are they cargos/workpants?'
        item_type = (raw_input())
        if item_type == 'yes':
            bottoms[item]['Type'] = 'workpants'
        else:
            bottoms[item]['Type'] = 'genericpants'

    print 'Are they comfortable?'
    comfortable = (raw_input())
    if comfortable == 'yes':
        bottoms[item]['Comfortable'] = True
    else:
        bottoms[item]['Comfortable'] = False

    print 'What colour is the item?'
    colour = (raw_input())
    bottoms[item]['Colour'] = colour


def add_socks():
    item = len(socks)+1
    socks[item] = {}

    print 'What colour is the item?'
    colour = (raw_input())
    socks[item]['Colour'] = colour


def add_shoes():
    item = len(shoes)+1
    shoes[item] = {}

    print 'What is the name of the item?'
    name = (raw_input())
    shoes[item]['Name'] = name

    print 'Are they a trainer/sandal/boot?'
    item_type = (raw_input())
    if item_type == 'trainer':
        shoes[item]['ModelType'] = 'trainer'
    elif item_type == 'sandal':
        shoes[item]['ModelType'] = 'sandal'
    elif item_type == 'boot':
        shoes[item]['ModelType'] = 'boot'
    
    print 'Is the item chunky?'
    chunky = (raw_input())
    if chunky == 'yes':
        shoes[item]['Chunky'] = True
    else:
        shoes[item]['Chunky'] = False


       
def suggest_outfit():#Needs an overhaul
    temp_average = sum(temp)/len(temp)
    windspeed_average = sum(wind_speed)/len(wind_speed)
    hatlength = len(hats)


    if 'Rain' in description:
        print '\n','It is raining today...'

    if temp_average <10:
        print '\n''COLD day today...jacket receommended...'
    elif temp_average >10 and temp_average <15:
        print '\n','MILD day today...Could definetly need a jumper today...'
    elif temp_average >15 and temp_average <20:
        print '\n','QUITE warm...Consider a tshirt and some trousers...'
    elif temp_average > 20:
        print '\n','VERY warm...Shorts and tshirt are a must...'

    rand = random.randint(0,hatlength)
    #print hats.items()
    print 'Hat: '
    if rand == 0:
        print 'No hat'
    else:
        print random.choice(list(hats))
    pass

    print 'Are you going to be inside/outside?'
    location = (raw_input())
    if location == 'inside':#Inside weather matters less but temp still matters
        print 'is it relaxed or more formal?'
        situation = (raw_input())
        if situation == 'relaxed':
            pass
            #Loop through hats-pick,jumpers-pick...
        else:
            print 'Wow'
            pass
            #Loop through only picking formal-True items...
    
    elif location == 'outside':
        print 'Will you be outside for an extended period of time?'
        response = (raw_input())
        if response == 'yes':
            pass

        else:
            pass
            
    

    #Take data from the forecast and suggest an outfit.



if __name__ == '__main__':
    get_data()
    #load clothes file
    #print data
    choice = 0
    '''print hats,'\n'
    print jackets,'\n'
    print jumpers,'\n'''
    while True:
        print '*****************************************************************'
        print 'Please choose an option:'
        print '1.Get forecast...','\n','2.Get weather averages (24 HRS)...','\n','3.Add clothing item to list...','\n','4.Suggest outfit...','\n','5.Close...'
        print '*****************************************************************'
        choice = int(raw_input())
        if choice == 1:
            get_forecast()
        elif choice == 2:
            get_averages()
        elif choice == 3:
            add_clothing()
        elif choice == 4:
            suggest_outfit()
        else:
            break

#Please answer all questions as is asked, and with lower case unless stated otherwise.
