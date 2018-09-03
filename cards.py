#!/usr/bin/python

foo = input("Enter the cards in order and divide them by a comma: ")
print (foo)
cards = foo.split(',')
for i in range(0,len(cards)):
    if (cards[i].isdigit()):
        print("het werkt")
