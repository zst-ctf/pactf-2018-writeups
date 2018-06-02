#!/usr/bin/env python
from pwn import *

context(terminal=['bash'])


def get_main_str():
    main_str = ''
    main_str += chr(0x24)
    main_str += chr(0x5)
    main_str += chr(0x48)
    main_str += chr(0x2a)
    main_str += chr(0x2b)
    main_str += chr(0xe)
    main_str += chr(0x52)
    main_str += chr(0x34)
    main_str += chr(0x2e)
    main_str += chr(0x17)
    main_str += chr(0x5c)
    main_str += chr(0x3d)
    main_str += chr(0x5f)
    return main_str


def main():
    log.info('Starting GDB')
    p = ['gdb', './source.6d9692804a8b.out']
    bananagrams = process(p)

    log.info('Set main() breakpoint')
    bananagrams.recvuntil('(gdb)')
    bananagrams.sendline('break main')

    log.info('Running')
    bananagrams.recvuntil('(gdb)')
    bananagrams.sendline('run')

    log.info('Calling bananagrams0()')
    bananagrams.recvuntil('(gdb)')
    bananagrams.sendline('call bananagrams0()')

    for i in range(99):
        log.info('Returning bananagrams{}()'.format(i))
        result = bananagrams.recvuntil('(gdb)')
        for line in result.strip().splitlines():
            if (not line.startswith('(gdb)')):
                print(line)

        bananagrams.sendline('continue')
        result = bananagrams.recvuntil('(gdb)')
        for line in result.strip().splitlines():
            if (not line.startswith('Continuing.')) and \
               (not line.startswith('(gdb)')) and \
               ('exited normally' not in line):
                print(line)

        log.info(' ')
        log.info('Calling bananagrams{}()'.format(i+1))
        bananagrams.sendline('call bananagrams{}()'.format(i+1))



if __name__ == '__main__':
    main()
