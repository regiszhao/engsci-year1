Hello!

Copy in your autocomplete.c into this folder and try compiling / running the tester.c file.

"gcc tester.c autocomplete.c" followed with "./a.exe" (./a.out for linux & mac) worked for me

After much complaints from the mac peasants, I tried it for myself and what worked was the following:

1. go to terminal and type gcc, it should prompt you to install dev tools (which you do). If it doesn't
prompt you to install dev tools just go to step 2.

2. Navigate to the project1_tester folder in terminal 

3. type "gcc tester.c autocomplete.c" in terminal

4. type "./a.out" and the tester should start running

---------------------------------------------------------------------------------------------

-I highly recommend using MS Visual Studio (not vs code) for c / c++ as it's dead stable and it has
a really nice debugger. Many people with vs code are having trouble properly debugging.

-While decimal places will not be tested, I have them inside the sample case as it's a good idea to
use atof apparently (according to piazza)

-Use at your own risk... I do not guarantee you get 100% on this project if you pass all the cases
If you do though feel free to get me bbt once this pandemic is over ;) (this is a joke)

-Program by default goes through all the test cases

-There's also a function available to test specific test cases with more debugging information

-dm me on discord (mrmandarin#3434) or ask on the programming channel if you have questions

Good luck debugging

---------------------------------------------------------------------------------------------

There is nothing network based this time because C has the shittiest network protocol known to
mankind's existance. Essentially I output what my functions return onto text files and I compare
against what yours get through those.

Also for you little shits who complain that there's only 10000 test cases, unless you want me
to somehow find a way to host 500 gigs worth of fuck_praxis.txt files that's not happening.
I did include the code used to generate the sample_cases though so feel free to use that 
if you have no life.

