def word_count(text):
    split = text.split()
    return len(split)

def char_count(text):
    words = text.lower()
    word_dict = {}
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict

def func3(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    return sorted_list
    
        


