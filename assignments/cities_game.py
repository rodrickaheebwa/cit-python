# asks user to guess capital of a stated country
# choice of country is random
# tell user if they are correct or not
# keeps track of correct answers

import random, urllib.request, json

url = urllib.request.urlopen('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json')
data = json.load(url)

total_questions = 0
correct = 0

def generate_country(data):
    combination = random.choice(data)
    country = combination['country']
    capital = combination['city']
    return country, capital

while True:
    option = input("Enter 1 for a question or 2 to quit the game: ")
    try:
        option = int(option)
    except:
        print("Invalid option")
        continue

    if option == 1:
        country, capital = generate_country(data)
        user_answer = input(f"What is the capital city of {country}? : ")
        if user_answer.lower() == capital.lower():
            print("You got that correct")
            correct += 1
        else:
            print("You got that wrong")
            print(f"The correct answer is {capital}")
        total_questions += 1
    elif option == 2:
        print(f"You did {total_questions} questions and got {correct} of them correct")
        break
    else:
        print("Invalid option")