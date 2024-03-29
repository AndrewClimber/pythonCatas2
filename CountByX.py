'''
Create a function with two arguments that will return a list of length (n) with multiples of (x).

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array (or list in Python, Haskell or Elixir).

Examples:

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
'''
# aka
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [i*x for i in range(1,n+1)]
    #return list (map(lambda i: x*i, range(1,n+1)))


# codewars
def count_by1(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return range(x, x * n + 1, x)


####################
count_by2 = lambda x,n : list (range(x,n*x+1,x))
#######################


print(count_by2(2, 5))

