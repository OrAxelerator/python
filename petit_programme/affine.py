import curses
from curses import wrapper
import os
from time import sleep

size = os.get_terminal_size()
w = size.columns
h = size.lines

a, b = int(input("a: ")), int(input("b : "))

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear() # clear screen
    for x in range(w):
        
        y = (-1*a)*x + -1*b
        if 0 <= y < h:
            sleep(0.1) 
            stdscr.addstr(y,x," ",curses.color_pair(1))
            stdscr.refresh()
        else:
            pass
        
    stdscr.getch() # wait user input something to "pass" and end program
    

wrapper(main)
