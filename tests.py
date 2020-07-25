from model import create_sentence, create_dict, clean_data, make_sentence


# Test create_sentence

# Test create_dict

# Test clean_data
messy_data = """
this . test ;;  has a lot %%% OF junkkk that shou l d be removed.
"""

assert clean_data(messy_data) == "this test has a lot of junkkk that shou be removed"


# Test make_sentence
my_string = """
    1:2 And the !# earth was without $ form,
    and void; and *()@ darkness was upon,
    {  the } face of the deep. And the +  
    Spirit of God moved upon the face of the = waters. - 1:3 And
    God said, Let there be light: and there was light.
    """

assert make_sentence(my_string) == something
