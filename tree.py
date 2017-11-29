#!/usr/bin/python3

import sys
import curses
import random


def printTree():

    tree = '*'
    space = ' '
    bulb = 'O'

    for i in range( 0, width ):
        for j in range( 0, width - i ):
            stdscr.addch( space )
        for k in range( 0, i * 2 - 1 ):
            if random.randrange( 10 ) == 0:
                stdscr.addstr( tree, curses.color_pair( random.randrange( 5 ) ) )
            else:
                stdscr.addstr( tree, curses.color_pair( 1 ) )

        stdscr.addch( '\n' )
        stdscr.refresh()

    for j in range( 0, 3 ):
        for k in range( 0, width - 2 ):
            stdscr.addch( space )
        for j in range( 0, 3 ):
            stdscr.addch( trunk )

        stdscr.addch( '\n' )
        stdscr.refresh()

def printFullTree():

    a = 0
    star = [ '|', '/', '-', '\\' ]
    while True:
        try:
            for i in range( 0, width - 1 ):
                stdscr.addch( ' ' )

            stdscr.addstr( star[ a ], curses.color_pair( 3 ) )
            printTree()
            curses.napms( 250 )
            stdscr.clear()

            if a == 3:
                a = 0
            else:
                a = a + 1
        except KeyboardInterrupt:
            curses.endwin()
            return 0

width = int( sys.argv[ 1 ] )

stdscr = curses.initscr()

curses.start_color()
curses.init_pair( 1, curses.COLOR_GREEN, curses.COLOR_BLACK )
curses.init_pair( 2, curses.COLOR_RED, curses.COLOR_BLACK )
curses.init_pair( 3, curses.COLOR_YELLOW, curses.COLOR_BLACK )
curses.init_pair( 4, curses.COLOR_BLUE, curses.COLOR_BLACK )

printFullTree()
exit()
