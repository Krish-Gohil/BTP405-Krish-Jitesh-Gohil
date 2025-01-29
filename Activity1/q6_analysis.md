## Include written analysis here 
From the plotted graph from q6_testprogram.py, it is evident that mergesort takes similar amount of execution time even for lists with higher sizes, and among selection sort and bubblesort selection sort has lower execution times than bubblsort

### Differences between the three sorting algorithms
Bubble Sort works by repeatedly going through the list, comparing adjacent items and swapping them if they are in the wrong order. It keeps doing this until no more swaps are needed. This method is simple but can be slow for large lists because it might need to go through the entire list many times.

Selection Sort searches for the smallest element in the unsorted part of the list and moves it to the beginning of the unsorted section. It repeats this process for the remaining unsorted elements until the whole list is sorted. Like Bubble Sort, it's easy to understand but can be slow for big lists.

Merge Sort divides the list into smaller parts, sorts these parts, and then combines them back together. It keeps dividing until it has single-element lists, which are already sorted. Then it merges these small sorted lists into larger sorted lists until the whole list is sorted. This method is faster than Bubble Sort and Selection Sort, especially for large lists.