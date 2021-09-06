DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Facundo's Examples from class about high order functions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    # Task 1 --> Create list "all_python_devs" and "all_python_workers" using combination of filter and map
    all_python_devs_filter_map = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_filter_map = list(map(lambda worker: worker["name"], all_python_devs_filter_map))

    all_platzi_worker_filter_map = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_worker_filter_map = list(map(lambda worker: worker["name"], all_platzi_worker_filter_map))

    #Task 2 --> Create list "old_people" and "adults" using list comprehenseions
    old_people_list_comprehension = [worker["name"] for worker in DATA if worker["age"]>70]
    adults_list_comprehension = [worker["name"] for worker in DATA if worker["age"] > 18]

    # i must change the variable (iterable list) to see what is my result for worker
    for worker in adults_list_comprehension:
        print(worker)



if __name__ == '__main__':
    run()






