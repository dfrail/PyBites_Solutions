'''
The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based)
'''

def get_index_different_char(chars):
    alnm = [char for char in chars if str(char).isalnum()]
    dif = [char for char in chars if not str(char).isalnum()]
    print(alnm)
    if len(alnm) < len(dif):
        return(chars.index(alnm[0]))
    elif len(alnm) > len(dif):
        return(chars.index(dif[0]))
