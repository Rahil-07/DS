class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node = Node(data)
        # if self.head == None:
        #     self.head = node
        node.next = self.head
        self.head = node
    
    def insert_after_node(self,previous,data):
        node = Node(data)
        after_node = self.head
        while after_node.data != previous:
            after_node = after_node.next
        
        node.next = after_node.next
        after_node.next = node
    
    def insert_at_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return 0
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = node
    
    def delete_at_beg(self):
        if self.head == None:
            print("List is already Empty")
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def delete_after_node(self,previous):
        after_node = self.head
        while after_node.data != previous:
            after_node = after_node.next
            
        if after_node.next == None:
            print("end of list")
        temp = after_node.next.data
        after_node.next = after_node.next.next
        return temp
    
    def delete_at_end(self):
        if self.head == None:
            print("LIst is already empty")
        if self.head.next == None:
            temp = self.head.data
            self.head = None
            return temp

        last = self.head
        while(last.next.next):
            last = last.next
        temp = last.next.data
        last.next = None
        return temp

    def print_list(self):
        if self.head == None:
            print("List is Empty")
        temp = self.head
        while(temp.next):
            print(f"{temp.data}",end=" ")
            temp = temp.next
        print(f"{temp.data}")
    


if __name__ == "__main__":
    # 1. insert_at_end
    # 2. insert_after_node
    # 3. insert_at_beg
    # 4. delete_at_end
    # 5. delete_after_node
    # 6. delete_at_beg
    # 7. print_list

    linked_list =  LinkedList()
    user_input = int(input("Enter : "))
    while user_input != 0:
        if user_input == 1:
            data = int(input("Enter data : "))
            linked_list.insert_at_end(data)

        elif user_input == 2:
            data = int(input("Enter value : "))
            previous = int(input("Enter after value "))
            linked_list.insert_after_node(previous,data)

        elif user_input == 3:
            data = int(input("Enter data : "))
            linked_list.insert_at_beg(data)

        elif user_input == 4:
            temp = linked_list.delete_at_end()
            print(f"{temp} deleted")

        elif user_input == 5:
            previous = int(input("Enter after value : "))
            temp = linked_list.delete_after_node(previous)
            print(f"{temp} deleted")

        elif user_input == 6:
            temp = linked_list.delete_at_beg()
            print(f"{temp} deleted")

        elif user_input == 7:
            linked_list.print_list()
            
        user_input = int(input("Enter : "))