###
### Author: Amimul Ehsan  Zoha
### Course: CS110
### Description: A program that reads in a a text file which can be a
### a part of a book poem or any text and draws a graphical canvas
### containing various info of the text file like the most used words
### of different sizes, capitalized and punctuated words ratios (for extra credit)
### with the help of bars and different colors.
###
def word_list(file_name):
    '''
    This function opens and reads in the file input the user and
    returns the words of the file in a list
    file name name: a str which is the file to be used for infograph
    '''
    file= open(file_name,'r')
    words_lst=[]
    #for loops which iterates through the file and appends the words into a list
    for line in file:
        # stripping of the newline character and splitting in spaces
        line= line.strip('\n').split()
        for i in range(0,len(line)):
            words_lst.append(line[i])
    return words_lst

def count_dict(words_lst):
    '''
    This function loops through the words list and creates a dictionary
    containing the unique words as keys and the occurences as values
    returns the above described dictuonary and the number of unique words.
    words_lst: a list containing the words of the text file
    '''
    words_dict={}
    #for loop which loops through the words list and checks and adds those words
    # in the dictionary and the number of times they appeared.
    for i in words_lst:
        if i not in words_dict:
            words_dict[i]=0
        words_dict[i]+=1
    total_unique_words=len(words_dict)
    #return  the word dictioanry and the total_unique_words
    return words_dict, total_unique_words

def most_occurance(words_dict):
    '''
    This function calculates the most times each type of words appears in
    the text file and returns the word and the number of times they appeared
    for each case.
    words_dict: a dictionary containing the unique words as keys and the occurences as values
    '''
    small_word_occurance=0
    medium_word_occurance=0
    large_word_occurance=0
    #for loop which loops through the dictionary and checks for each type of word according to
    # the specified size in the spec
    for word, occurences in words_dict.items():
        # if statements to classify the different type of words according to lengths
        if len(word)<=4:
            if small_word_occurance < words_dict[word]:
                most_used_small_word = word
                small_word_occurance = words_dict[word]

        elif len(word)>= 5 and len(word)<=7:
            if medium_word_occurance < words_dict[word]:
                most_used_medium_word = word
                medium_word_occurance = words_dict[word]

        elif len(word)>= 8 :
            if large_word_occurance < words_dict[word]:
                most_used_large_word = word
                large_word_occurance = words_dict[word]
    # The calculated info is displayed in the following way as a string to match spec
    small_word_occurance = ' ' + '(' + str(small_word_occurance) + 'x' + ')' + ' '
    medium_word_occurance = ' ' + '(' + str(medium_word_occurance) + 'x' + ')' + ' '
    large_word_occurance = ' ' + '(' + str(large_word_occurance) + 'x' + ')' + ' '
    # returns the word and the number of times they appeared for each case.
    return small_word_occurance,most_used_small_word, medium_word_occurance, \
    most_used_medium_word ,large_word_occurance, most_used_large_word

def count_capitalized(words_dict):
    '''
    This function returns (counts) the capitalized and non capitalized unique words of the text
    words_dict:a dictionary containing the unique words as keys and the occurences as values
    '''
    # a list containing the unique words of the text file is created using a for loop
    unique_word_list=[]
    for word,occurences in words_dict.items():
        if word not in unique_word_list:
            unique_word_list.append(word)
    capitalized_count=0
    non_capitalized_count=0
    # looping through the list and determining the capitalized and non capitalized words
    for word in unique_word_list:
        if word[0].isupper()==True:
            capitalized_count+=1
        elif word[0].isupper()==False:
            non_capitalized_count+=1
    # returns the number (int) of capitalized and non capitalized words
    return capitalized_count, non_capitalized_count

def punctuation_count(words_dict):
    '''
    This function returns (counts) the punctuated and non punctuated unique words of the text
    words_dict:a dictionary containing the unique words as keys and the occurences as values
    '''
    # a list containing the unique words of the text file is created using a for loop
    unique_word_list=[]
    for word,occurences in words_dict.items():
        if word not in unique_word_list:
            unique_word_list.append(word)
    punctuated=0
    non_punctuated=0
    # looping through the list and determining he punctuated and non punctuated unique words
    for word in unique_word_list:
        if word[-1]== '.' or word[-1]==',' or word[-1]=='?' or word[-1]=='!' :
            punctuated+=1
        else:
            non_punctuated+=1
    # returns the number (int) of capitalized and non capitalized words
    return punctuated, non_punctuated



def word_count(words_dict):
    '''
    This function counts the number of different type(small medium and large) words of the
    text file and returns the number as ints
    words_dict: dictionary containing the unique words as keys and the occurences as values
    '''
    small_word_count=0
    medium_word_count=0
    large_word_count=0
    # for loop which loops through the dictionary and counts the number of words of each type
    for word,occurences in words_dict.items():
        if len(word)<=4:
           small_word_count+=1
        elif len(word)>= 5 and len(word)<=7:
           medium_word_count+=1
        elif len(word)>= 8 :
           large_word_count+=1
    # returns the number of times each type appeared
    return small_word_count,medium_word_count,large_word_count

