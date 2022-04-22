https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.front = list()
        self.back = list()
        
    def shift(self):
        while self.front:
            self.back.append(self.front.pop())

    def push(self, x: int) -> None:
        self.front.append(x)
        print("push ", self.front)
        

    def pop(self) -> int:
        if len(self.back) != 0:
            return self.back.pop()
        self.shift()
        return self.back.pop()


    def peek(self) -> int:
        if len(self.back) == 0:
            self.shift()
        return self.back[-1]

    def empty(self) -> bool:
        if not self.front and not self.back:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()