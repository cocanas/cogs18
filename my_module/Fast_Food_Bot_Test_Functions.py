from my_module.Fast_Food_Bot_Functions import *


def test_string_concatenator():
    # Testing string_concatenator
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('bye', 'planet', ' '), str)
    assert string_concatenator('bye', 'planet', ' ') == 'bye planet'
    
def test_prepare_text():
    # Testing prepare_text
    assert callable(prepare_text)
    assert isinstance(prepare_text('One two three.'), list)
    assert prepare_text('What! Okay, LOL.') == ['what', 'okay', 'lol']
    
    
def test_list_to_string():
    # Testing list_to_string
    assert callable(list_to_string)
    assert isinstance(list_to_string(['one', 'two'], '/'), str)
    assert list_to_string(['one', 'two'], '/') == 'one/two'
    
def test_end_chat():
    # Testing end_chat
    assert callable(end_chat)
    assert isinstance(end_chat(['one', 'two']), bool)
    assert end_chat(['quit', 'bye']) == True
    
def test_is_in_list():
    # Testing is_in_list
    assert callable(is_in_list)
    assert isinstance(is_in_list(['hello', 'bye'],['hello','bye','hi','lol']),bool)
    assert is_in_list(['hello', 'bye'],['hello','bye','hi','lol']) == True
    
def test_is_Pizza():
    # Testing is_Pizza
    assert callable(is_Pizza)
    assert isinstance(is_Pizza(['hamburgers']),bool)
    assert is_Pizza(['hamburgers']) == False 

def test_is_Hamburgers():
    # Testing is_Hamburgers
    assert callable(is_Hamburgers)
    assert isinstance(is_Pizza(['hamburgers']),bool)
    assert is_Pizza(['hamburgers']) == True
    
def test_is_Tacos():
    # Testing is_Tacos
    assert callable(is_Tacos)
    assert isinstance(is_Tacos(['tacos']),bool)
    assert is_Pizza(['tacos']) == True
    
def test_is_Wings():
    # Testing is_Wings
    assert callable(is_Wings)
    assert isinstance(is_Wings(['tacos']),bool)
    assert is_Pizza(['tacos']) == False 



    
                      
        