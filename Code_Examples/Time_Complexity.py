def show_all(n):
    print("Starting") # This will run once (excluding the for loop) but note that this is accounted for as +1
    for i in range(n):
        print(i)
  ## Note that the time complexity is T(n) = n + 1 
# Example 2
def sum_to(n):
    total = 0 # +1
    for i in range(n): # +n 
        total = total + i
    return total # +1
  ## 2 + n -- this is what def sum_to(n) costs


def double_sum(n):
    x = sum_to(n) #(2 + n) + 1 
    y = sum_to(n) #(2 + n) + 1
    return x + y # + 1

## (2 + n) + 1 + (2 + n) + 1 + 1

## T(n) = 7 + 2n -- linear O(n) 
