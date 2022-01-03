import curses
from curses import wrapper
from dankbot import DankBot
import time
from threading import Thread

# Pending Use Sync along with Threads and custom fucntions to achieve pseudo inter process communication

def init_selenium_process(survive=10):
    p = DankBot()
    p.exec_base_script()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)
    p = 0
    i = 0
    while(p != 78 and p != 110):
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(15, 0, f"Please Make Sure That You Are Using Full Screen Before Moving to the next step (Press N)(Iteration {i+1}, p = {p})", curses.color_pair(2))
        i += 1
        p = stdscr.getch()      
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(15, ((curses.COLS - 1) // 2) + 19, "       /||\                     /||\\", curses.color_pair(1))
    stdscr.addstr(16, ((curses.COLS - 1) // 2) + 19, "    ///    \\\\\\               ///    \\\\\\", curses.color_pair(1))
    stdscr.addstr(17, ((curses.COLS - 1) // 2) + 19, " ///          \\\\\\         ///          \\\\\\", curses.color_pair(1))
    stdscr.addstr(18, ((curses.COLS - 1) // 2) + 19, " \\\\\\          ///         \\\\\\          ///", curses.color_pair(1))
    stdscr.addstr(19, ((curses.COLS - 1) // 2) + 19, "    \\\\\\    ///               \\\\\\    ///", curses.color_pair(1))
    stdscr.addstr(20, ((curses.COLS - 1) // 2) + 19, "       \||/                     \||/", curses.color_pair(1))
    stdscr.addstr(25, (230 // 2) - len("Welcome To DankBot v0.1") - 4, "Welcome To DankBot v0.1", curses.color_pair(3))
    stdscr.addstr(26, (230 // 2) - len("Press Any Key To Continue") - 3, "Press Any Key To Continue", curses.color_pair(4))
    stdscr.getch()
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "IMPORTANT INSTRUCTIONS", curses.color_pair(5))
    stdscr.addstr(1, 10, "1. As soon as the program starts a chrome window will open up with the discord login page.", curses.color_pair(2))
    stdscr.addstr(2, 10, "2. Login by QR or Login using password and email. We do not retain the data in any manner.", curses.color_pair(2))
    stdscr.addstr(3, 10, "3. Select the channel where you want the bot to do its work.", curses.color_pair(2))
    stdscr.addstr(4, 10, "4. Make sure there isn't any spam bot detector and you have the permissions.", curses.color_pair(2))
    stdscr.addstr(5, 10, "5. After all the above steps are done type in \"startprogram\" in console to start the bot", curses.color_pair(2))
    stdscr.addstr(6, 10, "6. To Stop The bot close the browser then the console or just type in \"killbot\"", curses.color_pair(2))
    stdscr.getch()  


wrapper(main)
