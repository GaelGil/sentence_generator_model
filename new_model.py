import re



def create_sentence(tokens_dictionary:dict, starting_word='the', SENTENCE_LENGTH = 10)->str:
    """
    This function takes in a dictionary as its argument
    and populates the list sentence with 10 words that
    come after the keyword and the word after that.
    """
    sentence_list = []
    SPACE = ' '
    # print()
    for i in range(SENTENCE_LENGTH):
        sentence_list.append(starting_word)
        starting_word = random.sample(tokens_dictionary[starting_word], 1)[0]
        sentence = SPACE.join(sentence_list)
    return ("it worked")


def findMax():
    """
    """
    maxVal = 0
    return maxVal


def getWord(word, wordsDict):
    """
    """
    maxVal = 0
    print(wordsDict)

    return "yes"


def compose_sentence(wordsDict:str, SENTENCE_LENGTH = 10) -> str:
    # highest occruing word
    # starting_word = 
    sentence_list = []
    SPACE = ' '
    if "the" in wordsDict:
        starting_word = "the"
    else:
        starting_word = next(iter(wordsDict))
    # print(next(iter(wordsDict)))
    for i in range(SENTENCE_LENGTH):
        sentence_list.append(starting_word)
        starting_word = getWord(starting_word, wordsDict[next(iter(wordsDict))])

    sentence = SPACE.join(sentence_list)
    return sentence


def count_words(words_list:list) -> dict:
    """
    This function 
    
    Parameters
    ----------
    words_list: list
        A list of all the words
    Returns
    -------
    dict
        A dictionary with words as keys and the occurance of the word 
        as its value.
    """
    # initalize new dictionary to hold words and their occurances
    occurance_of_words = {}

    for i in range(len(words_list)):
        word = words_list[i]
        if word in occurance_of_words:
            # add 1 if word is already in there
            occurance_of_words[word] += 1
        else:
            # add new value and set to 1 if its a new word
            occurance_of_words[word] = 1


    return occurance_of_words


def create_probabilites(words_dict:dict):
    """
    This function 
    
    Parameters
    ----------
    words_list: list
        A list of all the words
    Returns
    -------
    dict
        A dictionary with words as keys and the occurance of the word 
        as its value.
    """
    new_dict = {}
    for word in words_dict:
        # calling function to count words
        new_dict_val = count_words(words_dict[word])
        # setting new key and value
        new_dict[word]= [new_dict_val]


    return new_dict




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



def clean_data(text:str):
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

tokens, tokens_index = clean_data("Suspected gunman in David Ortiz's shooting wanted for armed robberies in New Jersey By Patrick Oppmann, Nicole Chavez and Madeline Holcombe, CNN Updated 11:46 PM ET, Thu June 13, 2019 david ortiz shooting oppmann pkg vpx_00001104 Now Playing How the shooting of... Eli_Gregg_and_his_mother,_Jimmy_Russell,_recovering_at_the_hospital_following_his_injury This teenager survived a knife that impaled his face Iran official: US and Iran headed toward confrontation Youngest known child separated at border was 4 months old Anderson Cooper&#39;s mother Gloria Vanderbilt is an American artist, designer, author, actress, and member of the Vanderbilt family of New York. Anderson Cooper pays tribute to his mom, Gloria Vanderbilt Trump asks Mulvaney to leave ABC interview for coughing Former diplomat: Trump administration used funds to threaten activists 1 killed at graduation party shooting in Philadelphia Thousands of protesters dressed in black take part in a new rally against a controversial extradition law propos, 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. 1:3 And God said, Let there be light: and there was light. 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. 1:3 And God said, Let there be light: and there was light. 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. 1:3 And God said, Let there be light: and there was light.")
words_dict = create_dict(tokens, tokens_index)
some_dict = (create_probabilites(words_dict))
print(compose_sentence(some_dict))
