def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one = my_cycle(1)
    >>> add_one(1)
    2
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """

    input_func = (f1, f2, f3) # Tuple of input functions 

    def func_builder(n):
        """
        Returns a function that recursively calls this function.
        """
        
        count = (n % 3) - 1 # Gets index for desired function.
        this_func = input_func[count] # gets correct function.
        
        def this_cycle(x):
            """
            If the last cycle, acts as the identity function.
            Otherwise, calls the next-lowest function in the cycle.
            """
            if n == 0:
                return x
            else:
                return this_func(func_builder(n - 1)(x))
        
        return this_cycle
    
    return func_builder


