def FibonacciSeq():#(user_input):
    '''
    The sequence follows the rule that each number is equal
    to the sum of the preceding two numbers. The Fibonacci 
    sequence begins with the following 14 
    integers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ... 
    Each number, starting with the third, 
    adheres to the prescribed formula
    '''
    user_input = int(input('Enter an integer: \n'))
    h = user_input
    f_seq = [1,2]
    while f_seq[-1] <= user_input:       
        d = f_seq[-1]+f_seq[-2]
        #print(f'd = {d}')
        f_seq.append(d)
        last_f = f_seq[-1]
        if user_input== 1:
            f_se1 = [1]
            return f_se1
            break
        elif user_input==2:
            f_se2 = [1,2]
            return f_se2
            break
        elif last_f>= user_input:
            h = False
            f_seq.pop()
            return f_seq
            break
        else:
            continue
print(FibonacciSeq())