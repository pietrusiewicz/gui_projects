class MindMap:
    def __init__(self):
        self.tree = {'temat1':[], 'temat2':[]}
    
    def display_tree(self):
        for i,item in enumerate(self.tree):
            print(item)
    
if __name__ == '__main__':
    m = MindMap()

