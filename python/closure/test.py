# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("after myfunc() called.")
#     return func
 
# def myfunc():
#     print("myfunc() called.")
 
# myfunc = deco(myfunc)
 
# myfunc()
# myfunc()

# def deco(func):
# 	print("before myfunc() called.")
# 	func()
# 	print("after myfunc() called.")
# 	return func

# @deco
# def myfunc():
# 	print("myfunc() called.")
# myfunc()
# myfunc()

def deco(func):
	def _deco():
		print("before myfunc() called.")
		func()
		print("after myfunc().")
	return _deco

@deco
def myfunc():
	print("myfunc() called.")
	return 'ok'

myfunc()
myfunc()