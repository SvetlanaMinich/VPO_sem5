def task2():
    people = []
    while True:
        name = input('Enter name or <Enter> for end: ')
        if name == '':
            break
        surname = input('Enter surname: ')
        age = input('Enter age: ')
        people.append({'name': name,
                       'surname': surname,
                       'age': int(age)})
    for person in people:
        print(person['surname'], person['name'], person['age'])
    ages = [i['age'] for i in people]
    min_age, max_age, avr_age = min(ages), max(ages), round(sum(ages)/len(ages),2)
    print(min_age, max_age, avr_age)

task2()