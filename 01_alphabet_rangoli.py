import string
alpha = string.ascii_lowercase # getting english alphabet
size=3

def print_rangoli(size):
    M = []
    for i in range(0,size):
        letters = "-".join(alpha[i:size]) # base letters with "-" combine
        M.append((letters[::-1] + letters[1:] ).center(4*size-3, "-")) # all type line inside list

    print("\n".join(M[::-1] + M[1:]))  # up and down get together

print_rangoli(15)