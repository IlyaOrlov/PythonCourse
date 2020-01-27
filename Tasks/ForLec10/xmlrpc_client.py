import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print( "3 is even: %s" % str(proxy.is_even(3)))
print("100 is even: %s" % str(proxy.is_even(100)))
