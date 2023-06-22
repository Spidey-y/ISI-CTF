from pwn import * 


r = remote("challenges.isictf.live",1300)
r.recvline()
r.recvline()
r.recvline()
r.recvuntil('> ')
r.send(b"2\n")
r.recvuntil(': ')
r.send("adel"+chr(12)*12+'\n')
token = r.recvline().decode().split(": ")[-1][:32]
r.recvline()
r.recvline()
r.recvuntil('> ')
r.send(b"1\n")
r.recvuntil(': ')
r.send(token+'\n')
r.interactive()


