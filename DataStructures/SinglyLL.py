class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL(object):
    def __init__(self):
        self.head = None
    
mySinLL = SinglyLL()
mySinLL.head = Node(1)
sec = Node(2)
thi = Node(3)
fou = Node(4)

mySinLL.head.next = sec
sec.next = thi
thi.next = fou
