class MyHashSet:

    def __init__(self):
        self.size=10
        self.data=[[] for _ in range(self.size)]

    def _hash(self,key:int)->int:
        return key%self.size

    def add(self, key: int) -> None:
        bucket=self._hash(key)

        if key not in self.data[bucket]:
            self.data[bucket].append(key)
        

    def remove(self, key: int) -> None:
        bucket=self._hash(key)

        if key in self.data[bucket]:
            self.data[bucket].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket=self._hash(key)

        return key in self.data[bucket]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)