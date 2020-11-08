class TreeNode:
    def __init__(self, value=0, color=0):
        # Children of the tree node
        self.leftChild = None
        self.rightChild = None
        # parent of the node
        self.parentNode = None
        # value of the node
        self.value = value
        # color of the node
        self.color = color

    def setLeftChild(self, child):
        # adds child as the left child of the node and sets node as the parent of the child
        self.leftChild = child
        child.parentNode = self

    def setRightChild(self, child):
        # adds child as the right child of the node and sets node as the parent of the child
        self.rightChild = child
        child.parentNode = self

    def getChildren(self):
        # returns all children of the node
        return [self.leftChild, self.rightChild]

    def getAllValues(self):
        """
        gets and returns all values from node and all it's (grand)children
        :param lista: list of all the children and grandchildren
        :return: list lista
        """
        # list that will be filled with values
        listOfValues = []
        # check if node has left child
        if self.hasLeftChild():
            listOfValues += (self.getLeftChild().getAllValues())
        if self.hasRightChild():
            listOfValues +=(self.getRightChild().getAllValues())
        listOfValues.append(self.value)
        return listOfValues

    def getLeftChild(self):
        # returns left children of the node
        return self.leftChild

    def getRightChild(self):
        # returns right children of the node
        return self.rightChild

    def popLeftChild(self):
        # removes and returns left child, if it exists
        if self.leftChild:
            left = self.leftChild
            left.parent = None
            self.leftChild = None
            return left

    def popRightChild(self):
        # removes and returns right child, if it exists
        if self.rightChild:
            right = self.rightChild
            right.parent = None
            self.rightChild = None
            return right

    def setParent(self, parent):
        # sets parent as the parent of the node
        self.parentNode = parent

    def getParent(self):
        # returns parent of the node
        if self.parentNode:
            return self.parentNode
        else:
            print("this is root")

    def setColor(self, color):
        # sets color of the node
        self.color = color

    def getColor(self):
        # returns color of the node
        return self.color

    def hasLeftChild(self):
        # returns true if node has left child
        if self.leftChild:
            return True
        else:
            return False

    def hasRightChild(self):
        # returns true if node has right child
        if self.rightChild:
            return True
        else:
            return False

    def hasParent(self):
        # returns true if node has parent
        if self.parentNode:
            return True
        else:
            return False

    def countChildren(self):
        """
        Counts the number of children the node has

        :return: number of children + the node itself
        """
        # number of left children
        leftCount = 0
        # number of right children
        rightCount = 0
        # if node has left child, go there and count it
        if self.hasLeftChild():
            leftCount += self.getLeftChild().countChildren()
        # if node has right child, go there and count it
        if self.hasRightChild():
            rightCount += self.getRightChild().countChildren()
        # return sum of children and self
        return leftCount + rightCount + 1
