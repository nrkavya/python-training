'''def div(x,y):
    r = 0
    try:
        r =  x/y
    except(ZeroDivisionError):
        print("error")
    except(Exception):
        print('EXCEPTION')
    finally:
        print('HELLO iam from finally')
        return r
print(div(10,0))
print(div(10,2))'''

def div(x,y):
    r=0
    if(y==0):
        raise ZeroDivisionError
    else:
        return r

print(div(10,0))
print(div(10,2))
