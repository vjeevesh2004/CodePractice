''' Write a Python program to sort a list
of elements using the insertion sort 
algorithm. Note : According to Wikipedia 
"Insertion sort is a simple sorting 
algorithm that builds the final sorted 
array (or list) one item at a time. 
It is much less efficient on large lists 
than more advanced algorithms such as 
quicksort, heapsort, or merge sort."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]
'''

def sorrt(element):
    n=len(element)

    for i in range(1,n):
        anchor = element[i]
        j = i -1
        while j>=0 and anchor<element[j]:
            element[j+1] = element[j]
            j = j - 1
        element[j + 1] = anchor
        
if __name__ == "__main__":
    element = [14,46,43,27,57,41,45,21,70]
    sorrt(element)
    print(element)
