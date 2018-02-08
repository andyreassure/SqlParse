
def getBasic(oldlist):
    newlist = []
    for item in oldlist:
        if isinstance(item, dict):
            pass
        elif isinstance(item, (list, tuple)):
            parts = getBasic(item)
            newlist.extend(parts)
        else:
            newlist.append(item)
    return newlist


if __name__ == '__main__':
    data = [1, 2, 3, 4, [4, 3, 2, ['a', 'v']]]
    print(getBasic(data))