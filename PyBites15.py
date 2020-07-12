names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    count = 1
    for i in range(len(names)):
        spacecount = ' ' * (11-len(names[i]))
        print('{}. {}{}{}'.format(count,names[i],spacecount,countries[i]))
        count += 1

enumerate_names_countries()
