# Task-3---Collection-Framework

Write an application that takes a string and returns 
the number of unique characters in the string.

It is expected that a string with the same character 
sequence may be passed several times to the method. 

Since the counting operation can be time-consuming,
the method should cache the results, 
so that when the method is given a string previously encountered, 
it will simply retrieve the stored result.

Use collections and map where appropriate. 
Write tests using py.test.

E.g
"abbbccdf" => 3
a, d, f are present once.

your_func_name('abbbccdf') == 3