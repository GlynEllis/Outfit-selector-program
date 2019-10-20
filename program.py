import json
import random#Random when outfits have been added.
import requests
from collections import Counter#Used to count the weather descriptions in averages.

with open('clothing.txt','r') as incoming_data:
    clothing_informaion = json.load(incoming_data)

possible_choices = {}
final_outfit = {}
temp = []
wind_speed = []
description = []
hats = clothing_informaion[0]
jackets = clothing_informaion[1]
jumpers = clothing_informaion[2]
tees = clothing_informaion[3]
bottoms = clothing_informaion[4]
socks = clothing_informaion[5]
shoes = clothing_informaion[6]

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Stockholm&APPID=76852765b5d0777aa3af09938f379342")
forecast = r.json()

#Getting the weather data for the forecast.
def get_data():
    counter = 0
    while counter < 8:#Data is captured every 3 hours, 8 is a day(24hrs).
        temp.append(forecast['list'][counter]['main']['temp']-273.15) #Need to convert from kelvin to celcius.
        description.append(forecast['list'][counter]['weather'][0]['main'])
        wind_speed.append(forecast['list'][counter]['wind']['speed']*2.3)
        counter += 1
    
#Displaying the 24 hour forecast predictions. 
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
    
#Displaying the averages for the day.
def get_averages():
    print 'LOCATION:',forecast['city']['name']
    temp_average = sum(temp)/len(temp)
    print "AVERAGE TEMP:",'%.2f' % temp_average,'DEGREES'

    windspeed_average = sum(wind_speed)/len(wind_speed)
    print 'AVERAGE WINDSPEED:','%.2f' % windspeed_average,'MPH'

    print 'THE WEATHER DESCRIPTIONS FOR THE NEXT 24 HOURS:'
    print Counter(description).items()
    
#    for x in range(len(description)):
#        print '(',forecast['list'][x]['dt_txt'],')',description[x]
#    print '\n'

#The menu for adding new clothing items to the dictionary and viewing all stored clothing items.
def add_clothing():
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
        print'8.Show all clothes...'
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
        elif choice == 8:
            print 'HATS:'
            for items in hats:
                print hats[items]['Name'],hats[items]['Type']
            print '********************************************************'
            print 'JACKETS:'
            for items in jackets:
                print jackets[items]['Name']
            print '********************************************************'
            print 'JUMPERS:'
            for items in jumpers:
                print jumpers[items]['Name'],jumpers[items]['Type']
            print '********************************************************'
            print 'TEES:'
            for items in tees:
                print tees[items]['Name'],tees[items]['Type']
            print '********************************************************'
            print 'BOTTOMS:'
            for items in bottoms:
                print bottoms[items]['Name'],bottoms[items]['Type']
            print '*******************************************************'
            print 'SHOES:'
            for items in shoes:
                print shoes[items]['Colour'],shoes[items]['Name'],shoes[items]['ModelType']
        elif choice == 9:
            with open('clothing.txt', 'w') as outfile:  
                json.dump([hats,jackets,jumpers,tees,bottoms,socks,shoes], outfile)
            break
#A copy of the dictionary is made and the clothing items are added to it, once the user has added the clothing the orignal is then overwritten with the new copy. 
#This is fine small scale but if the data set were large then a different method would be more favourable.

    
#Items are added after the user selects the garment type and then answers a few basic questions which gives more complexity to each item when it comes to the decision making process. 
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

    print 'Is the item a button shirt?'
    button_shirt = (raw_input())
    if button_shirt == 'yes':
        tees[item]['Shirt'] = True
    else:
        tees[item]['Shirt'] = False

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

#Socks not implemented as they are too basic for now, can be added later.
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
    
    print 'Is it formal? yes/no'
    decision = (raw_input())
    if decision == 'yes':
        shoes[item]['Formal'] = True
    else:
        shoes[item]['Formal'] = False
    
    print 'What is the primary colour of the shoe?'
    colour = (raw_input())
    shoes[item]['Colour'] = colour