def word_length_bar(gui,small_word_count,medium_word_count,large_word_count):
    '''
    This function draws the bar which represents the count of different
    lengths of words appearing in the text file
    gui: a graphical canvas. Drawing in it.
    small_word_count: number of unique small words appearing in the text.
    medium_word_count: number of unique medium words appearing in the text.
    large_word_count: number of unique large words appearing in the text.
    '''
    total_unique_words= small_word_count+ medium_word_count + large_word_count
    # calculating the height of the rectangle each type will take according to proportion
    small_word_portion= (small_word_count/total_unique_words)* 450
    medium_word_portion= (medium_word_count/total_unique_words)* 450
    large_word_portion= (large_word_count/total_unique_words)* 450
    # Drawing the bar according to the calcuated porportion with rectangles and text
    gui.text(30, 170, 'Word lengths','white', 17)
    gui.rectangle(33,200,133,small_word_portion,'blue')
    gui.text(37,204,'small words','white',10)
    gui.rectangle(33,200+small_word_portion,133,medium_word_portion,'green')
    gui.text(37,204+small_word_portion, 'medium words', 'white',10)
    gui.rectangle(33,200+small_word_portion+medium_word_portion,133,large_word_portion,'red')
    gui.text(37,204+ small_word_portion+medium_word_portion, 'large words', 'white', 10)

def capitalized_bar(gui,capitalized_count, non_capitalized_count):
    '''
    This function draws the bar which represents the capitalized info of different
    words appearing in the text file
    gui: a graphical canvas. Drawing in it.
    capitalized_count: number of unique capital words appearing in the text.
    non_capitalized_count: number of unique non capitalized words appearing in the text.
    '''
    total_words = capitalized_count + non_capitalized_count
    # calculating the height of the rectangle each type will take according to proportion
    capitalized_portion= (capitalized_count / total_words) * 450
    non_capitalized_portion= (non_capitalized_count / total_words) * 450
    # Drawing the bar according to the calcuated porportion with rectangles and text
    gui.text(250, 170, 'Cap/Non-Cap','white', 17)
    gui.rectangle(250,200,133,capitalized_portion,'blue')
    gui.text(255,204,'Capitalized','white',10)
    gui.rectangle(250,200+capitalized_portion,133,non_capitalized_portion,'green')
    gui.text(255,204+capitalized_portion,'Non Capitalized','white',10)

def punctuated_bar(gui,punctuated,non_punctuated):
    '''
    This function draws the bar which represents the punctuation info of different
    words appearing in the text file
    gui: a graphical canvas. Drawing in it.
    punctuated: number of unique punctuated words appearing in the text.
    non_punctuated: number of unique non_punctuated words appearing in the text.
    '''
    total_word= punctuated + non_punctuated
    # calculating the height of the rectangle each type will take according to proportion
    punctuated_portion = (punctuated/total_word) * 450
    non_punctuated_portion = (non_punctuated/total_word) * 450
     # Drawing the bar according to the calcuated porportion with rectangles and text
    gui.text(470, 170, 'Punct/Non-Punct' , 'white', 17)
    gui.rectangle(470,200,133,punctuated_portion,'blue')
    gui.text(475,204,'Punctuated','white',10)
    gui.rectangle(470,200+punctuated_portion,133,non_punctuated_portion,'green')
    gui.text(475,204+ punctuated_portion,'Non Punctuated','white',10)


def main():
    '''
    This function calls all the other functions to accomplish the program.
    '''
    #importing the graphics module
    from graphics import graphics
    #user input file to draw the infograph of
    file_name=input('Enter file name:\n')
    words_lst=word_list(file_name)
    # calling the appropriate functions to get the values returned by each.
    words_dict, total_unique_words = count_dict(words_lst)
    small_word_count,medium_word_count,large_word_count= word_count(words_dict)
    small_word_occurance,most_used_small_word, medium_word_occurance, \
    most_used_medium_word ,large_word_occurance, most_used_large_word = most_occurance(words_dict)
    capitalized_count, non_capitalized_count = count_capitalized(words_dict)
    punctuated, non_punctuated = punctuation_count(words_dict)
    # drwaing the canvas
    gui= graphics(650,700,'infographic')
    gui.rectangle(-10,-10,670,720,'grey10')
    gui.text(33,35,file_name,'cyan2',20)
    # drawing the info in the canvas using gui.text function
    gui.text(33,85,'Total Unique Words: ' + str(total_unique_words), 'white', 18)
    gui.text(33,133,'Most used words(s/m/l): ', 'white',14)
    gui.text(250,133, most_used_small_word + small_word_occurance + \
    most_used_medium_word + medium_word_occurance +
    most_used_large_word + large_word_occurance, 'cyan2', 14)
    # calling the functions to draw the three bars
    word_length_bar(gui,small_word_count,medium_word_count,large_word_count)
    capitalized_bar(gui,capitalized_count, non_capitalized_count)
    punctuated_bar(gui,punctuated,non_punctuated)

main()