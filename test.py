class A():
    def __init__(self):
        print("A init 被调用")
    def hi(self):
        print("A hi方法被调用")
    def hello(self):
        print("A hello方法被调用")

class B(A):
    #init函数:对象被创建的时候就会自动被调用
    def __init__(self):
        super().__init__()                  #调用A的init
        print("B init 被调用")
    def helloB(self):
        self.hello()                        #B类没有hello函数，所以会默认调用到A的hello
        super().hello()                     #super() 表明同样是调用父类A的hello
        print("B helloB方法被调用")
    def hi():
        pass

b = B()
#输出：
#A init 被调用
#B init 被调用
b.helloB()
#输出：
#A hello方法被调用
#A hello方法被调用
#B helloB方法被调用

#a = A()