import socket

def sendline(sock, data):
    sock.sendall(data + b"\n")

def recvline(sock):
    buf = b""
    while True:
        data = sock.recv(1)
        if not data:
            break
        buf += data
        if data == b"\n":
            break
    return buf

def recvuntil(sock, delim):
    buf = b""
    while True:
        data = sock.recv(1)
        if not data:
            break
        buf += data
        if delim in buf:
            break
    return buf

from Crypto.Util.number import long_to_bytes, bytes_to_long

def conn():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(('34.44.186.163', 31510))
  return sock

io = conn()

def query(io, i):
    recvuntil(io, b': ')
    sendline(io, str(i).encode())
    r = recvline(io).decode().strip()
    if r.startswith('bad'):
        return -1
    else:
        return bytes.fromhex(r)

def batch_query(io, batch):
    to_send = '\n'.join(str(i) for i in batch)
    sendline(io, to_send.encode())
    
    ret = []
    for _ in range(len(batch)):
        r = bytes.fromhex(recvline(io).decode().strip().split(': ')[-1])
        ret.append(r)
    return ret

def get_blocks(s):
    ret = []
    for i in range(0, len(s), 16):
        ret.append(s[i : i + 16])
    return ret

def get_modulus(io, verbose = False):
    lo, hi = 1, 1 << 1024
    n = -1
    cnt = 1
    while lo <= hi:
        if verbose and cnt % 100 == 0:
            print(f'query no {cnt}')
        cnt += 1
        mid = (lo + hi) // 2
        if query(io, mid) == -1:
            n = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    for n in range(n - 2, n + 1):
        if query(io, n) == -1:
            return n
    return -1
            

print(recvline(io))

ct = int(recvline(io).decode().strip())
n = get_modulus(io, verbose = True)
print(f'the modulus is {n}')
e = 12389231641983877009741841713701317189420787527171545487350619433744301520682298136425919859970313849150196317044388637723151690904279767516595936892361663


sz = 34

sofar = b''

for i in range(63, 0, -1):
    to_send = ct * pow(256, i * e, n)
    to_send %= n
    blocks = get_blocks(query(io, to_send))
    batch = []
    for c in range(32, 128):
        if len(sofar) > 15:
            take = sofar[:15]
        else:
            take = sofar
        ts = bytes([c]) + take
        while len(ts) != 16: ts += b'\x00'
        batch.append(pow(bytes_to_long(ts), e, n))

    r = batch_query(io, batch)
    found = None
    for c, v in zip(range(32, 128), r):
        if blocks[0] == get_blocks(v)[0]:
            found = c
            break
            
    if not found:
        print('everything all g?')
        break
    sofar = bytes([found]) + sofar
    print(sofar)
    if b'{' in sofar:
        break
