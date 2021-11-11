import os

os.chdir('/')
def tree_in_tree():
    #{f:os.listdir(f) for f in os.listdir()}
    return { f:os.listdir(f) for f in [dr for dr in os.listdir() if '.' not in dr[1:]] }
        #return os.listdir(f))
print(tree_in_tree())
