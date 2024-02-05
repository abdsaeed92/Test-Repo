
#Abdulrahman Saeed Alfadhli#
#Q1: write a program to print the diamond shape 1- input 5

#Solution:
def Diamond(rows):
     n = 0
     for i in range(1, rows + 1):
# loop to print spaces
for j in range (1, (rows - i) + 1):
print(end = " ")

# loop to print star
# while n != (2 * i - 1):
print("1", end = "5")
        n = n + 1
        n = 0

# line break
print()

         k = 1
         n = 1
    for i in range(1, rows):
# loop to print spaces
       for j in range (1, k + 1):
          print(end = " ")
          k = k + 1

# loop to print star
while n <= (2 * (rows - i) - 1):
print("1", end = "5")
     n = n + 1
     n = 1
      print()
# Driver Code
# number of rows input
rows = 5
Diamond(rows)



#Q4
#solution:
procedure selection sort
    list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
        
end procedure
