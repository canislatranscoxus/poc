def solution_old(N):
    enable_print = 1
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print == 1:
            print(N % 10, end="")
        N = N // 10

def solution(N):
    enable_print = N % 10
    while N > 0:
        #if enable_print == 0 and N % 10 != 0:
        #    enable_print = 1
        #elif enable_print == 1:
        print(N % 10, end="")
        N = N // 10


print( '\n\n' )
solution_old( 3210  )        
print( '\n\n' )