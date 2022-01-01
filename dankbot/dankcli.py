import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(15, 45, 'Welcome To Dank Bot')
    stdscr.addstr(15, 45, 'Press Any Key To Continue!!!!')
    stdscr.getch()

wrapper(main)