#The outfit is selected first by weather and then by the clothing attributes themselves as certain items will not work together, such as a button shirt and cargo pants.
#Once an item is chosen it is added to the final_outfit dictionary.
#As dictionaries are not ordered, a random entry is selected and if it fits the criteria for a cohesive outfit it is kept, if not another item is randomly selected.
def suggest_outfit():
    temp_average = sum(temp)/len(temp)
    windspeed_average = sum(wind_speed)/len(wind_speed)

    print 'Is the situation formal?...yes/no'
    answer = (raw_input())
    if answer == 'yes':# and temp_average > 15:
        final_outfit['Tee'] = random.choice(list(tees.items()))
        while final_outfit['Tee'][1]['Formal'] != True:
            final_outfit['Tee'] = random.choice(list(tees.items()))

        final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
        while final_outfit['Bottoms'][1]['Type'] != 'genericpants':
            final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
        
        final_outfit['Shoes'] = random.choice(list(shoes.items()))
        while final_outfit['Shoes'][1]['Formal'] != True:
            final_outfit['Shoes'] = random.choice(list(shoes.items()))
    else:    
        if temp_average <10:
            print '\n''COLD day today...jacket receommended...'
        
            final_outfit['Hat'] = random.choice(list(hats.items()))
            while final_outfit['Hat'][1]['Type'] != 'beanie':
                final_outfit['Hat'] = random.choice(list(hats.items()))
            final_outfit['Jacket'] = random.choice(list(jackets.items()))
            final_outfit['Jumper'] = random.choice(list(jumpers.items()))
            final_outfit['Tee'] = random.choice(list(tees.items()))
            while final_outfit['Tee'][1]['Shirt'] != False:
                final_outfit['Tee'] = random.choice(list(tees.items()))
            final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
            while final_outfit['Bottoms'][1]['Type'] == 'shorts':
                final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
    
            final_outfit['Shoes'] = random.choice(list(shoes.items()))

        elif temp_average >10 and temp_average <15:
            print '\n','MILD day today...Could definetly need a jumper today...\n'
            final_outfit['Hat'] = random.choice(list(hats.items()))
            final_outfit['Jumper'] = random.choice(list(jumpers.items()))
            final_outfit['Tee'] = random.choice(list(tees.items()))
            while final_outfit['Tee'][1]['Shirt'] != False:
                final_outfit['Tee'] = random.choice(list(tees.items()))
            final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
            final_outfit['Shoes'] = random.choice(list(shoes.items()))

    
        elif temp_average >15 and temp_average <20:
            print '\n','QUITE warm...Consider a tshirt and some trousers...'
            final_outfit['Hat'] = random.choice(list(hats.items()))
            final_outfit['Tee'] = random.choice(list(tees.items()))
            if final_outfit['Tee'][1]['Shirt'] == True:
                final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
                while final_outfit['Bottoms'][1]['Type'] == 'workpants':
                    final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
            else:
                final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
            final_outfit['Shoes'] = random.choice(list(shoes.items()))

        elif temp_average > 20:
            print '\n','VERY warm...Shorts and tshirt are a must...'
            final_outfit['Hat'] = random.choice(list(hats.items()))
            final_outfit['Tee'] = random.choice(list(tees.items()))
            final_outfit['Bottoms'] = random.choice(list(bottoms.items()))
            while final_outfit['Bottoms'][1]['Type'] != 'shorts':
                final_outfit['Bottoms'] = random.choice(list(bottoms.items()))

            final_outfit['Shoes'] = random.choice(list(shoes.items()))

    print 'OUTFIT: '#Need to sort printing the outfit/clearing the list after each suggestion.(Possibly pop it.)
    if 'Hat' in final_outfit and answer != 'yes':
        print final_outfit['Hat'][1]['Colour'],final_outfit['Hat'][1]['Name'],final_outfit['Hat'][1]['Type']

    if 'Jacket' in final_outfit:
        print final_outfit['Jacket'][1]['Colour'],final_outfit['Jacket'][1]['Name']
    if 'Jumper' in final_outfit and answer != 'yes':
        print final_outfit['Jumper'][1]['Colour'],final_outfit['Jumper'][1]['Name'],final_outfit['Jumper'][1]['Type']

    print final_outfit['Tee'][1]['Colour'],final_outfit['Tee'][1]['Name'],final_outfit['Tee'][1]['Type']
    print final_outfit['Bottoms'][1]['Colour'],final_outfit['Bottoms'][1]['Name'],final_outfit['Bottoms'][1]['Type']
    print final_outfit['Shoes'][1]['Name'],final_outfit['Shoes'][1]['ModelType']

#As a precaution if there is a descriptor of rain at any point in the forecast data over the 24 hour period a waterproof jacket is always suggested as an ad-on.
    if 'Rain' in description:
        final_outfit['Jacket'] = random.choice(list(jackets.items()))
        while final_outfit['Jacket'][1]['Waterproof']!= True:
            final_outfit['Jacket'] = random.choice(list(jackets.items()))
        print '\n','It is raining today...so consider an umbrella or:'
        print final_outfit['Jacket'][1]['Name']


#Main menu to access either the clothing or weather functions of the program.
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
        print '1.Get forecast...','\n','2.Get weather averages (24 HRS)...','\n','3.Add clothing item to/view list...','\n','4.Suggest outfit...','\n','5.Close...'
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
            quit
            break

#Please answer all questions as is asked, and with lower case unless stated otherwise.