
#gets number of words from text
def get_num_words(txt_1):
    count=0
    txt_2=txt_1.split()
    for i in txt_2:
        count+=1
    return count

#gets number of times a character occured in text

def get_char_from_text(txt):
    text = txt.lower()
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

def sort_characters_by_count(char_dict):

    char_list = [
        {"char": char, "num": count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]

    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list