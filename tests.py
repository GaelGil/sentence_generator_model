from model import create_sentence, create_dict, clean_data, make_sentence


# Test create_sentence


# Test create_dict


# Test clean_data
messy_data = """
this . test ;;  has a lot %%% OF junkkk that shou l d be removed.
"""

assert clean_data(messy_data) == "this test has a lot of junkkk that shou be removed"


# Test make_sentence


