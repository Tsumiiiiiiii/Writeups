These are the writeups for the crypto challenges from team Exodus

To see my scripts and the rough experiments I did for this, refer to the sagemath notebook attached here https://github.com/Tsumiiiiiiii/Writeups/blob/main/smp24/Untitled4.ipynb. Please scroll to the bottom from cell $166$, that is where the relevant portion starts from.

By the way, in sagemath we do $\oplus$(XOR) with `^^` instead of `^` in python. 

## Challenge 1

$$
\text{flag}\\_{i} = \frac{\text{to\\_int}(c_i)}{69 + 67}
$$

## Challenge 2

Extremely silly and guessy challenge. Very disappointing. Had to experiment with a shit load of stuffs, before suddenly getting the flag, which turned out to be an even bigger disappointment. 

If we xor the 2 given keys and convert them to integers, we get a number(lets say it's $X$) that is somewhat close to the splitted parts $P1, P2_{0}, P_3$. Only the middle portion is a bit different, We actually get the proper $P2$ if we do $P2_{0} \oplus P_4$. But this observation turns out to be valueless. I tried things like scrabmbling the given parts, checking if they are prime(given $Y$ being another prime??), using them as RSA keys to see if it gives the correct decryption(this was the these of a crypto problem in KnightCTF 24, by the same organizers). 

Anyways, what did give me the flag was simply doing $X \oplus H$. WHAT THE ABSOLUTE FUCK.

## Challenge 3

This was (supposed) to be a harder challenge. So i did the RSA things here as well, only to be disappointed again. But trying the exact same strategy as before gave me the flag. 
