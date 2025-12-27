from ImplementStack import Stack

def balanced(s):
    e=Stack()
    maps={')':'(','}':'{',']':'['}

    for ch in s:
        if ch in '({[':
            e.push(ch)
        else:
            if not e:
                return False
            top=e.pop()
            if maps[ch]!=top:
                return False
    return True

print(balanced(s="(((())))"))