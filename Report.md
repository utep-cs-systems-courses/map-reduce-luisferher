#Parallel Lab 2

The problems that I encounter first was how I would traverse or iterate through the files that had thousands of lines.
I resolved this issue by creating a loop to store all the contents from the multiple files into a single object and the a list that splited items by spaces.
Another problem that I had was that there were some words with a '\n','.' or ',' making the comparison unsuccessful eventhough the word was the same.
I overcome this issue by using replace() to delete those characters.
Some of the problems that I could not resolve why I was not getting the desired number of words that I should get from the handout. 
I got like 2/3 from the supposed total.
This assignment took me 8 hours in total to complete.

Performance measures:
Number of threads: 1
{'Number of hate words in Shakespeare is: ': 178}
{'Number of love words in Shakespeare is: ': 2149}
{'Number of death words in Shakespeare is: ': 858}
{'Number of night words in Shakespeare is: ': 686}
{'Number of sleep words in Shakespeare is: ': 250}
{'Number of time words in Shakespeare is: ': 1095}
{'Number of henry words in Shakespeare is: ': 595}
{'Number of hamlet words in Shakespeare is: ': 442}
{'Number of you words in Shakespeare is: ': 14006}
{'Number of my words in Shakespeare is: ': 13148}
{'Number of blood words in Shakespeare is: ': 655}
{'Number of poison words in Shakespeare is: ': 81}
{'Number of macbeth words in Shakespeare is: ': 272}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of heart words in Shakespeare is: ': 997}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of honest words in Shakespeare is: ': 296}
Elapsed Time: 54.28800607300218 Seconds
Number of threads: 2
{'Number of hate words in Shakespeare is: ': 178}
{'Number of love words in Shakespeare is: ': 2149}
{'Number of death words in Shakespeare is: ': 858}
{'Number of night words in Shakespeare is: ': 686}
{'Number of sleep words in Shakespeare is: ': 250}
{'Number of time words in Shakespeare is: ': 1095}
{'Number of henry words in Shakespeare is: ': 595}
{'Number of hamlet words in Shakespeare is: ': 442}
{'Number of you words in Shakespeare is: ': 14006}
{'Number of my words in Shakespeare is: ': 13148}
{'Number of blood words in Shakespeare is: ': 655}
{'Number of poison words in Shakespeare is: ': 81}
{'Number of macbeth words in Shakespeare is: ': 272}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of heart words in Shakespeare is: ': 997}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of honest words in Shakespeare is: ': 296}
Elapsed Time: 3767.877483684999 Seconds
Number of threads: 4
{'Number of hate words in Shakespeare is: ': 178}
{'Number of love words in Shakespeare is: ': 2149}
{'Number of death words in Shakespeare is: ': 858}
{'Number of night words in Shakespeare is: ': 686}
{'Number of sleep words in Shakespeare is: ': 250}
{'Number of time words in Shakespeare is: ': 1095}
{'Number of henry words in Shakespeare is: ': 595}
{'Number of hamlet words in Shakespeare is: ': 442}
{'Number of you words in Shakespeare is: ': 14006}
{'Number of my words in Shakespeare is: ': 13148}
{'Number of blood words in Shakespeare is: ': 655}
{'Number of poison words in Shakespeare is: ': 81}
{'Number of macbeth words in Shakespeare is: ': 272}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of heart words in Shakespeare is: ': 997}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of honest words in Shakespeare is: ': 296}
Elapsed Time: 4871.282644305 Seconds
Number of threads: 8
{'Number of hate words in Shakespeare is: ': 178}
{'Number of love words in Shakespeare is: ': 2149}
{'Number of death words in Shakespeare is: ': 858}
{'Number of night words in Shakespeare is: ': 686}
{'Number of sleep words in Shakespeare is: ': 250}
{'Number of time words in Shakespeare is: ': 1095}
{'Number of henry words in Shakespeare is: ': 595}
{'Number of hamlet words in Shakespeare is: ': 442}
{'Number of you words in Shakespeare is: ': 14006}
{'Number of my words in Shakespeare is: ': 13148}
{'Number of blood words in Shakespeare is: ': 655}
{'Number of poison words in Shakespeare is: ': 81}
{'Number of macbeth words in Shakespeare is: ': 272}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of heart words in Shakespeare is: ': 997}
{'Number of king words in Shakespeare is: ': 2815}
{'Number of honest words in Shakespeare is: ': 296}
Elapsed Time: 6523.610421926 Seconds

I can notice that while incrementing the number of threads the Elapsed time increases dramatically, because it my program, as using parallel programming, 
it gets slower as more threads are used, more complex communication between them takes place.
While doing this assignment I learn how to use the dictionary and shared list and how the locks are useful to keep the variables data syncronized when using
multiple threads. 


model name      : Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz
      4      36     220
