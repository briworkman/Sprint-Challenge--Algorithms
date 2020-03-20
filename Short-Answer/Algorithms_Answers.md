#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n)

The bigO notation for the loop is O(n) because there are n number of operations.

b)O(n^2)

The bigO notation for the while loop is O(n) and the bigO notation for the for loop is O(n), so combined is O(n^2)

c)O(n)

the bigO notation for the loop is O(n) with n being the number of bunnies

## Exercise II

Find the middle floor
go to the middle floor and drop an egg
if the egg breaks, return true
assume all floors above the middle floor is not safe to drop the eggs
Then, find a new middle in the lower number of floors, and repeat the process
When the egg no longer breaks, you have found a safe floor and can assume any floors below and including it are safe to drop your eggs

runtime complexity = O(log n)
