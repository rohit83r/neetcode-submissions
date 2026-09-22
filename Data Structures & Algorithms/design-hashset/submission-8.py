class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if self.root is None:
            self.root=TreeNode(key)
            return

        curr=self.root

        while True:
            if key==curr.key:
                return 

            if key < curr.key:
                if curr.left is None:
                    curr.left=TreeNode(key)
                    return
                else:
                    curr=curr.left

            else:
                if curr.right is None:
                    curr.right=TreeNode(key)
                    return
                else:
                    curr=curr.right

    def search(self,key):
        curr=self.root

        while curr:
            if curr.key==key:
                return True

            if key < curr.key:
                curr=curr.left
            else :
                curr=curr.right

        return False

    def delete(self,key):
        self.root=self.remove(self.root,key)

    def remove(self,curr,key):

        if curr is None:
            return 

        if key < curr.key:
            curr.left=self.remove(curr.left,key)

        elif key > curr.key:
            curr.right=self.remove(curr.right,key)

        else:
            if curr.left is None:
                return curr.right

            elif curr.right is None:
                return curr.left

            else:
                succ=curr.right
                while succ.left:
                    succ=succ.left

                curr.key=succ.key
                curr.right=self.remove(curr.right,succ.key)

            
        return curr



class MyHashSet:

    def __init__(self):
        self.size=1000
        self.set=[BST() for _ in range(self.size)]

    def _hash(self,key:int)->int:
        return key%self.size

    def add(self, key: int) -> None:
        bucket=self._hash(key)
        self.set[bucket].insert(key)
            
    def remove(self, key: int) -> None:
        bucket=self._hash(key)
        self.set[bucket].delete(key)

    def contains(self, key: int) -> bool:
        bucket=self._hash(key)
        return self.set[bucket].search(key)

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)