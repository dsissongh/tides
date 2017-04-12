

from func1 import showmenu
from func1 import generatedatadictionary
from func1 import gethistory

#variables
history = "history.txt"

menu, orderedlist = showmenu()

print(menu)
print(orderedlist)
print(gethistory(history, orderedlist))