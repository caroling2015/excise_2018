#!/usr/bin/env python
from time import ctime,sleep
import thread

def loop0():
    print 'start loop 0 at:',ctime()
    sleep(2)
    print 'end loop 0 at:',ctime()

def loop1():
    print 'start loop 1 at:',ctime()
    sleep(3)
    print 'end loop 1 at:',ctime()

def main():
    print 'starting at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all Done at:',ctime()

if __name__ == '__main__':
    main()