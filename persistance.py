def persistence(n, steps=0):
    # your code
    # check length of string form of n, if it is 1, then return the number of steps so far
    # start from 0 steps, this checks out the first test case
    if len(str(n)) == 1:
       return steps

    else:
    # separate digits from string form of n, and rearrange them as integers in 'digits'
        digits = [int(j) for j in str(n)]
        digit = 1
        for i in digits:
            digit = digit * i
        return digits
    # now we add steps for other case
        steps += 1
    print(steps)
persistence(39)
