def likes(names):
    if len(names) <= 0:
        return "no one likes this"
    
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        l = len(names)
        l -= 2
        return f"{names[0]}, {names[1]} and {l} others like this"
        