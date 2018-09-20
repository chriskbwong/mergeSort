#Author: Chris Wong: www.chriskbwong.com
def mergeSort(givenList):
    if len(givenList)>1:
        mid = len(givenList)//2 #splits givenList in half
        left = givenList[:mid]
        right = givenList[mid:]

        mergeSort(left) #repeats until length of each givenList is 1
        mergeSort(right)

        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                givenList[z]=left[x]
                x = x + 1
            else:
                givenList[z]=right[y]
                y = y + 1
            z = z + 1

        while x < len(left):
            givenList[z]=left[x]
            x = x + 1
            z = z + 1

        while y < len(right):
            givenList[z]=right[y]
            y = y + 1
            z = z + 1
    #merges the givenList

testOneList = [-10, 2, 0, 9 , 7, 79, 0, 6]
mergeSort(testOneList)
print(testOneList)

testTwoList = [-1000, 44, 0, 9 , 9, 7, -1, 77, 99]
mergeSort(testTwoList)
print(testTwoList)
