def largest(arr,n):
     max=arr[0]
     for i in range(1,n):
          if(arr[i]>max):
                max=arr[i]
     return max
     
arr={10,20,4}
n=len(arr)
ans=largest(arr,n)
print("largest in given array id:" ans)
