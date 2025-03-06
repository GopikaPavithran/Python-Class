def str_palindrome(s):
    if s[::-1]==s:
        return '%s is palindrome'%s
    else:
        return '%s is not palindrome'%s


def str_duplicate_remove(s):
    s_new=''
    for i in s:
        if i not in s_new:
            s_new+=i
    return s_new