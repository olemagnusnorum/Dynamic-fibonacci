import time

class fibonacciGetter:
    
    def __init__(self):
        self.fibonacciList = [0, 1]
    
    # dynamic fib
    def getFibonacciNr(self, number):
        if len(self.fibonacciList) > number:
            return self.fibonacciList[number]
        for i in range(len(self.fibonacciList),number+1):
            fibNr = self.fibonacciList[i-1] + self.fibonacciList[i-2]
            self.fibonacciList.append(fibNr)
        return self.fibonacciList[number]

    #recursive fib
    def fib(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    #compares the to differnt fib algorithms
    def compareFib(self, number):
        startTimeDynamic = time.time()
        self.getFibonacciNr(number)
        endTimeDynamic = time.time() - startTimeDynamic
        startTimeRec = time.time()
        self.fib(number)
        endTimeRec = time.time() - startTimeRec
        print(" the dynamic algorithm used: %.2e seconds \n the recursive algorithm used: %.2e seconds"%(endTimeDynamic, endTimeRec))



if __name__ == "__main__":

    test = fibonacciGetter()
    test.compareFib(30)
