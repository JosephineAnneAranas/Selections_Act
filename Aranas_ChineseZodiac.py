def chinese_zodiac(birth_year):
    zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog",
                      "Pig"]

    if birth_year >= 1900:
        zodiac_sign = zodiac_animals[(birth_year - 1900) % 12]
        return f" Your Chinese zodiac sign: {zodiac_sign}"
        # Where f is an F-String for allowing values of the variable zodiac_animals
    else:
        return "Invalid Year number! Chinese zodiac signs are limited from the year 1900s onwards."


# Prompt the user with their birth year
birth_year = eval(input("Enter your birth year: "))
result = chinese_zodiac(birth_year)

print(result)