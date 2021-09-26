import csv


def read_csv(file_path):
    """
    Function reads csv-file and returns file contents as a list of dictionaries
    :param file_path: str - csv-file name
    :return: list - file contents as a list of dictionaries
    """
    lst = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")

        for row in reader:
            lst.append(row)
    return lst


def write_csv(file_path, lst, field_names):
    """
    Function writes data in csv-file
    :param file_path: str - csv-file name
    :param lst: list - a list of dictionaries with data
    :param field_names: list - a list with field names of csv-file
    :return: None
    """
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=field_names)
        writer.writeheader()
        for row in lst:
            writer.writerow(row)


def sort_by_age(lst):
    """
    Function sorts list of dictionaries with data and returns list
    :param lst: list - list of dictionaries with data
    :return: list
    """
    sort_age_students = sorted(lst, key=lambda item: int(item['age']), reverse=True)
    return sort_age_students


def get_top_performers(file_path, number_of_top_students=5):
    """
    Function gets top of students from file and returns list
    :param file_path: str - csv-file name
    :param number_of_top_students: int - count of top students
    :return: list
    """
    lst = read_csv(file_path)
    sort_top_students = sorted(lst, key=lambda item: float(item['average mark']), reverse=True)[:number_of_top_students]
    students_names = [i['student name'] for i in sort_top_students]
    return students_names


if __name__ == '__main__':
    print(get_top_performers("data/students.csv"))
    fieldnames = ['student name', 'age', 'average mark']
    students_lst = read_csv('data/students.csv')
    write_csv('data/new_students.csv', sort_by_age(students_lst), fieldnames)