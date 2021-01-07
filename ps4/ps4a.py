# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    sequence = list(sequence)
    start = 0
    end=len(sequence)-1
    result = []
    def permute(sequence , start ,end ):
        if start == end:
            result.append("".join(sequence))
        else:
            for index in range(start,end+1):
                sequence[start],sequence[index] = sequence[index], sequence[start]
                permute(sequence, start + 1,end)
                sequence[start],sequence[index] = sequence[index], sequence[start]
        
    permute(sequence,start,end)
    return result

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abcd'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


