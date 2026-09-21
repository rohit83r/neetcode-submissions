class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


class MyHashSet:

    def __init__(self):
        self.size=10
        self.set=[ListNode(0) for _ in range(self.size)]

    def _hash(self,key:int)->int:
        return key%self.size

    def add(self, key: int) -> None:
        bucket=self._hash(key)

        curr=self.set[bucket]
        while curr.next:
            if curr.next.val==key :
                return 
            curr=curr.next

        curr.next=ListNode(key)
            
        

    def remove(self, key: int) -> None:
        bucket=self._hash(key)
        curr=self.set[bucket]

        while curr.next:
            if curr.next.val==key:
                curr.next=curr.next.next
                return
            
            curr=curr.next
        
        return 

    def contains(self, key: int) -> bool:
        bucket=self._hash(key)
        curr=self.set[bucket]

        while curr.next:
            if curr.next.val==key:
                return True

            curr=curr.next

        return False

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)