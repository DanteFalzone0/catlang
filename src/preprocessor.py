def preproc_pure_func(pure_func_prototype):
    # By putting the "pure" qualifier before the return type
    # of a function in C@, you can ensure that the function
    # won't modify any of the variables passed to it,
    # whether by reference *or* by value.
    return pure_func_prototype.replace("pure", "").replace("(", "(const ").replace(",", ", const ")