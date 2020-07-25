import random
import re


def create_sentence(tokens_dictionary:dict, starting_word='the', SENTENCE_LENGTH = 10)->str:
    """
    This function takes in a dictionary as its argument
    and populates the list sentence with 10 words that
    come after the keyword and the word after that.
    """
    sentence_list = []
    SPACE = ' '
    for i in range(SENTENCE_LENGTH):
        sentence_list.append(starting_word)
        starting_word = random.sample(tokens_dictionary[starting_word], 1)[0]
    sentence = SPACE.join(sentence_list)
    return sentence


def create_dict(tokens: list, tokens_index: list) -> dict:
    """
    This function 

    Parameters
    ----------
    text: str
        A string containing a large ammount of text
    Returns
    -------
    dict
        A dictionary with words as keys and a list of words that come 
        after it as value.
    """
    # initializing dictionary
    words_with_nearby = {}

    # set tokens as keys in dictionary
    for token in tokens_index:
        words_with_nearby[token] = []

    # get words that come after the token index
    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i + 1]
        words_with_nearby[current_word].append(next_word)

    return words_with_nearby

def clean_data(text: str) -> list:
    """
    This function takes in some big ammount of text as its argument, the function 
    then cleans it by removing some numbers, some punctuation and makes all words
    lowercase. Laslty this function returns two lists of words one containing 
    duplicates and the other with not containing duplicates.
    
    Parameters
    ----------
    text: str
        A string containing a large ammount of text
    Returns
    -------
    list, list
        Returns a list of all the words, returns a list of all non repeating words
    """
    # remove some punctuation
    cleaned = re.sub(r'[\.!#$%*()@,:/;"{}+=-]', ' ', text)
    
    # remove numbers
    clean_nums = re.sub(r'[0-9]', ' ', cleaned)
    
    # split up string
    tokens = clean_nums.split()
    
    #  make all words lowercase
    tokens = [token.lower() for token in tokens]
    
    # get a list of non repeating words
    tokens_index = list(set(tokens))

    return tokens, tokens_index


# def generate_sentence():
#     """
#     This function takes in no argument but it opens a text file and
#     puts it in varible data
#     """
#     with open('test_bible.txt', 'r') as file:
#         data = file.read().replace('\n', ' ')
#     return data


def make_sentence(book:str)->str:
    """
    This function takes in a book or text from
    the user and calls all the functions
    """
    tokens, tokens_index = clean_data(book)
    token_dictionary = create_dict(tokens, tokens_index)
    dictionary = create_sentence(token_dictionary)
    return dictionary

my_string = '1:2 And the !# earth was without $ form,   and void; and *()@ darkness was upon, {  the } face of the deep. And the +  Spirit of God moved upon the face of the = waters. - 1:3 And God said, Let there be light: and there was light.  '
print(make_sentence(my_string))

# def make_bible_sentence()-> str:
#     """
#     This function takes in no argument and is called once
#     and sets varianles to functions, those varibles are
#     turned into retrun values passed into the next function
#     """
#     the_book = generate_sentence()
#     tokens, tokens_index = clean_data(the_book)
#     token_dictionary = create_dict(tokens, tokens_index)
#     dictionary = create_sentence(token_dictionary)
#     return dictionary

# if __name__ == "__main__":
    # make_bible_sentence()