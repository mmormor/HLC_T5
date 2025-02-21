def palabra(words):
    if len(words)<=1:
        return True
    elif words[0]!=words[-1]:
        return False
    else:
        return palabra(words[1:-1])
print(palabra("reconocer"))