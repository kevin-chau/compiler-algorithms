from treelib import Node, Tree
stack = []
root = Tree()

# Test input
input = "a+b*c"

# consumes next input "word"
def NextWord():
    global input
    word = input[0]
    input = input[1:]
    return word

# Start symbol
S = input[0]

root.create_node(S)
focus = root.root
stack.append(None)
word = NextWord()

while (True):
    if (focus is )
