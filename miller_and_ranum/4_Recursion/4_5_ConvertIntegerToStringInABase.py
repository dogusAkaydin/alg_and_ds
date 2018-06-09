def int2str(myInt,base):
    """Convert an integer to an integer represented as a string in a given base."""
    alphabet = "0123456789ABCDEF"     
    if myInt < base:
        return alphabet[myInt]
    else:
        return int2str(myInt//base,base) + alphabet[myInt%base]

def int2str_stack(myInt,base)
    """Convert an int to str in a given base using the stack impelemtation."""
    alphabet = "0123456789ABCDEF"     
    if myInt < base:
        
def test_int2str():
    testInt =10
    testBase=2
    correct ="1010"
    res=int2str(testInt,testBase)
    assert res==correct, "FAIL: {0} in base {1} is {2} -- not {3}".format(testInt,testBase,correct,res)

if __name__ == "__main__":
    test_int2str() 
