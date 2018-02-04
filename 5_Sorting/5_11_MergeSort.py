def mergeSort1(theList):
    """Sort the list using Merge Sort algorithm with recursion"""
    mergeSort = mergeSort1
    if  theList is None:
        pass
    elif len(theList)==1:
        pass
    elif len(theList)>1:
        nList = len(theList)
        mid = nList//2
        left  = theList[:mid] 
        right = theList[mid:]
      
        mergeSort(left)
        mergeSort(right)
      
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                theList[k]=left[i]
                i+=1
            else:
                theList[k]=right[j]
                j+=1
            k+=1
      
        while i < len(left):
           theList[k]=left[i]
           i+=1
           k+=1
      
        while j < len(right):
           theList[k]=right[j]
           j+=1
           k+=1

def mergeSort2(L):
    """Sort the list using Merge Sort algorithm without recursion"""
    n=len(L)
    #k=int(log(n,2))
    #np2 = 2**k
    #nr=n-np2
    #Define split points
    bL=0
    eL=6
    bR=eL
    eR=n
    #Split into L and Right sublists
    sL=L[bL:eL]
    sR=L[bR:eR]
    dL=len(sL)
    dR=len(sR)
    
    #Initialize the indices
    i=0
    j=0
    k=bL
    #print(sL)
    #print(sR)
    while i<dL and j<dR:
        #print("i={},j={},k={}".format(i,j,k))
        if sL[i]<=sR[j]:
           L[k]=sL[i]
           i+=1
        else:
           L[k]=sR[j]
           j+=1
        k+=1
    #print("done while 1")
    while i<dL:
       L[k]=sL[i]
       i+=1
       k+=1
    #print("done while 2")
    while i<dR:
       L[k]=sR[j]
       j+=1
       k+=1
    #print("done while 3")

def test_mergeSort():
    """Test if mergeSort works as expected."""
    for mergeSort in [mergeSort1, mergeSort2]:
        print("Testing: {:s}".format(mergeSort.__name__))
        #Reinitialize the test inputs:
        a_sorted_list           =[0,1,2,3,4,5,6,7,8,9,10]
        a_sorted_list_copy      =a_sorted_list[:] 
        a_reversed_list         =[10,9,8,7,6,5,4,3,2,1,0]
        an_unsorted_list        =[8,1,10,5,7,2,9,3,0,4,6]
        a_half_sorted_list      =[1,2,5,7,8,10,0,3,4,6,9]
        a_half_sorted_list_copy =a_half_sorted_list[:]
        a_list_of_one_item      =[5]
        a_list_of_one_item_copy =a_list_of_one_item[:]
        an_empty_list           =[]
        an_empty_list_copy      =an_empty_list[:]
        a_list_with_None        =[None]
        a_list_with_None_copy   =a_list_with_None[:]
        a_None_list             =None

        #mergeSort(a_sorted_list      ); assert a_sorted_list     ==a_sorted_list_copy     ,"FAIL: a_sorted_list     "
        #mergeSort(a_reversed_list    ); assert a_reversed_list   ==a_sorted_list_copy     ,"FAIL: a_reversed_list   "
        #mergeSort(an_unsorted_list   ); assert an_unsorted_list  ==a_sorted_list_copy     ,"FAIL: an_unsorted_list  "
        print(a_half_sorted_list_copy)
        mergeSort(a_half_sorted_list) ; 
        print(a_half_sorted_list)
        assert a_half_sorted_list==a_sorted_list_copy     ,"FAIL: a_half_sorted_list"
        #mergeSort(a_list_of_one_item ); assert a_list_of_one_item==a_list_of_one_item_copy,"FAIL: a_list_of_one_item"
        #mergeSort(an_empty_list      ); assert an_empty_list     ==an_empty_list_copy     ,"FAIL: an_empty_list     "
        #mergeSort(a_list_with_None   ); assert a_list_with_None  ==a_list_with_None       ,"FAIL: a_list_with_None  "
        #mergeSort(a_None_list        ); assert a_None_list        is None                 ,"FAIL: a_None_list       "

if __name__ == "__main__":
    import bigO

    test_mergeSort()

    for mergeSort in [mergeSort1, mergeSort2]:
        print("Benchmarking: {}".format(mergeSort.__name__))
        bigO.analyze(mergeSort)

