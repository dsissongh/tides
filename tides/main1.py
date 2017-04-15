

from func1 import showmenu
from func1 import generatedatadictionary
from func1 import gethistory
from func1 import sethistory
from func1 import getchoice

#variables
history = "history.txt"

menu, orderedlist = showmenu()
choice = getchoice(orderedlist)

print(menu)
print(orderedlist)
print(choice)


exit()

choice = gethistory(history, orderedlist)
sethistory(history, choice)
print(choice)