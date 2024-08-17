class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("Enter element to be pushed into the stack : "))
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped Element is :", self.top.data)
            print("-----------------------------------")
            self.top = None
        else:
            temp = self.top
            print("Popped Element is :", self.top.data)
            print("------------------------------------")
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Stack is empty\n---------------------")
        else:
            print("Elements of the stack are :")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is :", self.top.data)
            print("--------------------------------------")


s = Stack()

while (1):
    print("Enter the option from below")
    print("1 - Push Operation")
    print("2 - Pop Operation")
    print("3 - Display Operation")
    print("4 - Exit")

    option = int(input())
    if option == 1:
        print("Push Operation\n------------")
        s.push()
    elif option == 2:
        print("Pop Operation\n------------")
        s.pop()
    elif option == 3:
        print("Display Operation\n------------")
        print(s.display())
    elif option == 4:
        print("Exiting...")
        break

