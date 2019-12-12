import string, random

# Functions from the A3 Chatbot assignment
def string_concatenator(string1, string2, separator):
    """ Concatenates two strings with a separator
    Parameters
    ----------
    
    string1: string
        the first string input
    string2: string
        the second string input
    separator: string
        the string that separates the strings
    Returns
    -------
    output: string
       two strings seperated by the seperator
       
    """
    output = string1 + separator + string2
    return output

def prepare_text(input_string):
    """ it makes the text lowercase, it seperates it into string and it removes    
    punctuation
    Parameters
    ----------
    
    input_string: string
        the text the user inputs
  
    Returns
    -------
    out_list: string
       the text the user input made lowercase, without punctuation and seperated 
       into strings
       
    """  
    out_list = []
    temp_string = ''
    temp_string = input_string.lower()
    out_list = temp_string.split()
    return out_list

def list_to_string (input_list, separator):
    """ Turns a list of strings back into one single concatenated string
    Parameters
    ----------
    
    input_list: string
        the text the user inputs
    separator: string
        what goes between the strings
  
    Returns
    -------
    output: string
       the list of strings modified into one single string
       
       
    """
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output

def end_chat (input_list):
    """ Ends chat if the user types 'bye' or 'quit'
    Parameters
    ----------
    
    input_list: string
        the text the user inputs
    Returns
    -------
    boolean:
        wheter it was true or false that the user typed 'bye' or 'quit'
           
    """
    for item in input_list:
        if item.lower() == 'quit' or item.lower() == 'bye':
            return True
        else: 
            return False
        
def is_in_list(list_one, list_two):
    """ Checks if an element from list_one appears in list_two
    ----------
    
    list_one: list
        the first list
    list_two: list
        the second list that is being checked to see if any element from the first 
        list is inside this one
  
    Returns
    -------
    boolean:
        Boolean wheter the element exists or not 
       
    """
    
    for element in list_one:
        if element in list_two:
            return True
    return False
    




# Functions I developed 
def introduction():
    # The FF Bots first lines   
    print("Hey, i'm the Fast Food Bot!")
    print("I'm here to help you pick where to eat")
    print("Which of the following sounds most appetizing to you: Pizza, Hamburgers, Tacos, or Wings?")
    
def is_Pizza(food_input):
    """ Checks if the input was 'pizza'
    Parameters
    ----------
    
    food_input: string
        user's input
        
    Returns
    -------
    Boolean:
        Boolean that determines if it was the expected input
    """
    
    check = ''
    check = list_to_string(food_input,' ')
    if check.lower() == 'pizza':
        return True
    return False

def is_Hamburgers(food_input):
    """ Checks if the input was 'hamburgers'
    Parameters
    ----------
    
    food_input: string
        user's input
        
    Returns
    -------
    Boolean:
        Boolean that determines if it was the expected input
    """
    check = ''
    check = list_to_string(food_input,' ')
    if check.lower() == 'hamburgers':
        return True
    return False

def is_Tacos(food_input):
    """ Checks if the input was 'tacos'
    Parameters
    ----------
    
    food_input: string
        user's input
        
    Returns
    -------
    Boolean:
        Boolean that determines if it was the expected input
    """
    check = ''
    check = list_to_string(food_input,' ')
    if check.lower() == 'tacos':
        return True
    return False

def is_Wings(food_input):
    """ Checks if the input was 'wings'
    Parameters
    ----------
    
    food_input: string
        user's input
        
    Returns
    -------
    Boolean:
        Boolean that determines if it was the expected input
    """
    check = ''
    check = list_to_string(food_input,' ')
    if check.lower() == 'wings':
        return True
    return False


#template from A3 Chatbot assignment 

def have_a_chat():
    """Main function to run the Fast Food Bot."""

    introduction()  
    chat = True
    generator = 0


    while chat:
        
        # Get a message from the user
        msg = input('')
        out_msg = None
        msg = prepare_text(msg)
        
        # Check if the input is 'pizza'
        pizza = is_Pizza(msg)
        
        # Check if the input is 'hamburgers'
        hamburgers = is_Hamburgers(msg)
        
        # Check if the input is 'tacos'
        tacos = is_Tacos(msg)
        
        # Check if the input is 'wings'
        wings = is_Wings(msg)
        
        # Check for an end msg 
        # Runs if user types 'quit' or 'bye'
        if end_chat(msg):
            out_msg = "It was nice chatting with ya!"
            chat = False
             
        # Runs if the user typed pizza
        # Gives a statement about their food choice
        # Generates a random pizza place for the user to go eat 
        elif pizza:
            out_msg = "MMM Pizzaaaa"   
            generator = 1
        
      
        # Runs if the user typed hamburgers
        # Gives a statement about their food choice
        # Generates a random hamburger place for the user to go eat 
        elif hamburgers:
            out_msg = "I love burgers! "
            generator = 2
            
        # Runs if the user typed tacos
        # Gives a statement about their food choice
        # Generates a random taco place for the user to go eat     
        elif tacos:
            out_msg = "It doesn't have to be Tuesday to eat Tacos"
            generator = 3
          
        # Runs if the user typed wings
        # Gives a statement about their food choice
        # Generates a random wings place for the user to go eat 
        elif wings:
            out_msg = "Wings always sound good."
            generator = 4
        # Outputs a random message if the user didn't type any of the food options listed          
        else:
            out_msg = random.choice(["sorry what?", "interesting", "i'm confused"])
        
        # Prints the response    
        print(out_msg)
        
        # Pizzas generator is 1, so it will randomly select a pizza place
        if generator is 1:
            return random.choice(['Pizza Hut it is', 'Dominos is the way to go', "Go to Papa John's Pizza!"])
        
        # Hamburgers generator is 1, so it will randomly select a pizza place
        elif generator is 2:
            return random.choice(["In&Out it is!", "Jack in the Box is the way to go", "go to McDonald's!"])
        
        # Tacos generator is 1, so it will randomly select a pizza place
        elif generator is 3:
            return random.choice(["Taco Bell it is!", "Del Taco is the way to go", "What about Jack in the Box?!"])
        
        # Wings generator is 1, so it will randomly select a pizza place
        elif generator is 4:
            return random.choice(["Buffalo Wild Wings it is!", "Wingstop is the way to go", "What about Hooters?!"])
        
                
        

 
        