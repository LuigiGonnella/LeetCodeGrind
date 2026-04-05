1. Bucket Sort
Time & Space Complexity
Time complexity: 

O(n)
Space complexity: 
O(n)

Intuition
Each number in the array appears a certain number of times, and the maximum possible frequency is the length of the array.
We can use this idea by creating a list where the index represents a frequency, and at each index we store all numbers that appear exactly that many times.

For example:

All numbers that appear 1 time go into group freq[1].
All numbers that appear 2 times go into group freq[2].
And so on.
After we build these groups, we look from the highest possible frequency down to the lowest and collect numbers from these groups until we have k of them.
This way, we directly jump to the most frequent numbers without sorting all the elements by frequency.

Algorithm
Build a frequency map that counts how many times each number appears.
Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
For each number and its frequency in the map, add the number to freq[frequency].
Initialize an empty result list.
Loop from the largest possible frequency down to 1:
For each number in freq[i], add it to the result list.
Once the result contains k numbers, return it.

2. Min-Heap 
Time & Space Complexity
Time complexity: 

O(nlogk)
Space complexity: 
O(n+k)


Intuition
After counting how often each number appears, we want to efficiently keep track of only the k most frequent elements.
A min-heap is perfect for this because it always keeps the smallest element at the top.
By pushing (frequency, value) pairs into the heap and removing the smallest whenever the heap grows beyond size k, we ensure that the heap always contains the top k most frequent elements.
In the end, the heap holds exactly the k values with the highest frequencies.

Algorithm
Build a frequency map that counts how many times each number appears.
Create an empty min-heap.
For each number in the frequency map:
Push (frequency, number) into the heap.
If the heap size becomes greater than k, pop once to remove the smallest frequency.
After processing all numbers, the heap contains the k most frequent elements.
Pop all elements from the heap and collect their numbers into the result list.
Return the result.