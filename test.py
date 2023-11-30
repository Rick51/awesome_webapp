class A():
    def __init__(self):
        print("A init 被调用")
    def hi(self):
        print("A hi方法被调用")
    def hello(self):
        print("A hello方法被调用")

class B(A):
    #init函数:对象被创建的时候就会自动被调用
    def __new__(cls,*args,**kwargs):
        print("调用new方法")     
        #类实例化创建对象时候，会先调用new方法
        #分配内存空间给对象+返回对象的引用即self给init函数
        #所以重写new方法一定要有return super().__new__(cls)给到init,否则init的self是空
        return super().__new__(cls)
    '''
    #如果不重写__new__,其默认如下
    def __new__(cls,*args,**kwargs):
        return super().__new__(cls,*args,**kwargs)   
    '''   
    def __init__(self):
        super().__init__()                  #调用A的init
        print("B init 被调用")
    def __str__(self):
        return "通过__str__魔法函数,可以print出描述信息。"
    def helloB(self):
        self.hello()                        #B类没有hello函数，所以会默认调用到A的hello
        super().hello()                     #super() 表明同样是调用父类A的hello
        print("B helloB方法被调用")
    def hi():
        pass

b = B()
print(b)

#输出：
#A init 被调用
#B init 被调用
b.helloB()
#输出：
#A hello方法被调用
#A hello方法被调用
#B helloB方法被调用

#a = A()