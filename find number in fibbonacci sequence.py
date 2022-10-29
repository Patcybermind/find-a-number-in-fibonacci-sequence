def parity(number):
    #checks if its pair or not
    #[*immidiate]
    fli_in_bin_array = [*bin(for_loop_iteration)]
    #print(fli_in_bin_array)
    #get the last bit
    last_bit = int(fli_in_bin_array[-1])
    return(last_bit)

#prompt user for number of numbers to give
iterations = int(input("enter the max of fibonacci iterations or -1 for unlimited: "))
if iterations == -1:
    iterations = 1000000000000000000000
number_to_find = str(input("enter the number you want to find : "))

#iteration 0
print("iteration : 0, number : 0")

# first iteration
print("iteration : 1, number : 1")
fib_n1 = 1
fib_n2 = 0

for for_loop_iteration in range(2,iterations + 1):

    if parity(for_loop_iteration) == 1:
        #odd numbers
        fib_n1 = fib_n1 + fib_n2
        current_iteration_answer = fib_n1
    else:
        #pair numbers
        fib_n2 = fib_n1 + fib_n2
        current_iteration_answer = fib_n2
    # prints the current iteration and number
    print(f"iteration : {for_loop_iteration} number : {current_iteration_answer}")
    current_iteration_answer = str(current_iteration_answer)
    if current_iteration_answer.find(number_to_find) == (-1):
        pass
    else:
        print(f"found {number_to_find} in iteration {for_loop_iteration} starting at character {current_iteration_answer.find(number_to_find)}")
        exit()
print("could not find number, please increase the maximum number of iterations")