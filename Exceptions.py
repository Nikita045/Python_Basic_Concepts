try:
    raise Exception('spam','eggs')
except Exception as e:
    print(type(e))    #type class Exception
    print(e.args)
    print(e)
    x,y=e.args
    print('x=',x)
    print('y=',y)