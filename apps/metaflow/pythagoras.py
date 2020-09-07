from metaflow import FlowSpec, step
import numpy as np

class PythagorasFlow(FlowSpec):

    @step
    def start(self):
        self.nums = [1,2]
        self.next(self.declare, foreach="nums")

    @step
    def declare(self):
        self.x = 3 if self.input==1 else 4
        self.next(self.square)

    @step
    def square(self):
        self.sq = self.x**2
        self.next(self.join)

    @step
    def join(self,inputs):
        self.sum = sum([inp.sq for inp in inputs])
        self.next(self.end)

    @step
    def end(self):
        # it should print 5
        print(np.sqrt(self.sum))

if __name__ == '__main__':
    PythagorasFlow()
