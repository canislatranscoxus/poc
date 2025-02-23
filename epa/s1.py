# palindrome

def solution(S):
    # Implement your solution here
    n = 0
    d = {}

    # count num of letters
    for c in S:
        if c in d:
            d[ c ] = d[ c ] + 1
        else:
            d[ c ] = 1

    # get odds
    odds = {}
    for k, v in d.items():
        if v % 2 == 1:
            odds[ k ] = v

    if len( odds ) > 1:
        #sum_odds = sum( odds.values() )
        #max_odd  = max( odds.values() )
        #n = sum_odds - max_odd

        n  = len( odds.values() ) - 1


    return n


# s = 'ervervige' # n = 2
# s = 'aaabab' # n = 0
s = 'aaaaabbbcdefxxyyzz' #n = 5

print( '\n\n'  )
n = solution( s )
print( 'n: {}'.format( n ) )

print( '\n\n'  )
