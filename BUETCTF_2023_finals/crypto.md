## Crypto 1
We are given a file called `galf.db`. I opened it using Notepad and found a huge chunk of random characters. It was giving me a `base 64` vibe. So I scrolled to the end
of the file, and indeed there were some `=` at the end, confirming my suspicion. 

I opened up [cyberchef](https://gchq.github.io/CyberChef/) and selected base64 decoding. I got another base64 string. Decoding it gave a base64 string, again.

At this point, I gave up and wrote a python script to do the repetitive decryption for me, stopping only when I get a probable flag (a string that has `BCF` in it).
```python
from base64 import b64decode

with open('galf.db', 'r') as f:
    ct = f.read().encode()

while b'BCF' not in ct:
    ct = b64decode(ct)

print(ct.decode())
```
> Flag: **BCF2023{k33p_d3b451n6_t1ll_3t3rn1ty_0xabba}**

## Crypto 2
Upon opening the given `foo.bar` file via Notepad, we get the following:
```
foo bar foo foo foo foo bar foo foobar foo bar foo foo foo foo bar bar foobar foo bar foo foo foo bar bar foo foobar foo foo bar bar foo foo bar foo foobar foo
foo bar bar foo foo foo foo foobar foo foo bar bar foo foo bar foo foobar foo foo bar bar foo foo bar bar foobar foo bar bar bar bar foo bar bar foobar foo bar
bar foo bar foo foo foo foobar foo foo bar bar foo bar foo foo foobar foo bar bar bar foo bar bar foo foobar foo foo bar bar foo foo bar bar foobar foo bar foo
bar bar bar bar bar foobar foo bar bar bar bar foo foo bar foobar foo foo bar bar foo foo foo foo foobar foo bar bar bar foo bar foo bar foobar foo bar foo bar
bar bar bar bar foobar foo bar bar foo bar foo foo foo foobar foo foo bar bar foo bar foo foo foobar foo bar bar foo foo bar foo foo foobar foo bar foo bar bar
bar bar bar foobar foo bar bar foo foo bar foo bar foobar foo bar bar foo bar bar bar foo foobar foo foo bar bar foo foo foo foo foobar foo bar bar bar foo bar
foo bar foobar foo bar bar foo foo bar bar bar foobar foo bar bar foo bar foo foo foo foobar foo bar foo bar bar bar bar bar foobar foo bar bar foo foo bar bar
foo foobar foo bar foo bar foo bar foo bar foobar foo bar bar foo bar bar bar foo foobar foo bar foo bar bar bar bar bar foobar foo foo bar bar foo foo foo foo
foobar foo bar bar bar bar foo foo foo foobar foo foo bar bar foo foo bar bar foobar foo foo bar bar foo bar foo foo foobar foo foo bar bar foo foo bar foo foobar
foo bar bar foo foo foo foo bar foobar foo bar bar bar bar bar foo bar foobar foo foo foo foo bar foo bar foo 
```
Problems like this are quite common in Bangladeshi CTFs. The `foo` represents `1` and `bar` represents `0` or vice versa. `foobar` works as a separator.

The final step is to just do binary decoding.
```python
with open('foo.bar', 'r') as f:
    s = f.read()

s = s.replace('foobar', '')
s = s.replace('foo', '0')
s = s.replace('bar', '1')
s = s.replace(' ', '')

flag = ''
for i in range(0, len(s), 8):
    c = s[i : i + 8]
    c = int(c, 2)
    flag += chr(c)

print(flag)
```
> Flag: **BCF2023{h4v3_y0u_h4d_en0ugh_fUn_0x342a}**
