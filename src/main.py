def read_input(input_file):
    with open(input_file, "r") as input_file:
        lines = input_file.read().split("\n")
    employees, beer = map(int, lines[0].split())
    beer_preferences = [list(map(lambda x: x == "Y", line)) for line in lines[1:]]
    return employees, beer, beer_preferences


def write_to_file(output_txt, output):
    with open(output_txt, "w") as output_file:
        output_file.write(str(output))


def all_possible_combinations(elements_list, elements_num):
    if elements_num == 0:
        return [[]]
    else:
        combinations = []
        for i in range(len(elements_list)):
            for each_combination in all_possible_combinations(elements_list[i + 1 :], elements_num - 1):
                combinations.append([elements_list[i]] + each_combination)
        return combinations


def exact_algorithm(employees, beer, beer_preferences):
    for b in range(1, beer + 1):
        for combination in all_possible_combinations(range(beer), b):
            if all(
                any(beer_preferences[n][j] for j in combination)
                for n in range(employees)
            ):
                return b
    return beer


def main(input_file, output_file):
    employees, beer, beer_preferences = read_input(input_file)
    min_beers = exact_algorithm(employees, beer, beer_preferences)
    write_to_file(output_file, min_beers)
    return min_beers


# main("input_txt", "output_txt")

# Код, який повністю не відповідав завданню
# Цей код використовував жадібний алгоритм
#
# def greedy_algorithm(num_employees, beer, beer_preferences):
#     beer_needed = set(range(beer))
#     employees = {i: set() for i in range(num_employees)}
#     for i in range(num_employees):
#         for j in range(beer):
#             if beer_preferences[i * beer + j] == "Y":
#                 employees[i].add(j)
#
#     final_employees = set()
#     while beer_needed:
#         best_employee = None
#         beer_covered = set()
#         for employee, beer_for_employee in employees.items():
#             covered = beer_needed & beer_for_employee
#             if len(covered) > len(beer_covered):
#                 best_employee = employee
#                 beer_covered = covered
#
#         beer_needed -= beer_covered
#         final_employees.add(best_employee)
#
#     return len(final_employees)
#
#
# def write_to_file(file, data):
#     with open(file, "w") as output_file:
#         output_file.write(str(data))
#
#
# def read_input(file):
#     with open(file, "r") as input_file:
#         num_employees, beer = map(int, input_file.readline().split())
#         beer_preferences = input_file.readline().strip()
#     return num_employees, beer, beer_preferences
#
#
# if __name__ == "__main__":
#     employees_num, beer_for_party, likes = read_input("input_txt")
#     write_to_file("output_txt", greedy_algorithm(employees_num, beer_for_party, likes))
