import pymongo as pymongo
from  bson.objectid import ObjectId
import pprint

def print_hi(name):

     print(f'Hi, {name}')


def connectDB():
    client = pymongo.MongoClient(
        "mongodb+srv://diana:Qweasd123!@cluster0.oei8x.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    print(db.list_collection_names())
    countries = db.countries
    continents = db.continents

# # Question1
# # Get all the country where a letter or word given is in the name
    letter = input('Please enter a letter: ')
    def get_countries(countries, letter):
        result = countries.find({"name": {'$regex': letter, '$options': "i" }})
        for countries in result:
            pprint.pprint(countries)
    get_countries(countries, letter)
#
# # Question3
# # Send the list of continent with there number of countries
    for continent in continents.find():
        result = (continent['name'], len(continent['countries']))
        print(result)

# Question 4
# Send back the forth countries of a continent by alphabetic order

    def find_forth_country():
        result = {}
        for continent in continents.find():
            continent_countries = continent["countries"]
            continent_name = continent['name']
            for country in continent_countries:
                country_id = ObjectId(str(country))
                _country = countries.find({'_id': ObjectId(country_id)})[0]
                country_name = _country['name']
                if continent_name in result.keys():
                    if len(result[continent_name]) < 4:
                        result[continent_name].append(country_name)
                else:
                    result[continent_name] = [country_name]

            result[continent_name].sort()

        return result

    print(find_forth_country())

# # Question 6
# # Get all the countries order by number of people first the less populated and last the most populated
    def sorted_countries(countries):
        result = countries.find().sort('population')
        for countries in result:
            pprint.pprint(countries)
    sorted_countries(countries)
#
# # Question 7
# # Get countries which have a ‘u’ in their name and more 100 000 people inside
    def get_country(countries):
        result = countries.find(({"name": {'$regex': "u", '$options': "i"}, 'population': {'$gte': 100000}}))
        for countries in result:
            pprint.pprint(countries)
    get_country(countries)



if __name__ == '__main__':
    print_hi('PyCharm')
    connectDB()
