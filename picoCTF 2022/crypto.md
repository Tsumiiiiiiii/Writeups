# basic-mod1

 Just do as the instructions say. Mod the serial no. of each character(0 for A, 1 for B,...) by 37 and map the result by the relevant characters(A for 0, B for 1,...)

```python 
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" #all the relevant characters
ct = "128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137".split()
ans = ""
for m in ct:
    m = int(m)
    ans += c[m % 37]
print("picoCTF{" + ans + "}")
```
`FLAG: picoCTF{R0UND_N_R0UND_CE58A3A0}`

# basic-mod2

Very similar to the first problem, except that we have to find the modular inverse. In python you can do it like this `pow(n, -1, 41)`
```python
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
ct = "186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137".split()
ans = ""
for m in ct:
    m = pow(int(m), -1, 41)
    ans += c[m - 1]
print("picoCTF{" + ans + "}")
```
`FLAG: picoCTF{1NV3R53LY_H4RD_B7FB947C}`

# credstuff

We copy paste the contents of `usernames.txt` in a code editor and search for the username **cultiris** and find that it is in line no. 378. Now that we know this informaiton, we can say that the 378th line of `passwords.txt` will contain the password for that particular user.  
The password is : `cvpbPGS{P7e1S_54I35_71Z3}`  
It is giving us instant ROT cipher vibe. Trying ROT 13 indeed reveals the flag.  
  
`FLAG : picoCTF{C7r1F_54V35_71M3}`

# morse-code

We can use any online audio morse decoder. I used [this](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) and the decoded text is found to be `WH47 H47H 90D W20U9H7`.  
Replacing the spaces with underscores and wraping it with the flag format gives us the original flag.  
  
`FLAG: picoCTF{WH47_H47H_90D_W20U9H7}`

# rail-fence

Classic rail fence cipher.  
Using an online ddecrypter like [this](https://www.boxentriq.com/code-breaking/rail-fence-cipher) and setting the `Rails` to 4 reveals the secret to be `The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7`.  
  
`FLAG: picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7}`

# substitution0

[This](https://www.guballa.de/substitution-solver) particular website is always my first choice for problems related to substitution cipher.  
  
`FLAG: picoCTF{5UB5717U710N_3V0LU710N_03055505}`

# substituion1

The same approach is followed once again. There is a single catch here though. We get `picoCTF{FR3JU3NCY_4774CK5_4R3_C001_7AA384BC}` but the part `FR3JU3NCY` doesn't make any sense. We changed it to `FR3QU3NCY1 and voila!  
  
`FLAG: picoCTF{FR3JU3NCY_4774CK5_4R3_C001_7AA384BC}`

# substitution2

Same as before, and with no catches.  
  
`FLAG: picoCTF{N6R4M_4N41Y515_15_73D10U5_702F03FC}`

# transposition-trial

This is a very classic problem in cryptography.  
As the hint said, we divide the strings in blocks of 3. It can be intuitively said that the first block `heT` will be `The`. From it we guess that the first character is shifted to the second position, second character to the third position and the last character to the first position.  
```python
s = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B"
ans = ""
cur = []
for i in range(len(s)):
    if i % 3 == 0 and i != 0:
        ans += cur[2] + cur[0] + cur[1]
        cur = []
    cur.append(s[i])
ans += cur[2] + cur[0] + cur[1]
print(ans)
```
`FLAG: picoCTF{7R4N5P051N6_15_3XP3N51V3_AE131DBD}`

# Vigenere

Another very classic cipher.  
We plug the ciphertexy and the key in [this](https://www.dcode.fr/vigenere-cipher) webesite and the flag is found.  
  
`FLAG: picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}`

