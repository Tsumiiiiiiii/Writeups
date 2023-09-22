
## Why pwntools?

Quite often you might have encountered challenges that are interactive, that is, the server asks you some queries, you asnwer those queries and if you manage to answer all of them, you get the flag. 

Those can be found in all categories but mostly in pwn, cryptography and misc.

How to approach problems of those type? There is always the option to calculate each query manually and then send the answer to the server by hand. But what if there are a million queries, or the server shuts itself after like 2 minutes, making it infeasible to do things manually. 
What comes to the rescue is **pwntools**. It is a python module that helps you interact with the server through automation. You can code the interaction, making query answering faster and more efficient. 

## Installing pwntools

It is just a python module guys. You should already know by now how to install a python module. Google how to install the pwntools module in python.

## Example problem

You can find problems of this type in the form of :

```
nc [server-no.] [port-no.]
```

For example : 
```
nc 192.168.3.1 5000
```
If you have a terminal installed, and netcat is installed there, you can just copy paste that line in the terminal and you would be able to communicate with the server. 

For our example problem, the form is like :
```
nc 127.0.0.1 5000 
```
You might have realized that I am using the ip of my localhost, and that is because i am hosting the challenge in my own pc. 

What happens when I copy paste it in my terminal? 

![nc status](https://github.com/Tsumiiiiiiii/Writeups/blob/main/Random-stuffs/pwn-tools-practice/Pasted%20image%2020230921095318.png?raw=true)

See? Now I can communicate with my server.

What does the server tell my to do? It tells me I have to answer 300 queries of the form :
** Give me the sum of 2 numbers**

The server timeout is 2 minutes, and hence, infeasible to be done manually. I need **pwntools**.

## Coding the solution using pwn-tools

The below two lines are default for any pwn-tools problem.

```python
from pwn import *

io = remote('127.0.0.1', 5000)
```

Notice the remote line. The provided ip in **nc** is entered first and then the port. (io is just a variable name, you could have used anything u wanted.)

When we start interacting with the server, we are always greeted with the default two lines:
```
Welcome to Kikis query service!
Answer Kikis questions correctly 300 times and thou shall be rewarded with the flag!
```
They are unnecessary. But when we are coding it out, we have to still take it as input right?
How do we take inputs?

```python
io.recvline()
```

This take one line as input. But I just said I have to take 2 lines as input? What do we do? Simple, write that line twice. 

```python
io.recvline()
io.recvline()
```

After that is done, we have to answer the queries 300 times. Each portion discussed below will be in a loop that will run the number of queries(300 times in this case.)

Now, notice that for each query, the following line is mandatory :

```
Currently at query 1/300.
```

We can take it as input and print it to see out progress(that is, how many queries we have passed so far.)

```python
print(io.recvline())
```

Another mandatory line is:

```
Enter the sum of : number1 number2
```

In this line, the portion before `:` is unnecessary. We only need the portion after. 
So, after taking the line as input, we can split it into 2 parts by `:`. What it does it, it splits the line into an array of length 2. The array has the following elements now:

```
['Enter the sum of : ', 'number1 number2']
```

As we are only concerned with the second part, we take list[1] as python is 0 indexed.

Btw, when you want to use the input given by the server, you have to decode it. Also, the numbers are stored as string and seperated by a space. We need to convert it into 2 integer numbers.

```python
line = io.recvline().decode()
# remember when you take an input from server, you must decode it before you can work with it

needed_part = line.split(': ')[1] 
# becuase we only need the 2 numbers, which are after : in the line

number1, number2 = map(int, needed_part.split(' ')) 
#converts the space seperated numbers to 2 integers
```

Now we have the 2 numbers ready to be summed up. We sum them and send it to the server.

Also remember to convert you answer to a string and encode it.

```python
SUM = number1 + number2
#this answer must be sent to the server

io.sendline(str(SUM).encode())

# the SUM integer must be converted to an int and encoded before being sent
#if this was say a string already, you have just encoded it only
```

We send answers or responses to the server using 

```python
io.sendline()
```


Now depending on our answer, we would be getting a response form the server, whether we are correct or not

```
'Good job. You have passed this round!'
```
Either that or,

```
'You are doomed. No flag for you'
```

That line also has no value for solving this challenge, but would be a nice response to see if we have progressed. So we print that response anyway after we get it from the server:

```python
print(io.recvline()) #it recieves the verdict for our answer and prints it to us
```

Now, when we have done it for 300 times, we are all set to get the flag.

For getting the flag, we can just take the line and print it out

```python
#All queries done, now its time to get the flag
print(io.recvline())
```

![flag getting](https://github.com/Tsumiiiiiiii/Writeups/blob/8320cb2d2ced954f5ec153ea0a37d033a4a83655/Random-stuffs/pwn-tools-practice/Pasted%20image%2020230921102548.png)

Voila, our job is done.

## Full solution script

```python
from pwn import *

io = remote('127.0.0.1', 5000)

io.recvline()
io.recvline()

for _ in range(300):
    print(io.recvline())
    line = io.recvline().decode()
    # remember when you take an input from server, you must decode it before you can work with it
    needed_part = line.split(': ')[1] # becuase we only need the 2 numbers, which are after : in the line
    number1, number2 = map(int, needed_part.split(' ')) #converts the space seperated numbers to 2 integers
    SUM = number1 + number2
    #this answer must be sent to the server
    io.sendline(str(SUM).encode())
    # the SUM integer must be converted to an int and encoded before being sent
    #if this was say a string already, you have just encoded it only
    print(io.recvline()) #it recieves the verdict for our answer and prints it to us

#All queries done, now its time to get the flag
print(io.recvline())
```


## Server script

If you are wondering what was the script for the server that you were communicating with, here you go

```python
#!/usr/local/bin/python

from random import randint

print('For each of the 200 queries, check how many vowels are there in the given string.')

def getRandomString():
    ret = ''
    for i in range(10):
        c = randint(97, 97 + 26)
        ret += chr(c)
    return ret
    
def check(s):
    ret = 0
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            ret += 1
    return ret

for query in range(200):
    print('Currently you are at query no. {}/200'.format(query + 1))
    s = getRandomString()
    print('How many vowels for the string : {}'.format(s))

    x = int(input())
    if x == check(s):
        print('You passed this round!')
    else:
        print('Faillllllll')
        exit(2)

with open('flag.txt', 'r') as f:
    print('Flag is :', f.read())
```
## Bonus

Experiment with the following functions

```python
io.recv()
io.recvuntil()
io.send()
io.sendafter()
io.interactive()
```

Even though I have not used them in the example problem, they can become very handy at times when you are solving difficult problems. So try them out and see what happens. 

Especially, try using the `io.interactive()` function. That has saved me a lot at times.
