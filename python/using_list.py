#!/usr/bin/python

shoplist=['apple','mongo','carrot','banana']

print 'I have ',len(shoplist),' items to purchase.'

print 'These items are:'

for item in shoplist:
	print item,

print "\nI also want to buy rice."

shoplist.append("rice")

print 'My shopping list now is ',shoplist,'.'

print "I will sort my list now ."
shoplist.sort()
print "Sorted shopping list is",shoplist,'.1'

print "The first thing i want to buy is",shoplist[0],'.'
olditem=shoplist[0]
del shoplist[0]
print 'I bought the ',olditem,'.'
print 'My shopping list is now ',shoplist,'.'