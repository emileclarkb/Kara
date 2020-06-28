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
