import random
import re


def create_sentence(tokens_dictionary: dict, starting_word="the", sentence_length = 10) -> str:
    """
    This function function uses a Markov decision process to sample words
    from a distribution. The `tokens_dictionary` argument is a dictionary that maps
    words to lists of words that follow them, effectively creating a sampling distribution.
    """
    sentence_list = []

    if starting_word not in tokens_dictionary.keys():
        tokens_dictionary[starting_word] = [list(tokens_dictionary.keys())[0]]

    # Sample words from the distribution using a Markov decision process.
    try:
        for _ in range(sentence_length):
            sentence_list.append(starting_word)
            starting_word = random.sample(tokens_dictionary[starting_word], 1)[0]
    except ValueError: # happens when we access the last word from data, if it's unique
        sentence_list.append("the")
        starting_word = "the"

    sentence = " ".join(sentence_list)

    return sentence


def create_dict(tokens: list, tokens_index: list) -> dict:
    """
    This function ...

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
    # Initializing dictionary
    words_with_nearby = {}

    # Set tokens as keys in dictionary
    for token in tokens_index:
        words_with_nearby[token] = []

    # Get words that come after the token index
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


def make_sentence(book: str) -> str:
    """
    This function takes in a book or text from
    the user and calls all the functions
    """
    tokens, tokens_index = clean_data(book)
    token_dictionary = create_dict(tokens, tokens_index)
    dictionary = create_sentence(token_dictionary)

    return dictionary
