#############################################
#											                      #
#	Name: CSV column fusion      	            #
#	Date: 04/01				                        #
#   Ver: 1.0.0             					        #
#	- Combines two CSV rows 				          #
#	- Spaces and separates them with "///"	  #
#	- Counts and orders						            #
#	- Commented and notes added		            #
#   - First Python App                      #
#                                           #
#   Next Edits                              #
#   - Calc the mertial length               #
#   - Run with input CSV name               #
#	     									                    #
#############################################

import csv
import sys  

# Pass 1: gather related ProductNames and add to a object list

# Set the CSV name
CSV = 'EGLOINDOORCSV'

# Open the CSV and use escape for later editing date
with open('%s.csv' % CSV) as csvfile:
    # Set the contents to a varible
    reader = csv.reader(csvfile)
    related = {}
    # Loop all the rows in the varible
    for row in reader:
        # Assign the rows to varibles
        ProductName = row[0]
        GroupName = row[4]
        related.setdefault(GroupName, set()).add(ProductName)
        # print(related) # Prints the object
        # Adds the ProductName for each GroupName
        # setdefault - https://www.programiz.com/python-programming/methods/dictionary/setdefault
        # set - Set a object 
        # add - Add a item to the object
        # As it's running a for loop it will loop all items in

        # Long hand
        # if GroupName not in related:
        #    related[GroupName] = set()
        #    related[GroupName].add(ProductName)
        # Make more sence knowing this in a for loop

# Loaded twice for memory leaks

# Pass 2: output the data
with open('%s.csv' % CSV) as csvfile:
    reader = csv.reader(csvfile)
    count = 0 
    for row in reader:
        ProductName = row[0]
        GroupName = row[4]
        # Count each time it loops
        count = count + 1
        # Default string length
        ProductNamelength = 29

        # Statement runs on the fourth count and because it's reset to 0 it keeps looping on the fourth
        if count == 4:
        	print('%s | %s | %s' % (ProductName, GroupName, '///'.join(sorted(related[GroupName]))[0:ProductNamelength])) # Cut by the default string length, all ProductNames are the same size
        	count = 0
        	# print("")
        else:
        	print('%s | %s | %s' % (ProductName, GroupName, '///'.join(sorted(related[GroupName]))[0:ProductNamelength]))
            # join - Join the strings together
            # sorted - Acends the order (A to Z)

            # Prints by the productnames in the related objects by the amount of Productnames
            # for ProductName in related[GroupName]:
            #   print(ProductName,'///')
            #
            # for ProductName in related[GroupName]:
            #	count += 1
            #	print(count)
            #	if count == 4:
            #		count = 0

# As a scriping lang it needs to have a input to close
Exit = input("press close to exit")

# Notes:
# Only works for 5 charaters cause of limit (perfect for the one i was dealing with)
# Help from https://pythonprogramming.net/reading-csv-files-python-3/
# Use tabs and white space correctly
# Statemnets need a colon :

# First Test

#   readCSV = csv.reader(csvfile, delimiter=',')
#   ProductNames.append(ProductName) # appends object to object list (array)
#   GroupNames.append(GroupName) 

#   # print(ProductNames)
#   # print(GroupNames)
#        # print(row[0])
#        # print(row[0],row[1],row[2])
#   print("Done") # Prints done once it has ran though