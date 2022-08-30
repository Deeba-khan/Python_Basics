#raise
#'raise' is a keyword, used it to raise an exception or error, and stops the control flow of code
#with 'raise' keyword we can defined what kind of error to raise, and text to printout

x = "Broken"
if not type(x) is int:
    raise Exception("x type should be integer")
