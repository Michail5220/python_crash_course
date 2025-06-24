#Functions

#ex1
def display_message():
    """Ch8, Ex1. Displayi simple message."""
    print("Learning a chapter on Functions!")

# display_message()

def favourite_book(title):
    """Ch8, Ex2. Display favourite book title."""
    print(f"One of my favourite books is {title}.")

# favourite_book('Idiot')

# def make_shirt(size, message):
#     """Ch8, Ex3. Display size of the t-shirt and the message printed on it"""
#     print(f"The size of the t-shirt is: {size}\n"
#           f"and the message says the following:\n{message}")

def make_shirt(size='large', message='I love Python'):
    """Ch8, Ex4. Display size of the t-shirt and the message printed on it
       Use default value in the parameters (not it is defined last among the parameters)
    """
    
    print(f"The size of the t-shirt is: {size}\n"
          f"and the message says the following: {message}")

# make_shirt() 
# make_shirt(message='I love Python more') 
# make_shirt('medium', 'My love for Python is limitless') 

def describe_city(city, country='UK'):
        """Ch8, Ex5. Print City and Country"""
        print(f"The {city} is in {country}")

# describe_city('Exeter')
# describe_city('Gloucester')
# describe_city('Vilnius','Lithuania')
    
def city_country(city, country):
     """Ch8. Ex6. Formatted city country"""
     full_name=(f"{city.title()}, {country.title()}")
     return full_name

# value = city_country('Vilnius', 'LITHUANIA')
# print(value)

def make_album(artist_name, album_title, song_num=None):
    """Ch8, Ex7. The function should return a dictionary describing the album
        Remember, None evalues to False
    """
    if song_num:
        album_dict = {'artist':artist_name, 'title': album_title, 'number of songs': song_num}
    else:
        album_dict = {'artist':artist_name, 'title': album_title}
    return album_dict

# album=make_album('The Beatles', 'Abbey Road')
# print(album)
# album=make_album('Michael Jackson', 'Thriller')
# print(album)
# album=make_album('Eagles', 'Hotel California')
# print(album)
# album=make_album('Metallica', 'Through the never',12)
# print(album)

# flag=True
# my_dict={}
# while flag:
#     title = input("please enter the title of the albmum: ")
#     if title != 'q':
#         artist = input("please enter the name of the artist: ")
#         if artist !='q':
#             my_dict=make_album(artist, title)
#         else:
#             flag=False
#     else:
#         flag=False
    

# print(my_dict)

#Ch8, Ex9.


def show_messages(sms_list):
    """print a list of short message"""
    sent_sms_list=[]
    #for sms in sms_list:
    #     removed_sms=sms_list.pop()     #do not use this approach, 
                                        #you remove the item from the list, but the index in the for loop stays the same
    
    #here I'm looping from large index to small, this way it works
    # for i in range(2,-1,-1):
    #     print(f"{i}: {len(sms_list)}: {sms_list[i]}")
    #     removed_val=sms_list.pop(i)
    #     sent_sms_list.append(removed_val)

    #the best way, however, is it to use while
    while sms_list:
         removed_val=sms_list.pop()
         sent_sms_list.append(removed_val)

    print("The following messages were sent: ")
    sent_sms_list.reverse()
    print(sent_sms_list)
        

# my_sms_list=['hi','hello','hiya']
# show_messages(my_sms_list)
# print(my_sms_list)

def make_sandwich(*toppings):
    """Ch8, Ex9. Function that uses arbitrary number of arguments"""
    for topping in toppings:
        print(f"making a sandwitch with {topping}")
        #  i=0
        #  while i<len(toppings):
        #       print(f"making a sandwitch with {toppings[i]}")
        #       i+=1


# make_sandwich('ham','cheese','butter','artichokes')
# make_sandwich('ham')

def build_profile(first, last, **user_info):
    """Ch8, Ex14. Build a dictionary containing everything we know about a user"""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

# user_profile = build_profile('john', 'bishop',
#                              profession='comedian',
#                              country=['US', 'UK'])
# print(user_profile)

def make_car(make, model, **user_inputs):
    car_config={}
    car_config['make'] = make
    car_config['model'] = model
    for user_key, user_value in user_inputs.items():
        car_config[user_key]=user_value
    return car_config

# my_car=make_car('ford','escort', low_suspension=True)
# print(my_car)


    

