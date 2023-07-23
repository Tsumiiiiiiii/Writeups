## The challenge

This was an OSINT challenge. The challenge description said something like `An attacker made some mistake in the victim's server`. We are tasked to find the date of birth of that attacker.
At first, it made no sense and everything seemed out of context. At around the last 2 hours, a hint was added, saying it was connected to some IR problem that we had to solve before. 

## The solution

Upon going through the IR logs again, we could understand that the attacker was the same person who created the ransomware to encrypt all the files. Luckily, we are given
the encryption script. If we take a closer look at that script, we can see this part:
```
header = '''

  __  __         ____                          _____                             _             
 |  \/  |_   _  / ___| _   _ _ __   ___ _ __  | ____|_ __   ___ _ __ _   _ _ __ | |_ ___  _ __ 
 | |\/| | | | | \___ \| | | | '_ \ / _ \ '__| |  _| | '_ \ / __| '__| | | | '_ \| __/ _ \| '__|
 | |  | | |_| |  ___) | |_| | |_) |  __/ |    | |___| | | | (__| |  | |_| | |_) | || (_) | |   
 |_|  |_|\__, | |____/ \__,_| .__/ \___|_|    |_____|_| |_|\___|_|   \__, | .__/ \__\___/|_|   
         |___/              |_|                                      |___/|_|                  
@nan0shade
'''
```
At the bottom, we can see a string called `@nan0shade`. This felt like a social media handle. We tried using Twitter first, and voila, a [post](https://twitter.com/nan0shade/status/1681361829652746240?s=20) containing an image with his age
in a birthday cake. We can get his birth date from the date the post was done, and his birth year by subtracting 26 from 2023.

