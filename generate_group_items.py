import csv
from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="pcya_thingifier_generator")

print(""" 
<!DOCTYPE html>

<html>
  <head>
    <title>Weekly and Regular Gatherings | Philadelphia Christian Young Adults</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
  </head>
  <body>
    <h1>REGULAR GATHERINGS</h1>
    <a class="docs-link" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vQkcA5GraBjDAKgaHIo1tgUxxHYigHt-6hjMJrquKLe2y6b0GtvOI8PHVnRs9GjQvKsXuLoOeIabCCv/pubhtml">Google Sheets Document With Below Information</a>
    <div id="church-list">""")

with open ('sheet.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    first = True
    for row in spamreader:
        if first == True:
            first = False
            continue
        name = row[0]
        website = row[1]
        county = row[2]
        state = row[3]
        address = row[4]
        monday = row[5]
        tuesday = row[6]
        wednesday = row[7]
        thursday = row[8]
        print('<div class="church-item">')
        print('  <h2>{}</h2>'.format(name))
        print('  <img src="{}.jpg"></img>'.format(name))
        print('  <table>')
        print('    <tr><td>Website</td><td><a href="{}">{}</a></td></tr>'.format(website, website))
        print('    <tr><td>County</td><td>{}</td></tr>'.format(county))
        print('    <tr><td>Address</td><td>{}</td></tr>'.format(address))
        print('  </table>')
        print('  <h5 class="meeting-times">Weekly Meeting Times</h5>')
        print('  <table>')
        if (monday.strip() != ''):
            print('    <tr><td>Monday</td><td>{}</td></tr>'.format(monday))
        if (tuesday.strip() != ''):
            print('    <tr><td>Tuesday</td><td>{}</td></tr>'.format(tuesday))
        if (wednesday.strip() != ''):
            print('    <tr><td>Wednesday</td><td>{}</td></tr>'.format(wednesday))
        if (thursday.strip() != ''):
            print('    <tr><td>Thursday</td><td>{}</td></tr>'.format(thursday))
        print('  </table>')
        print('</div>')
        print('')

print("""
    </div>
    <a href="index.html">Home</a>
  </body>
</html>""")
