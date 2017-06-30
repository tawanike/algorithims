# Pre-requisites
# - Knowledge of lists


# List to be sorted.
items = [4, 202, 3, 9, 6, 5, 1, 43, 506, 2, 0, 8, 7, 100, 25, 4, 5, 97, 1000, 27]

def bubble_sort(items):
    # First step is to create a FOR loop that will go through the list
    for i in range(len(items)-1):
        # Everytime we get to a number in the list while running the FOR loop in 
        # line 6 we should also go through the whole list again in the FOR loop in
        # line 10 below. This ensures that we go through the list for as many times as
        # there are elements in that list. So is there are 20 elements in the list, 
        # the FOR loop below will run 20 times comparing each element to the next one 
        # 20 times.
        for l in range(len(items)-1):
            # Here is where the actual comparison takes place. l here denotes the index of 
            # an element in a list and this is zero based, starts at 0 and not 1. Using the list (items)
            # the number 4, or list element with a value of 4 is on indeces 0, for the first one and 
            # 15 for the second one.
            if items[l] > items[l+1]:
                # This IF statement compares the value of the element on index l, against the value of
                # the element on index l + 1. For example if l is equal to 0, then the IF statement will compare the
                # element on index 0, items[0] to the element on index items[0+1]/items[1].
                # If the element on index 0 is bigger than the element on index 1 we will store that element
                # in the variable temp for use later.
                temp = items[l]
                # After storing the element in temp we want to take the original list and swap the 
                # positions of these elements such that the element with smaller value comes first. 
                # To do this we replace the element at index 0 with the element at index 1.
                items[l] = items[l+1]
                # To complete the swap we will then also need to take the element that was originally
                # at index 0 now stored in the temp variable and replace the element on index 1.
                items[l+1] = temp
                # This comparison and replacing takes places for all numbers 

    return items

results = bubble_sort(items)
print(results)

