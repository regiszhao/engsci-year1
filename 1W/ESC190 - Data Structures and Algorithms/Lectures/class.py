#%%
class Node:
    def __init__(self, name):
        self.name = name
    
    def introduce(self, introducee):
        print("Hello", introducee+", my name is", self.name)


node = Node("praxis")
node.introduce("EngSci 1T5")
# %%
