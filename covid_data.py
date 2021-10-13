import urllib.request


def loadRSS():
    rssurl ='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumDeaths28DaysByDeathDate&format=csv'
    response = urllib.request.urlopen(rssurl)
    return response.readlines()


data = [line.decode('utf8') for line in loadRSS()]

list = []
for i in range(len(data)):
    new = ''
    for ch in data[i]:
        if ch == ',':
            list.append(new)
            new = ''
        elif ch == '\n':
            list.append(new)
            new = ''
        else:
            new += ch

scale = int(input("Enter scale: "))

scaled_death_number_list = []
for i in range(9, len(list), 5):
    scaled_death_number_list.append(int(list[i])//scale)

print(scaled_death_number_list)

