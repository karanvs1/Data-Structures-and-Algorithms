class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)
    
customTree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

customTree.addChild(cold)
customTree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])

hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)

print(customTree)