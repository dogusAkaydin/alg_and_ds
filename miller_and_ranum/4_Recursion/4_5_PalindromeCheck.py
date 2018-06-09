def isPalindrome(string):
    """Check if a given string is a palindrome."""
    if len(string) <= 1:
        return True
    else:
        return False if string[0] != string[-1] else isPalindrome(string[1:-1])

def test_isPalindrome(benchmark):
    """Test if isPalindrome function works as expected"""
    a_long_palindrome        = "eyedipadanadapideye"
    a_long_non_palindrome    = "eyedipadanadapideyem"
    one_letter               = "a"
    two_letter_palindrome    = "aa"
    two_letter_non_palindrome= "ab"

    assert isPalindrome(a_long_palindrome)         == True,  "FAIL: a_long_palindrome"
    assert isPalindrome(a_long_non_palindrome)     == False, "FAIL: a_long_non_palindrome"
    assert isPalindrome(one_letter)                == True,  "FAIL: one_letter"
    assert isPalindrome(two_letter_palindrome)     == True,  "FAIL: two_letter_palindrome"
    assert isPalindrome(two_letter_non_palindrome) == False, "FAIL: two_letter_non_palindrome"

    benchmark(isPalindrome, a_long_palindrome)

if __name__ == "__main__" :
    test_isPalindrome()




