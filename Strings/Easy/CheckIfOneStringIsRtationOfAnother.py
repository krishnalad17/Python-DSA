def rotation(s,goal):
    if len(goal)!=len(s):
        return False
    return goal in s+s

def rotation1(s,goal):
    if len(goal)!=len(s):
        return False
    for i in range(len(s)-1):
        rotated=s[i:]+s[0:i]
        if rotated==goal:
            return True
    return False

print(rotation1(s="rotation",goal="tionrota"))