def assignment_01():
    directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
    management = {'Tine', 'Trunte', 'Rane'}
    employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent',
                 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

    director_not_employee = directors.difference(employees)

    director_and_employee = directors.intersection(employees)

    mangement_and_director = management.intersection(directors)

    mangement_and_employee = management.intersection(employees)

    mangement_and_director = management & directors

    employee_management_director = management & directors & employees

    employees_only = employees - directors - management


def assignment_02():
    dataset = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
    tuples = [(key, value) for key, value in dataset.items()]


def assignment_03():
    s1 = {'a', 'e', 'i', 'o', 'u', 'y'}
    s2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

    union = s1.union(s2)

    symmetric_difference = s1.symmetric_difference(s2)
    difference = s1.difference(s2)

    # get unique values from both sets and combine them into a disjointed set
    temp1 = s1.difference(s2)
    temp2 = s2.difference(s1)
    disjoint = temp1.union(temp2)


def assignment_04():
    date = date_formatter('8-MAR-85')
    print(date)


def date_formatter(str):
    months = {'JAN': 1,
              'FEB': 2,
              'MAR': 3,
              'APR': 4,
              'MAT': 5,
              'JUN': 6,
              'JUL': 7,
              'AUG': 8,
              'SEP': 9,
              'OCT': 10,
              'NOV': 11,
              'DEC': 12}
    space_indexes = [(i) for i in range(len(str)) if str[i] == '-']

    day = str[0:space_indexes[0]]
    month = str[space_indexes[0] + 1:space_indexes[1]]
    year = str[space_indexes[1]+1:]

    month = months.get(month)
    if int(year) >= 23:
        year = '19' + year
    else:
        year = '20' + year

    return (year, month, day)


def main():
    assignment_01()
    assignment_02()
    assignment_03()
    assignment_04()


main()
