#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This function will loop for the amount of times that it takes for n square
   to reach n cubed, which is n times. Thus a time complexity of O(n)


b) This function initially loops n times, then inside it loops until doubling j
   reaches n, which I think is log2(n). Giving time complexity of O(n*log(n))


c) This function will recursively loop one time for each bunny
   giving a time complexity of O(bunnies) or  O(n)
   unless I'm missing something about recursion, in which case log(n) cause
   that's what the other recursive cases were

## Exercise II

1) Go to the middle floor and drop the egg (round down in case of odd numbers)

    IF there are two floors  remaining drop the egg on the first
        IF it breaks, this is floor f
        IF Not then the floor above it is floor f (assuming there is a point the egg will break)

    IF egg breaks you know it would also break on the top half of the floors
         start over using your current floor the top

    IF egg does not break you know it would not break below that floor
        start over with current floor as bottom floor

This function loops as many times as you can half n
again I think this is log2(n) giving a time complexity of O(log(n))
