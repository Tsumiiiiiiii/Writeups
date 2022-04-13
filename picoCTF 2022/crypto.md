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

# diffie-hellman

Basic understanding of how key exchange works in [diffie-hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) is sufficient for this problem.  
From the given information, we can easily generate the shared secret `sh` which will be the shift value for our ROT cipher. One catch here is that we do not know whether the shifting will be done backwards or forwards. So we try both of them and the one that creates a meaningful text is our flag.
```python
p = 13
g = 5
a, b = 7, 3
A = pow(g, a, p)
sh = pow(A, b, p) # this is the shared secret

s = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_DI9D987F"

f = ""
b = ""

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

n = len(alpha)
for c in s:
    if c in alpha:
        x = alpha.index(c)
        x += sh
        x %= n
        f += alpha[x]
    else:
        f += c

for c in s:
    if c in alpha:
        x = alpha.index(c)
        x -= sh
        if x < 0:
            x += n
        b += alpha[x]
    else:
        b += c

print("picoCTF{" + f + "}")
print("picoCTF{" + b + "}")
```
`FLAG: picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_8D48432A}`

# Very Smooth

From the hint and the title we understand this problem is about [pollard p-1 factorization](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm).  
The algorithm itself is not that difficult to code, or, you can use an already implemented code. After you factr the modulus, everything is trivial from there.
```python
import  math
from Crypto.Util.number import long_to_bytes

def  pollard (n): 
    a = 2 
    b = 2 
    while True : 
        a = pow(a, b , n) 
        d = math.gcd(a - 1, n) 
        if 1 < d < n : return  d 
        b  +=  1


n = 0xc5261293c8f9c420bc5291ac0c14e103944b6621bb2595089f1641d85c4dae589f101e0962fe2b25fcf4186fb259cbd88154b75f327d990a76351a03ac0185af4e1a127b708348db59cd4625b40d4e161d17b8ead6944148e9582985bbc6a7eaf9916cb138706ce293232378ebd8f95c3f4db6c8a77a597974848d695d774efae5bd3b32c64c72bcf19d3b181c2046e194212696ec41f0671314f506c27a2ecfd48313e371b0ae731026d6951f6e39dc6592ebd1e60b845253f8cd6b0497f0139e8a16d9e5c446e4a33811f3e8a918c6cd917ca83408b323ce299d1ea9f7e7e1408e724679725688c92ca96b84b0c94ce717a54c470d035764bc0b92f404f1f5
c = 0x1f511af6dd19a480eb16415a54c122d7485de4d933e0aeee6e9b5598a8e338c2b29583aee80c241116bc949980e1310649216c4afa97c212fb3eba87d2b3a428c4cc145136eff7b902c508cb871dcd326332d75b6176a5a551840ba3c76cf4ad6e3fdbba0d031159ef60b59a1c6f4d87d90623e5fe140b9f56a2ebc4c87ee7b708f188742732ff2c09b175f4703960f2c29abccf428b3326d0bd3d737343e699a788398e1a623a8bd13828ef5483c82e19f31dca2a7effe5b1f8dc8a81a5ce873a082016b1f510f712ae2fa58ecdd49ab3a489c8a86e2bb088a85262d791af313b0383a56f14ddbb85cb89fb31f863923377771d3e73788560c9ced7b188ba97
e = 0x10001

p = pollard(n)
q = n // p
assert(p * q == n)
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
```
`FLAG: picoCTF{7c8625a1}`
