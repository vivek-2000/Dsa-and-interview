#creating two linklist for head
class LinkList:
    def __init__(self):
        self.head=None

    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None

    def push(self,data):
        node=self.Node(data)
        node.next=self.head
        self.head=node

    def finalmaxList(self,head1,head2):
        prev1=head1
        curr1=head1
        prev2=head2
        curr2=head2
        result=None
        while curr1 or curr2:
            sum1=0
            sum2=0
            while curr1 and curr2 and curr1.data !=curr2.data:
                if curr1.data<curr2.data:
                    sum1+=curr1.data
                    curr1=curr1.next
                else:
                    sum2+=curr2.data
                    curr2=curr2.next
            #print(curr1.data)
            #print(curr2.data)
            #print(sum1)
            #print(sum2)
            #break
            if curr1==None:
                while curr2!=None:
                    sum2+=curr2.data
                    curr2=curr2.next
            if curr2==None:
                while curr1!=None:
                    sum1+=curr1.data
                    curr1=curr1.next

            if prev1==head1 and prev2==head2:
                if sum1>sum2:
                    result=prev1
                else:
                    result=prev2
            else:
                if sum1>sum2:
                    prev2.next=prev1.next
                else:
                    prev1.next=prev2.next
            prev1=curr1
            prev2=curr2
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        while result:
            print(result.data,end=" ")
            result=result.next
        




    def printLL(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next


list1=LinkList()
list2=LinkList()
list1.push(120)
list1.push(110)
list1.push(90)
list1.push(30)
list1.push(3)
list1.push(1)
  
list2.push(130)
list2.push(120)
list2.push(100)
list2.push(90)
list2.push(32)
list2.push(12)
list2.push(3)
list2.push(0)
  
list1.finalmaxList(list1.head, list2.head)


