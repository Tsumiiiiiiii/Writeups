from pwn import *
from tqdm import tqdm

io = remote('challs.actf.co', 32100)

def query(io, to_send):
    io.recvuntil(b':')
    io.sendline(b'1')
    io.recvuntil(b'>')
    io.sendline(to_send)
    m = int(io.recvline().strip())
    return m


so_far = set()
for _ in tqdm(range(100)):
    try:
        r = query(io, '0'.encode())
        so_far.add(r)
    except:
        io = remote('challs.actf.co', 32100)

print(so_far)
