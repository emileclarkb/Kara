# get word prior to other word
def prior(text, word):
    try:
        # split str to list
        split = text.split()
        # find where days was said
        index = split.index(word)
        p = split[index - 1] # get prior

        return p
    # word not in text
    except ValueError:
        return 0


# get cache to ability difference
def difference(abPath, cPath):
    # path to list
    abPath = abPath.split('/')
    cPath = cPath.split('/')

    # shared paths
    shared = []

    # move through
    i = 0
    while True:
        try:
            # current dir shared
            if abPath[i] == cPath[i]:
                # add dir
                shared.append(abPath[i])
            else:
                break
        except:
            pass

        i += 1

    # list to path
    shared = '/'.join(shared) + '/'
    abPath = '/'.join(abPath)
    cPath = '/'.join(cPath)

    # store cache value
    oldCache = cPath

    # path towards
    abPath = abPath.replace(shared, '')
    cPath = cPath.replace(shared, '')

    # finalized link
    link = '.'

    # find directory movement backwards
    for i in cPath.split('/'):
        # not empty
        if i:
            link += '.'


    # path to object instancing
    link += abPath.replace('/', '.')

    # remove trailing "."
    if link[-1] == '.':
        link = link[:-1]

    return link
