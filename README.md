# RandomDataGenerator
Generates random user data in a csv or json file.  
Run ```dataGenDiekhoff.py <file type> <number of users to generate>```  
from the command line, where `<file type>` is either 'csv' or 'json'

# Mac or Linux users
remove `, newline= ''` from line 35 in dataGenDiekhoff.py.  
This prevents Windows from inserting a blank line between entries.

# For some related programs, see my other repo ![here]https://github.com/BenDiekhoff/5303-DB-Diekhoff/tree/master/A09

# Data
- user_id
- email
- username
- first_name
- last_name
- password
- create_time
- last_update

# Originally forked from
https://github.com/williexu/random_username

# Uses lists from:
- https://github.com/williexu/random_username
- https://github.com/dominictarr/random-name
- https://github.com/arineng/arincli/tree/master/lib
- https://gist.github.com/tbrianjones/5992856/
