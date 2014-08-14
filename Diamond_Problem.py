class A(object):
    def foo(self):
        print "A"
 
class B(A):
    def foo(self)
        print "B"
 
class C(A):
    def foo(self):
        print "C"
 
class D(B,C):
    def foo(self):
        print "D"
 
d = D()
d.foo()


#Output: D

#Change class D here to see the result, now it calls method form B class 
class D(B,C):
	pass

d = D()
d.foo()

#Output: B