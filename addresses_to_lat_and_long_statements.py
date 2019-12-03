import csv
from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="pcya_thingifier_generator")

metadata = {}
with open ('sheet.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    first = True
    for row in spamreader:
        if first == True:
            first = False
            continue
        name = row[0]
        metadata[name] = row

with open ('coordinates.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    first = True
    i = 0
    for row in spamreader:
        church_name = row[0]
        latitude = row[1]
        longitude = row[2]
        meta = metadata[church_name]
        website = meta[1]
        county = meta[2]
        state = meta[3]
        address = meta[4]
        monday = meta[5]
        tuesday = meta[6]
        wednesday = meta[7]
        thursday = meta[8]
        if (monday.strip() != ''):
            monday = '<p>Monday {}<p>'.format(monday)
        if (tuesday.strip() != ''):
            tuesday = '<p>Tuesday {}<p>'.format(tuesday)
        if (wednesday.strip() != ''):
            wednesday = '<p>Wednesday {}<p>'.format(wednesday)
        if (thursday.strip() != ''):
            thursday = '<p>Thursday {}<p>'.format(thursday)
        print('var marker{} = L.marker([{}, {}]).addTo(map);'.format(i, latitude, longitude))
        print('marker{}.bindPopup("<b>{}</b><div><a href=\\\"{}\\\">{}</a></div><p>{}</p>{}{}{}{}");'.format(i, church_name, website, website, address, monday, tuesday, wednesday, thursday))
        i += 1
