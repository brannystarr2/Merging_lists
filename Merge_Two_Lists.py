"""_summary_
Merging lists refers to the process of combining two or more lists into a single list, 
with the resulting list containing all the elements from the original lists. In the context of programming
merging lists is often used when dealing with sorted data, such as when sorting and merging data from multiple sources.
    """
    
def merge_sorted_lists(list1, list2):#defining a function that takes two arguments
    """
    Merges two already sorted lists into a single sorted list.
    """
    # initialize empty result list
    result = []

    # initialize indices for each list
    i = 0
    j = 0

    # iterate over both lists simultaneously until one is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # add any remaining elements from the non-exhausted list
    #result += list1[i:]
    #result += list2[j:]

    return result

listx = [1,2 , 3, 5, 7, 8]
listy = [2, 4, 6, 8]

merged_list = merge_sorted_lists(listx, listy)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


