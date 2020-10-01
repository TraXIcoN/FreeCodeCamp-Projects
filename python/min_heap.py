class Min_Heap():
    def __init__(self):
        self.arr = []

    def parent(self,i):
        parent = (i-1)//2
        return parent
    
    def left(self,i):
        left = 2*i +1
        return left
    
    def right(self,i):
        right = 2*i + 2
        return right
    
    def shiftup(self,i):
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

    def shiftdown(self,i,n):

        max_index = i
        l = self.left(i)
        if(l<n and self.arr[l] < self.arr[max_index]):
            max_index = l
        r = self.right(i)
        if(r<n and self.arr[r] < self.arr[max_index]):
            max_index = r
        if(i != max_index):
            self.arr[i], self.arr[max_index] = self.arr[max_index], self.arr[i]
            self.shiftdown(max_index,n)
    
    def push(self,val):
        self.arr.append(val)
        self.shiftup(len(self.arr)-1)

    def extract_min(self):
        result = self.arr[0]
        self.arr[0] = self.arr[len(self.arr)-1]
        self.arr.pop()
        self.shiftdown(0,len(self.arr))
        return result

    def remove(self,i):
        self.change(i,-1)
        self.shiftup(i)
        self.extract_min()

    def change(self,i,val):
        old = self.arr[i].value
        self.arr[i].value = val
        if(val > old):
            self.shiftdown(i,len(self.arr))
        else:
            self.shiftup(i)

    def print_min(self):
        print(self.arr[0])  

    def print_heap(self):
        print(self.arr)  





heap = Min_Heap()
n = int(input("Enter total number of elements : "))
for i in range(0,n):
    heap.push(int(input()))

choice = 0
while(choice!=7):
    print("Select Choice:")
    print("1) Add element")
    print("2) Remove element")
    print("3) Change element")
    print("4) Print Min")
    print("5) Print Heap")
    print("6) Remove Min")
    print("7) Exit")
    choice = int(input("Choice : "))
    if(choice == 1):
        val = int(input("Enter Element : "))
        heap.push(val)
    elif(choice == 2):
        heap.print_heap()
        val = int(input("Enter index to remove : "))
        heap.remove(val)
    elif(choice == 3):
        heap.print_heap()
        i = int(input("Enter index to change : "))
        val = int(input("Enter new value : "))
        heap.change(i, val)
    elif(choice == 4):
        heap.print_min()
    elif(choice == 5):
        heap.print_heap()
    elif(choice == 6):
        print(heap.extract_min())
        print("New Min")
        heap.print_min()