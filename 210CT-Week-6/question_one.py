#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None



def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)

def in_orderItr(tree):                    # iterative || Bits added


    stack_node = []                       # empty list for init stack
    node_post = tree                      # set tree to node position
    condition = False

    while condition != True:

        if node_post != None:             # Start with the left node of the current position node

            stack_node.append(node_post)
            node_post = node_post.left

        
        # if the stack has no elements left it is done

        elif len(stack_node) > 0:

            node_post = stack_node.pop()     # pop/remove then print the node starting from the end of the list
            print (node_post.value)
            node_post = node_post.right     # once left area has been visited, move to the right tree.

        else:
            condition = True                # terminate the while loop




def in_orderRec(tree):
    if(tree.left!=None):
        in_orderRec(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_orderRec(tree.right)

if __name__ == '__main__':

  t = tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  tree_insert(t,7)
  in_orderItr(t
