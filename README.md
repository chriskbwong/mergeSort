# mergeSort
A simple python merge sort program. The program takes in an array of values, then outputs an array in ascending order. This is done in O(n*log(n)) for time complexity.  

Explaination of mergesort:

givenList = [-10, 2, 0, 9 , 7, 79, 0, 6] # gets continously split in half until it is just single elements 
singleValueList = [-10] # then sorts them 2 by 2 (does this for all other elements as well)
twoValueList = [-10, 2] # combines and sorts with another list
fourValueList = [-10, 0, 2, 9] # continues combining until the entire list is sorted
finalList = [-10, 0, 0, 2, 6, 7, 9, 79]
