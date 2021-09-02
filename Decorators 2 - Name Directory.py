def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: x[2]))
        #lambda have been used for age constraint
    return inner
