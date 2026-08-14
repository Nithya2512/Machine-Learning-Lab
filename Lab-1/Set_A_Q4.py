def highest_occurring_character(text):
    frequency = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in frequency:
                frequency[character] += 1
            else:
                frequency[character] = 1
    highest_character = ""
    highest_count = 0
    for character in frequency:
        if frequency[character] > highest_count:
            highest_count = frequency[character]
            highest_character = character
    return highest_character, highest_count
input_string = input("Enter a string: ")
character, count = highest_occurring_character(input_string)
print("Highest occurring character:", character)
print("Occurrence count:", count)