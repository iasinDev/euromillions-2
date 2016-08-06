#!/bin/python
# -*- coding: utf-8 -*-
#__author__ = "Kevin Van den Brande"


import random
import sys
import time
from tweet_dm import tweet_direct_message
from internet import is_connected


#Tweet euromillions numbers


def euromillions():
    if is_connected()==True:
        generate_numbers()
        sys.exit()
    else:
        sys.exit()    


def generate_numbers():
    my_list1 = []                              
    my_list2 = []

    while len(my_list1) < 5:                    
        new_number = random.randrange(50)+1    
        if not new_number in my_list1:          
            my_list1.append(new_number)         

    while len(my_list2) < 2:
        new_stars = random.randrange(11)+1
        if not new_stars in my_list2:
            my_list2.append(new_stars)

    winners = sorted(my_list1)
    stars = sorted(my_list2)  
    str_winners = " ".join(str(i) for i in winners)
    str_stars = " ".join(str(j) for j in stars)
    numbers = "Euromillions: " + str_winners + " stars: " + str_stars
    
    send_tweet(numbers)


def send_tweet(lucky_numbers):
    contact_K = "@kvandenbrande"
    contact_L = "@ldvandenbrande"
    tweet_direct_message(contact_K,lucky_numbers)
    time.sleep(1)
    tweet_direct_message(contact_L,lucky_numbers)

   

euromillions()
