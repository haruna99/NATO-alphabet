import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}


def create_phonetics():
    words = input("Enter a word: ")
    try:
        word_list = [new_dict[word] for word in words.upper()]
    except KeyError:
        print("Sorry, only letters of the alphabet please.")
        create_phonetics()
    else:
        print(word_list)


create_phonetics()
