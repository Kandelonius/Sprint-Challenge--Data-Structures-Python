class RingBuffer:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.head = 0
        # self.tail = -1

    def append(self, item):
        if len(self.queue) == self.capacity:
            self.queue[self.head] = item
            if self.head + 1 == self.capacity:
                self.head = 0
            else:
                self.head += 1
        else:
            self.queue.append(item)

    def get(self):
        return self.queue
    #     if self.head == -1:
    #         print("No element in the circular queue")
    #
    #     elif self.tail >= self.head:
    #         for i in range(self.head, self.tail + 1):
    #             print(self.queue[i], end=" ")
    #         print()
    #     else:
    #         for i in range(self.head, self.capacity):
    #             print(self.queue[i], end=" ")
    #         for i in range(0, self.tail + 1):
    #             print(self.queue[i], end=" ")
    #         print()


    #
    # def dequeue(self):
    #     if self.head == -1:
    #         print("The circular queue is empty\n")
    #
    #     elif self.head == self.tail:
    #         temp = self.queue[self.head]
    #         self.head = -1
    #         self.tail = -1
    #         return temp
    #     else:
    #         temp = self.queue[self.head]
    #         self.head = (self.head + 1) % self.capacity
    #         return temp
