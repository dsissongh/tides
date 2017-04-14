

from func1 import showmenu
from func1 import generatedatadictionary
from func1 import gethistory
from func1 import sethistory

#variables
history = "history.txt"

menu, orderedlist = showmenu()

print(menu)
#print(orderedlist)
choice = gethistory(history, orderedlist)
sethistory(history, choice)
print(choice)