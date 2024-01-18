class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def insert(self,data):
        node = Node(data)
        if self.front==None and self.rear==None:
            self.front = self.rear = node
            return 
        
        self.rear.next = node
        self.rear = node
    
    def delete(self):
        if self.front == None:
            print("Queue is Empty")
            return 
        temp = self.front.data
        self.front = self.front.next
        return temp
    
    def print_queue(self):
        if self.front == None:
            print("Queue is Empty")
            return 
        temp = self.front
        while temp != self.rear:
            print(f"{temp.data}",end=" ")
            temp =  temp.next
        print(f"{self.rear.data}")

if __name__ == "__main__":
    # 1. insert(data)
    # 2. delete
    # 3. print_queue
    q = Queue()

    user_str = int(input("Enter : "))

    while user_str != 0:
        if user_str == 1:
            data = int(input("Enter a data : "))
            q.insert(data)
        elif user_str == 2:
            deleted = q.delete()
            print(f"{deleted} deleted")
        elif user_str == 3:
            q.print_queue()

        user_str = int(input("Enter : "))
