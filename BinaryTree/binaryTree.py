from Trees import treeNode
import math


class BinaryTree:
    def __init__(self, root=None):
        self.rootNode = root

    def getRoot(self):
        """
        Gets the root node of the tree
        :return: root node
        """
        # check if tree has root assigned
        if self.rootNode:
            return self.rootNode
        else:
            print("no root")
            return None

    def setRoot(self, root):
        """
        Sets root as the root of the tree
        :param root: new root for the tree
        :return: Nothing
        """
        self.rootNode = root
        root.parentNode = None

    def addNodes(self, nodes, previous=None):
        """
        Adds nodes from the nodes to the tree in order.
        if nodes is not a list or None, adds it to the right place in the tree.

        :param nodes: list of nodes to be added to the tree
        :param previous: previous node used in recursion
        :return: nothing
        """
        lista = self.checkDimension(nodes)
        # check if lista has values
        if len(lista) > 0:
            mid = (len(lista) / 2).__round__() -1
            # check if tree has root
            if not self.getRoot():
                rootNode = treeNode.TreeNode(value=lista.pop(mid))
                self.setRoot(rootNode)
            # check if previous has been assigned, else it is root
            if not previous:
                previous = self.getRoot()
            # split lista into smaller than previous and larger or equal to previous
            smaller = []
            larger = []
            for i in lista:
                if i < previous.value:
                    smaller.append(i)
                else:
                    larger.append(i)
            # if smaller than previous exists
            if len(smaller) > 0:
                if previous.hasLeftChild():
                    # send smaller values to the left child
                    self.addNodes(nodes=smaller, previous=previous.getLeftChild())
                else:
                    # add left child and go to that
                    mid = (len(smaller) / 2).__round__() -1
                    leftChild = treeNode.TreeNode(smaller.pop(mid))
                    previous.setLeftChild(leftChild)
                    if len(smaller) > 0:
                        self.addNodes(nodes=smaller, previous=previous.getLeftChild())
            if len(larger) > 0:
                if previous.hasRightChild():
                    # send larger or equal values to the right child
                    self.addNodes(nodes=larger, previous=previous.getRightChild())
                else:
                    # add right child
                    mid = (len(larger) / 2).__round__() -1
                    rightChild = treeNode.TreeNode(larger.pop(mid))
                    previous.setRightChild(rightChild)
                    if len(larger) > 0:
                        self.addNodes(nodes=larger, previous=previous.getRightChild())

    def checkDimension(self, nodes):
        """
        Takes in a list containing values to be added to the tree, makes sure the list is not multidimensional,
        and if it is, changes it into one dimensional
        :param nodes: a list of nodes to be added to the tree
        :return: a single dimensional list containing all values sorted
        """
        # list that collects values
        list1 = []
        # check that we are dealing with a list
        if type(nodes) == list:
            # check that list is not empty
            if len(nodes) > 0:
                # go through the list
                for i in range(len(nodes)):
                    # if list contains list, go through it with recursion and add its inner values to list2
                    if type(nodes[i]) == list:
                        list2 = self.checkDimension(nodes[i])
                        # go through list2 and append its values to list1
                        for j in range(len(list2)):
                            list1.append(list2[j])
                    # if nodes are not list, append them to list1
                    else:
                        list1.append(nodes[i])
        # if nodes is not list, return as list
        else:
            return [nodes]
        # sort the values and return
        list1.sort()
        return list1

    def getValuesFromTree(self, values=None, previous=None):
        """
        gets all the values from the trees nodes
        :param values: list of values that will be returned
        :param previous: previous node used in recursion
        :return: a list containing all values of the tree nodes
        """
        # check if values is not a list
        if type(values) != list:
            values = []
            # check if tree has root
        if self.getRoot():
            # check previous. for first iteration set root as previous
            if not previous:
                previous = self.getRoot()
            # check if previous has left child and go there if true
            if previous.hasLeftChild():
                self.getValuesFromTree(values=values, previous=previous.getLeftChild())
            # after going through left children, add value to values list
            values.append(previous.value)
            # check if node has right child and go there if true
            if previous.hasRightChild():
                self.getValuesFromTree(values=values, previous=previous.getRightChild())
            return values

    def getNodesFromTree(self, nodes=None, previous=None):
        """
        gets all the nodes from the tree
        :param nodes: list of nodes that will be returned
        :param previous: previous node used in recursion
        :return: a list containing all nodes of the tree
        """
        # check if nodes is not a list
        if type(nodes) != list:
            nodes = []
            # check if tree has root
        if self.getRoot():
            # check previous. for first iteration set root as previous
            if not previous:
                previous = self.getRoot()
            # check if previous has left child and go there if true
            if previous.hasLeftChild():
                self.getNodesFromTree(nodes=nodes, previous=previous.getLeftChild())
            # after going through left children, add node to nodes list
            nodes.append(previous)
            # check if node has right child and go there if true
            if previous.hasRightChild():
                self.getNodesFromTree(nodes=nodes, previous=previous.getRightChild())
            return nodes

    def countNodes(self, node=None):
        """
        Counts the nodes of the tree or to the current node
        :return: number of nodes in the tree
        """
        # if root is not assigned, tree contains 0 nodes
        if not self.getRoot():
            return 0
        # if starting node wasn't given, count starts from root
        if not node:
            node = self.getRoot()
        # number of left children
        leftCount = 0
        # number of right children
        rightCount = 0
        # if node has left child, go there and count it
        if node.hasLeftChild():
            leftCount += self.countNodes(node.getLeftChild())
        # if node has right child, go there and count it
        if node.hasRightChild():
            rightCount += self.countNodes(node.getRightChild())
        # return sum of children and self
        return leftCount + rightCount + 1

    def countLeftChildren(self, startingNode=None, recNode=None):
        """
        Counts the number of left children the node has
        :param startingNode: node whose left children are counted
        :param recNode: node that is used in recursion
        :return: number of left children, doesn't count the starting node
        """
        # if starting node wasn't given, count starts from root
        if not startingNode:
            if self.getRoot():
                startingNode = self.getRoot()
            else:
                return 0
        # only in first recursion
        if not recNode:
            # if starting node has left child, go there using recursion, count children and return the sum
            if startingNode.hasLeftChild():
                return self.countLeftChildren(startingNode,startingNode.getLeftChild())
            # if starting node has no left child, return 0
            else:
                return 0
        # number of left children
        leftCount = 0
        # number of right children
        rightCount = 0
        # if node has left child, go there and count it
        if recNode.hasLeftChild():
            leftCount += self.countNodes(recNode.getLeftChild())
        # if node has right child, go there and count it
        if recNode.hasRightChild():
            rightCount += self.countNodes(recNode.getRightChild())
        # return sum of children and self
        return leftCount + rightCount + 1

    def countRightChildren(self, startingNode=None, recNode=None):
        """
        Counts the number of right children the node has
        :param startingNode: node whose left children are counted
        :param recNode: node that is used in recursion
        :return: number of right children, doesn't count the starting node
        """
        # if starting node wasn't given, count starts from root
        if not startingNode:
            if self.getRoot():
                startingNode = self.getRoot()
            else:
                return 0
        # only in first recursion
        if not recNode:
            # if starting node has right child, go there using recursion, count children and return the sum
            if startingNode.hasRightChild():
                return self.countRightChildren(startingNode,startingNode.getRightChild())
            # if starting node has no right child, return 0
            else:
                return 0
        # number of left children
        leftCount = 0
        # number of right children
        rightCount = 0
        # if node has left child, go there and count it
        if recNode.hasLeftChild():
            leftCount += self.countNodes(recNode.getLeftChild())
        # if node has right child, go there and count it
        if recNode.hasRightChild():
            rightCount += self.countNodes(recNode.getRightChild())
        # return sum of children and self
        return leftCount + rightCount + 1

    def countHeight(self, node=None):
        """
        Counts and returns the height of the current node
        Height is the number of edges between node and lowest leaf
        :return: Height of the node, height of tree if node is root
        """
        # check if node was given
        if not node:
            # if not, check if tree has root
            if self.rootNode:
                # if yes, node is root
                node = self.getRoot()
            # else height is 0
            else:
                return 0
        # height of the left children
        left = 0
        # height of the right children
        right = 0
        # if node has left child, go there and count the height
        if node.hasLeftChild():
            left += self.countHeight(node=node.getLeftChild())
        # if node has right child, go there and count the height
        if node.hasRightChild():
            right += self.countHeight(node=node.getRightChild())
        # return the max between left and right and add 1 to it to get current height
        return max(left,right)+1

    def isBalanced(self, node=None):
        """
        checks if the current tree or node and it's children are balanced.
        If node is not given, starts from the root

        :param node: optional starting node
        :return: True if balanced, False otherwise
        """
        # if node was not given and tree has root, node is root
        if not node:
            if self.getRoot():
                node = self.getRoot()
            else:
                # if tree doesn't have root, return True
                return True
        balance = True
        left = 0
        right = 0
        # check if node has left child
        if node.hasLeftChild():
            # count the number of left children the node has
            left = self.countLeftChildren(node)
            # check left children's balance recursively
            balance = self.isBalanced(node=node.getLeftChild())
        # if node has right child
        if node.hasRightChild():
            # count the number of right children the node has
            right = self.countRightChildren(node)
            # check right children's balance recursively
            balance = self.isBalanced(node=node.getRightChild())
        # if the difference between the sum of left and right children is 1 or less, return True, else return False
        if not math.sqrt((left-right)**2) <= 1:
            balance = False
        return balance

    def balanceTree(self, node=None, recParent=None):
        """
        Balances the tree if not balanced
        :param node: node used in recursion or as starting node, if not given start from root
        :param recParent: parent node used in recursion
        :return: Nothing
        """
        # todo
        # check if tree is already balanced
        if self.isBalanced():
            return
        else:
            # balancing tree
            # check if node was given
            if not node:
                # if not, check if tree has root
                if self.rootNode:
                    # node is root
                    node = self.getRoot()
                else:
                    # tree has no root so tree is empty
                    print("Tree is empty")
            # count roots l and r children
            # look from the larger side
            # for node with enough r children + parent to even the tree
            # make that node new root, its parent + right children go right, rest go left

            # if node has left child, count it and its children
            if node.hasLeftChild():
                left = node.getLeftChild().countChildren()
            else:
                left = 0
            # if node has right child, count it and its children
            if node.hasRightChild():
                right = node.getRightChild().countChildren()
            else:
                right = 0
            # while current nodes' children are not in balance
            while math.sqrt((left - right)**2) > 1:
                # balancing the tree
                # if left side is larger
                if left > right:
                    # left side has more nodes
                    lChild = node.getLeftChild()
                    if lChild.hasRightChild():
                        grandChild = lChild
                        # find first grandchild with no right child and it will get the smaller side as its new children
                        while grandChild.hasRightChild():
                            grandChild = grandChild.getRightChild()

                        node.popLeftChild()
                        grandChild.setRightChild(node)

                        if node == self.rootNode:
                            # if node was previous root, lChild is new root
                            self.setRoot(lChild)
                        else:
                            # else get nodes parent
                            parent = node.getParent()
                            if parent.hasLeftChild():
                                if parent.getLeftChild() == node:
                                    parent.setLeftChild(lChild)
                                else:
                                    parent.setRightChild(lChild)
                        node = lChild
                    else:
                        # lchild has no r Child
                        if node == self.rootNode:
                            # if node was previous root, lChild is new root
                            self.setRoot(lChild)
                        else:
                            # else get nodes parent
                            parent = node.getParent()
                            # lchild takes nodes place as parents l or r child
                            if parent.hasLeftChild():
                                if parent.getLeftChild() == node:
                                    parent.setLeftChild(lChild)
                                else:
                                    parent.setRightChild(lChild)
                        # then node pops left child
                        node.popLeftChild()
                        # node becomes right child of lchild
                        lChild.setRightChild(node)
                        # and next repeat while with lChild
                        node = lChild
                else:
                    # right side has more nodes
                    rChild = node.getRightChild()
                    if rChild.hasLeftChild():
                        grandChild = rChild
                        # find the first grandchild with no left child. It will get the smaller side as its new children
                        while grandChild.hasLeftChild():
                            grandChild = grandChild.getLeftChild()

                        if node == self.rootNode:
                            # if node was previous root, rChild is new root
                            self.setRoot(rChild)
                        else:
                            # else get nodes parent
                            parent = node.getParent()
                            # check if node was parent's left or right child and make rChild as parents that child
                            if parent.hasLeftChild():
                                if parent.getLeftChild() == node:
                                    parent.setLeftChild(rChild)
                                else:
                                    parent.setRightChild(rChild)
                        # pop right child from node
                        node.popRightChild()
                        # set node as grandChilds left node
                        grandChild.setLeftChild(node)
                        # and in next loop rChild is node
                        node = rChild
                    else:
                        # rChild has no l child
                        if node == self.rootNode:
                            # if node was previous root, rChild is new root
                            self.setRoot(rChild)
                        else:
                            # else get nodes parent
                            parent = node.getParent()
                            # rChild takes nodes place as parents l or r child
                            if parent.hasLeftChild():
                                if parent.getLeftChild() == node:
                                    parent.setLeftChild(rChild)
                                else:
                                    parent.setRightChild(rChild)
                        # then node pops the right child
                        node.popRightChild()
                        # node becomes the left child of rChild
                        rChild.setLeftChild(node)
                        # and next repeat with rChild
                        node = rChild
                # count nodes again
                if node.hasLeftChild():
                    left = node.getLeftChild().countChildren()
                else:
                    left = 0
                if node.hasRightChild():
                    right = node.getRightChild().countChildren()
                else:
                    right = 0
            # after while is done, use recursion for the children
            if node.hasLeftChild():
                self.balanceTree(node=node.getLeftChild())
            if node.hasRightChild():
                self.balanceTree(node=node.getRightChild())

    def printTree(self):
        """
        Prints values of the tree nodes. depth is displayed on the left side, the tree is after ":"
        :return: nothing
        """
        # check if tree is empty
        if not self.rootNode:
            print("empty tree")
            return
        else:
            # else get the root
            node = self.getRoot()
        # get the height of the tree
        height = self.countHeight()
        padding =""
        for i in range(height):
            padding +=" "*(height)
        # nodes will be saved here
        nodes = [[]for i in range(height+1)]
        #add root to nodes[0]
        nodes[0].append(node)
        # loop through every depth level of the tree
        for i in range(height-1):
            # if first loop, print value of root
            if i == 0:
                printable = str(i + 1) + ":" + padding[:(round(len(padding)/2))]
                printable += str(nodes[i][0].value)
                print(printable)
            # add current depth to the printable
            printable = str(i+2) + ": "
            current = round(len(padding)/(2**(i+2)))
            if current < 1:
                current = 1

            # loop through every node in current depth
            for x in nodes[i]:
                printable += padding[:current]
                # if x is string, append empty space to nodes i+1 and print some empty space
                if type(x) == str:
                    nodes[i+1].append(" ")
                    nodes[i+1].append(" ")
                    printable +=("* *")
                    printable += padding[:current]
                    printable += padding[:current]

                else:
                    # if x is not string we assume it's treeNode
                    # check left child and append nodes[i+1] with it if true for future loops
                    # also add its value to printable
                    if x.hasLeftChild():
                        nodes[i+1].append(x.getLeftChild())
                        printable += str(x.getLeftChild().value)
                    else:
                        # if no left child, append empty space and also add it to printable
                        nodes[i+1].append(" ")
                        printable += "*"
                    # print parts of padding between left and right child
                    printable += padding[:current]
                    printable += padding[:current]

                    # check right child and append nodes[i+1] with it if true for future loops
                    # also add its value to printable
                    if x.hasRightChild():
                        nodes[i+1].append(x.getRightChild())
                        printable += str(x.getRightChild().value)
                    else:
                        # if no right child, append empty space and also add it to printable
                        nodes[i+1].append(" ")
                        printable += "* "
                    # add padding after this nodes children
                    printable += padding[:(round(len(padding) / (2 ** (i + 2))))]
            # print the printable which now contains values and empty spaces according to current depth
            print(printable)

    def isInorder(self, node=None, last = [[None],[None]]):
        """
        checks if the tree is in order or not
        tree is in order if left children are smaller than parent and larger than last[1][0]
        and right children are larger than parent and smaller than last[0][0]
        :param node: starting node. if not given, root is used.it is also used in recursion.
        :param last: used in recursion. Saves the parents from last getLeftChild or getRightChild calls
        :return: True if tree values are in order, False otherwise
        """
        # check if node was given
        if not node:
            # check if tree has root
            if self.rootNode:
                # if node wasn't given and tree has root, node is root
                node = self.getRoot()
            else:
                # if tree has no root, it's in order
                return True
        # inOrder is going to be returned as true if all values are in order and false if not
        inOrder = True
        # get the value of the current node
        currentValue = node.value
        # check if node has left child
        if node.hasLeftChild():
            if node.value > node.getLeftChild().value:
                # check if last right exists
                if last[1][0]:
                    # check if left child is larger than last right, if not return false
                    if last[1][0].value < node.getLeftChild().value:
                        # go to left child using recursion. There current node is now last left
                        inOrder = self.isInorder(node=node.getLeftChild(),last=[[node],[last[1][0]]])
                    else:
                        inOrder = False
                # check if last right exists
                # if so, leftchild value should be larger than that
                else:
                    inOrder = self.isInorder(node=node.getLeftChild(), last=[[node],[last[1][0]]])
            else:
                inOrder = False
        if inOrder == False:
            return inOrder
        #check if node has right child
        if node.hasRightChild():
            if node.value < node.getRightChild().value:
                # check if last left exists
                if last[0][0]:
                    # if so, right child value should be smaller than that
                    if node.getRightChild().value < last[0][0].value:
                        # go to right child using recursion. New current node is right child of the previous one and
                        # last right is the (previous) node
                        inOrder = self.isInorder(node.getRightChild(), [[last[0][0]],[node]])
                    else:
                        inOrder = False
                else:
                    inOrder = self.isInorder(node=node.getRightChild(),last=[[last[0][0]],[node]])

            else:
                inOrder = False
        # return boolean inOrder
        return inOrder

    def sortTree(self, node=None, last= [[None],[None]]):
        """
        Sorts trees values in order (all values in left side smaller than parent, all values in right side larger than parent)
        :param node: current node that is being processed
        :param last: last left and right turns in recursion
        :return: nothing
        """
        # check if node was given, if not, node is root (if root exists, else  pritn empty tree and return)
        if not node:
            if self.rootNode:
                node = self.getRoot()
            else:
                print("empty tree")
                return
        # check if node has left child
        if node.hasLeftChild():
            # check if left child is smaller than parent
            if node.getLeftChild().value < node.value:
                # check if last right turn exists
                if last[1][0]:
                    # check if left child is larger than last right turn
                    if node.getLeftChild().value > last[1][0].value:
                        # recursion on left child, node is now last left turn
                        self.sortTree(node.getLeftChild(),[[node],[last[1][0]]])
                    else:
                        # last right turn is larger than left child
                        print("Previous right turn {} is larger than current left child {},"
                              " even though it should be smaller".format(last[1][0].value,node.getLeftChild().value))
                        # remove left child from tree
                        lChild = node.popLeftChild()
                        # get the value of left child and all its children to a list
                        lista = lChild.getAllValues()
                        # add the values from the list to the tree
                        self.addNodes(lista)

                else:
                    # there's no last right turn so recursion on left child, node is now last left turn
                    self.sortTree(node.getLeftChild(), [[node],[last[1][0]]])
            else:
                # node is smaller than its left child
                print("Current node {} is smaller than its left child {}".format(node.value,node.getLeftChild().value))
                # remove left child from tree
                lChild = node.popLeftChild()
                # add values of left child and all its children to a list
                lista = lChild.getAllValues()
                # add the values in list to the tree
                self.addNodes(lista)
        # check if right child exists
        if node.hasRightChild():
            # check if right child is larger than or equal to current node
            if node.getRightChild().value >= node.value:
                # check if last left turn exists
                if last[0][0]:
                    # check if right child is smaller than last left turn
                    if node.getRightChild().value < last[0][0].value:
                        # recursion on right child, node is now last right child
                        self.sortTree(node.getRightChild(), [[last[0][0]],[node]])
                    else:
                        # last left turn was smaller than right child
                        print("Previous left turn {} is smaller than right child {},"
                              " even though it should be larger".format(last[0][0].value,node.getRightChild().value))
                        # remove right child from tree
                        rChild = node.popRightChild()
                        # add values of right child and all its children to a list
                        lista = rChild.getAllValues()
                        # add the values from the list to the tree
                        self.addNodes(lista)

                else:
                    # no last left turn, so use recursion on right child, node is now last right turn
                    self.sortTree(node.getRightChild(), [[last[0][0]],[node]])
            else:
                # node is larger than its right child
                print("Current node {} is larger than its right child {}".format(node.value, node.getRightChild().value))
                # remove right child from the tree
                rChild = node.popRightChild()
                # add the values of right child and all its children to a list
                lista = rChild.getAllValues()
                # add teh values from the list to the tree
                self.addNodes(lista)

    def containsValue(self, value, node=None):
        """
        Looks for value and returns true if found in tree
        :param value: value that is being searched
        :return:True if value was found, False otherwise
        """
        try:
            found = False
            if not node:
                if self.rootNode:
                    node = self.getRoot()
                else: return found
            # check if current node is value
            if value == node.value:
                found = True
            if found:
                return found
            # check if value is smaller than current node
            if value < node.value:
                # check if node has left child
                if node.hasLeftChild():
                    # use recursion with left child
                     found = self.containsValue(value, node.getLeftChild())
                else:
                    # value was smaller but there was no left child so value doesn't exist
                    found = False
            elif value > node.value:
                # if value is larger than current node, check if node has right child
                if node.hasRightChild():
                    # if node has right child, use recursion on it, else value doesn't exist
                    found = self.containsValue(value,node.getRightChild())
                else: found = False
        except TypeError:
            print("Tree contains different type of value than the value that was being searched")
        finally:
            return found

    def searchNode(self, value, node=None):
        """
        looks for nodes with node.value of value
        :param value: value that is being searched for
        :return: returns list of nodes with node.value == value
        """
        try:
            lista = []
            if not node:
                if self.rootNode:
                    node = self.getRoot()
                else:
                    return lista

            if value < node.value:
                if node.hasLeftChild():
                    lista = self.searchNode(value, node.getLeftChild())
            elif value >= node.value:
                if node.hasRightChild():
                    lista = self.searchNode(value,node.getRightChild())
                if node.value == value:
                    lista.append(node)
        except TypeError:
            print("Tree contains different type of value than the value that was being searched")
        except:
            print("something went HORRIBLY wrong")
        finally:
            return lista


