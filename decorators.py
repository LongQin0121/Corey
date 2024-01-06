def outer_function(msg):
    message =msg

    def inner_function():
        print(message)
    return inner_function()
my_fuc = outer_function
bye_fuc = outer_function('bye')

my_fuc('HHH')