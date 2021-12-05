import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typer Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "arijanet muric"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start_screen(stdscr)
    
    wpm_test(stdscr)

wrapper(main)
