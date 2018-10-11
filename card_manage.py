# !/usr/bin/env python
# -*- coding:utf-8 -*-

cards = [{"name": "a", "phone_num": "123123", "addr": "qap"}, {"name": "b", "phone_num": "321321", "addr": "U"}]


# Define function list
def print_menu():
    print("="*50)
    print("1. addr a new card")
    print("2. delete a card")
    print("3. Modify a card")
    print("4. Inquire all the cards")
    print("5. Exit")
    print("="*50)


# Show the cards
def print_cards():
    i = 1
    print("num\tname\tphone_num\taddr")
    for card in cards:
        print("%d\t%s\t%s\t%s" % (i, card["name"], card["phone_num"], card["addr"]))
        i += 1


# addr a new card
def add_new_card():
    new_name = input("Enter the name: ")
    new_phone_num = input("Enter the phone number：")
    new_add = input("Enter the address：")

    # Define a new dictionary to store a card
    new_card = dict()
    new_card['name'] = new_name
    new_card['phone_num'] = new_phone_num
    new_card['addr'] = new_add
    # print(new_card)  for test

    cards.append(new_card)
    # print(cards)  for test


# Delete the select card
def del_card():
    print_cards()
    num = int(input("Select a number which you want to operate the card："))
    del cards[num - 1]


def main():
    while True:
        print_menu()
        num = int(input("Select the feature you want: "))
        if num == 1:
            add_new_card()

        elif num == 2:
            del_card()
            print("Succeed！")

        elif num == 3:
            del_card()
            add_new_card()
            print("Succeed")

        elif num == 4:
            print_cards()

        elif num == 5:
            break

        else:
            print("You enter a wrong number,please enter a correct number!")


main()

"""
@author: panxs
@data:2018/10/9 0009 22:01
"""