'''
In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is. For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
'''

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    result = []
    for name in names:
        if name.title() not in result:
            result.append(name.title())
    return result


def rev_name_order(names):
    result = []
    for name in names:
        splitname = name.split()
        revname = splitname[::-1]
        result.append(' '.join(revname))
    return result


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    result = []
    names = rev_name_order(names)
    names.sort(reverse=True)
    names = rev_name_order(names)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    shortest_name = names[0]
    names = dedup_and_title_case_names(names)
    for name in names:
        if len(name.split()[0]) < len(shortest_name):
            shortest_name = name.split()[0]
    return shortest_name

