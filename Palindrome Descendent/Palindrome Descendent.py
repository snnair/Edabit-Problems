def palindrome_descendant(n):
    if (len(str(n)) == 2 and str(n)[0] == str(n)[1]) or str(n) == str(n)[::-1]:
        return True
    elif len(str(n))%2 != 0:
        return False

    n_string = ""
    for i in range(0,len(str(n)),2):
        x, y = str(n)[i], str(n)[i+1]
        n_string += str(int(x) + int(y))


    return palindrome_descendant(int(n_string)) if len(n_string) != 1 else False
