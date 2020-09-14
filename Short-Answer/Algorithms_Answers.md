#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear Time / O(n) - The running time increases linearly with the size of input data. It scales linearly with n.

```
  a = 0                  O(1)
  while (a < n * n * n): O(n^3)
    a = a + n * n        O(n^2)
```
| n  |   n^3  |    n^2  | number of operations |
|----|--------|---------|----------------------|
| 6  |   216  |   36    |  6                   |
| 7  |   343  |   49    |  7                   |


b) O(n Log n) - There are 2 loops, one is nested inside the other one. The nested loop is dependent on "n" and increases exponentially so the time to reach "n" is halved. So instead of O(n^2) the complexity is O(n Log n).



c) Linear Time / O(n) - This time also increases linearly with the size of the input. If the input is 1, it will take less time to reach the base case of 0 and if the input is 500, it will take much longer since we are adding 2 and then substracting one with each recursive loop.


## Exercise II

Going to implement Binary Search for this problem because it's clear that eggs are not breaking at the floors that are lower than f.
This way we only search the floors higher than f and we literally avoid half of the floors each time.

     define a function which takes as parameters n floors
            initialize a variable to hold the starting point for our search
            (this will be set to the first floor)
            initialize a variable to hold the ending point for our search
            (this will be set to the top floor)
        
         create a loop which will continue as long as our starting and ending points have not crossed over each other
                define a midpoint between the current starting and ending values
                if at the current floor eggs break, but at the floor below, they do not, we have found f and can return this floor number
                if at the current floor eggs are not breaking, set the new start to be the former midpoint (plus one so we don't search the actual midpoint again) and the end stays the same. Continue searching.
                if at the current floor eggs break, but at the floor below, they also break, we need to keep searching, but floor 'f' is below. Set the end to be the former midpoint -1 and continue searching.

## Runtime is O(log n) for binary search, since we will never be searching through the whole array at any time. It will halve each iteration.




