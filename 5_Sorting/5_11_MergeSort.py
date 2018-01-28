def mergeSort(theList):
    """Sort the list using Merge Sort algorithm"""
    if len(theList) > 1:
        nList = len(theList)
        mid = nList // 2
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

if __name__ == "__main__":
    import bigO
    bigO.analyse(mergeSort)
