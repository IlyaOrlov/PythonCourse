def outer_fun(target_func): 
    """ 
    Полезный комментарий
    """ 
    def inner_fun(*args, **kwargs): 
	    # Делаем что-то перед вызовом функции
        res = target_func(*args, **kwargs) 
	    # Делаем что-то после вызова функции
        return res 
    return inner_fun
	
def new_fun(a, b, k=12, d=10):
    pass

new_fun(10, 20) 	
new_fun(b=10, a=20, k=3)
new_fun = outer_fun(new_fun)
new_fun(10, 20) 	
new_fun(b=10, a=20, k=3)

	
len = outer_fun(len)
len([1,2,3,4,5])	
