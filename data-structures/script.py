
def main():
    # list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
    # tu = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
    # str = 'Hello World Huston we are here'

    # print(list[1:-1])
    # print(list[:2])
    # print(list[4:])
    # print(list[4:5])
    # print(list[0::2])
    # print(list[-1::-1])
    # print(tu[1::1])
    # print(str[6:25])

    # ex1
    names = ['George', 'Bejamin', 'Thomas', 'John']
    ages = [10, 15, 20, 32, 8, 18, 17, 19]
    filtered = list(filter(fun, names))
    filtered_age = list(filter(check_age, ages))
    print(filtered)
    print(filtered_age)

    # ex2
    print(remove_vowels('aeeetst'))

    # ex3
    new_names = ['Claus', 'Ib', 'Per', 'Kristian']
    print(sorted(new_names))
    print(sorted(new_names, reverse=True))
    print(sorted(new_names, key=len))
    print(sorted(new_names, key=last_letter))
    print(sorted(new_names, key=check_if_contains_a))

    # ex4
    s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
    print(count_char(s))
    print(count_char_exclude(s))
    print(count_words(s))


def fun(x):
    return True if 'e' in x else False


def check_age(i):
    return True if i >= 18 else False


def remove_vowels(str):
    vowels = 'aeiouAEIOU'
    li = []
    for x in str:
        if x not in vowels:
            li.append(x)
    return sorted(li)


def last_letter(x):
    return x[-1]


def check_if_contains_a(x):
    return True if 'a' in x else False


def count_char(x):
    count = 0
    for i in x:
        count += 1
    return count


def count_char_exclude(x):
    count = 0
    for i in x:
        if ' ' not in i:
            count += 1
    return count


def count_words(x):
    count = 0
    for i in x:
        if ' ' in i:
            count += 1
    return count


main()
