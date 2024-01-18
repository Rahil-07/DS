# import math

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self) -> None:
        self.root = None
    
    def insert(self,data):
        self.insert_data = data
        self.new_node = Node(self.insert_data)
        if self.root == None:
            self.root = self.new_node
        else:
            self.insert_at(self.root)
        
    
    def insert_at(self,node):
        if self.insert_data <= node.data:
            if node.left == None:
                node.left = self.new_node
            else:
                self.insert_at(node.left)
        
        else:
            if node.right == None:
                node.right = self.new_node
            else:
                self.insert_at(node.right)

    def inorder(self,node):
        if node in None:
            return
        self.inorder(node.left)
        print(f"{node.data}",end=" ")
        self.inorder(node.right)
        




# def insert_node(node,key):
#     if key < node.data:
#         node.left = Node(key)
#     else:
#         node.right = Node(key)

# def find_insert_location(node,key):
#     if key < node.data:
#         if node.left == None:
#             return node
#         return find_insert_location(node.left,key)
#     else:
#         if node.right == None:
#             return node
#         return find_insert_location(node.right,key)

# def inorder(node):
#     if node is None:
#         return
#     inorder(node.left)
#     print(f" {node.data} ",end='')
#     inorder(node.right)

# def height(node):
#     if node is None:
#         return 0
#     else:
#         l_height = height(node.left)
#         r_height = height(node.right)     

#         if l_height > r_height:
#             return l_height+1
#         else:
#             return r_height+1

# def LevelOrder(root,height):
#     for i in range(1,height+1):
#         addCurrentLevel(root,i)

# def addCurrentLevel(node,level):
#     if node is None:
#         tree.append(None)
#         print("Tree : ",tree)
#     elif level == 1:
#         tree.append(node.data)
#         print("Tree : ",tree)
#     elif level > 1:
#         addCurrentLevel(node.left,level-1)
#         addCurrentLevel(node.right,level-1)

# if __name__ == '__main__':

#     lst = [3,2,1,5,4,8,5,8]

#     root = Node(lst[0])
    
#     for key in lst[1:]:
#         key_location = find_insert_location(root,key)
#         insert_node(key_location,key)
#         print(f"{key} successfully added")

#     print("\n")

#     inorder(root)
#     print("\n")
#     h_tree = height(root)
#     print(f"height of tree : {h_tree}\n")
#     # tree = [None]*(2**h_tree-1)
#     tree = []
#     LevelOrder(root,h_tree)
#     # print("Tree : ",tree)


#     tree = [1,2,3,4,None,6,7]

#     h_tree = 3
#     print("\n\n")

#     print(" "*((h_tree-1)*2),tree[0])

#     for i in range(1,len(tree)):
#         level = int(math.log(i+1,2))+1
#         if i == 2**(level-1)-1:     #for first node
#             print(" "*((h_tree-level)*2),tree[i] if tree!=None else str(" "),end="")
#         elif i == 2**level-2:       #for last node
#             print(" "*3,tree[i] if tree!=None else " ")
#         else:                       #for other node;
#             print(" "*3,tree[i] if tree!=None else " ",end="")
            