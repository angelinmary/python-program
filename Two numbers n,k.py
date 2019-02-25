def binarySearch(arr, low, high, n): 
  
    if (high >= low): 
      
        mid = low + (high - low)//2
        if n == arr[mid]: 
            return (mid) 
        elif(n > arr[mid]): 
            return binarySearch(arr, (mid + 1), high, n) 
        else: 
            return binarySearch(arr, low, (mid --1), n)
