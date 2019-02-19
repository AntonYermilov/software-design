# Architecture notes 
*by Liza Vasilenko*

The CLI environment was already so convenient that it contained `PWD` and `HOME` variables, 
which made porting new commands to existing architecture very easy. But in order to access 
these variables I had to change Anton's original plan and add a dependency on Environment 
from Command classes:

## Class diagram

<pre>
           ––––––          ––––––––––
           |     | –––––––> | Parser |
           |     |          ––––––––––
stdin –––> |     |              |
           | CLI |              | Variables
stdout <–– |     |              v           <b>Variables</b>
           |     |          –––––––––––––––          –––––––––––
           |     | –––––––> | Environment | <b><=======></b> | Command |
           –––––––          –––––––––––––––          –––––––––––
</pre>

Now I'm not fully satisfied with storing Environment as an attribute of global variable `CLI`. 
On one hand, it allows accessing all the values easily from any part of the program, but 
on the other hand, you have to carefully watch yourself modifying something used by other components.
This is clearly seen when testing: you can't mock the global `CLI` and so you can't run tests 
for a command independently, ex. if it reads from and writes to `PWD` as `cd` does.

I spent a lot of time thinking up something to complain about, since in the rest I fully agree 
with the architecture and responsibilities of the components. Extracting Environment and Parser 
into a separate entities makes the solution much more readable and extensible: I only had to inherit
another two classes from `Command` class and then add two items to `_commands` dict to make CLI run
with brand new utilities.

