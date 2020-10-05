import csv
import matplotlib.pyplot as plt
import numpy as np




from functools import reduce

with open("Emissions.csv", 'rt') as f:
    data = csv.reader(f)
    dictData = {}
    
    for row in data:
    #    dictData.update({str(row[0]), row[1:]})
 #       print(type(row[0]))
         dictData[row[0]] = row[1:]
#        print(row)

#print(dictData)

for key, value in dictData.items():
#    print(key, end="-")
#    print(value)
     pass
ok = False
while not ok:
    year = input("Select a year to find statistics:(1997, 2010)")
    try:
        if int(year) >= 1997 and int(year) <= 2010:
            ok = True
        else:
            print("The year should be between 1997 and 2010")
    except ValueError:
        print("Enter a number, please")
#print(year)

yearList = {}

index = int(year) - 1997

for key, value in dictData.items():
    yearList.update({key:value[index]})


#print(yearList)

del yearList["CO2 per capita"]

#print(yearList)
#yearList = yearList[1:]

#print(yearList)

maxEmission = 0
maxCountry = ""
for country, emission in yearList.items():
    if maxEmission < float(emission):
        maxEmission = float(emission)
        maxCountry = country

print("Country with max emission is{}: {}".format(maxCountry,maxEmission))

print("Max Emission:{}".format(maxEmission))

minEmission = 100
minCountry = ""

for country, emission in yearList.items():
    if minEmission > float(emission):
        minEmission = float(emission)
        minCountry = country
print("Country with min emission is: {}: {}".format(minCountry, minEmission))

averageEmission = reduce(lambda x, y: float(x) + float(x), yearList.values()) / len(yearList)

print("Average emission:{}".format(averageEmission))

index = 0

country1 = input("Enter first country please:")

emissionsCountry1 = dictData[country1]

x = []

for year in range(1997, 2011,1):
    x.append(year)

y = []

for index in range(len(x)):
    y.append( float(emissionsCountry1[x[index]-1997]))

country2 = input("Enter second country please:")

emissionsCountry2 = dictData[country2]

z = []

for index in range(len(x)):
    z.append( float(emissionsCountry2[x[index]-1997]))

plt.plot(x, y, label=country1)
plt.plot(x, z, label = country2)


plt.legend()
# Show the plot
plt.show()

