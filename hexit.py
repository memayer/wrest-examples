def hexit(num):
    result = []
    digits = "0123456789ABCDEF"
    while (True):
        r = num % 16
        num = num / 16
        result.insert(0, digits[r])
        if (num == 0):
            break
    return "".join(result)




def toHex(dec):
     r = (dec % 16)
     digits = "0123456789ABCDEF"
     q = dec / 16
     if (q == 0):
         return digits[r]
     return toHex(q) + digits[r]


def inner_reverse(s):
    s = list(s)
    start = 0
    end = 0
    while start < len(s):
        end += 1
        if s[end+1] == ' ':
            # reverse the string between here and start
            tmp_start = start
            tmp_end = end
            while tmp_start < tmp_end:
                s[end+1] = s[tmp_end] # we know this will be space when done
                s[tmp_end] = s[tmp_start]
                s[tmp_start] = s[end+1]
                tmp_start += 1
                tmp_end -= 1

            s[end+1] = ' '
            start = end+2

    return "".join(s)

foo = "Mary had a little lamb "
print inner_reverse(foo)
