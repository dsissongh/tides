
def resetcolor(term):
	#term.reset does not appear to be resetting the color correctly
	#set the terminal back to lt grey on black
	term.cprint(7,0,'')