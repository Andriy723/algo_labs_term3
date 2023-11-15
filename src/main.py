def greedy_algorithm(num_employees, beer, beer_preferences):
    beer_needed = set(range(beer))
    employees = {i: set() for i in range(num_employees)}
    for i in range(num_employees):
        for j in range(beer):
            if beer_preferences[i * beer + j] == "Y":
                employees[i].add(j)

    final_employees = set()
    while beer_needed:
        best_employee = None
        beer_covered = set()
        for employee, beer_for_employee in employees.items():
            covered = beer_needed & beer_for_employee
            if len(covered) > len(beer_covered):
                best_employee = employee
                beer_covered = covered

        beer_needed -= beer_covered
        final_employees.add(best_employee)

    return len(final_employees)


def write_to_file(file, data):
    with open(file, "w") as output_file:
        output_file.write(str(data))


def read_input(file):
    with open(file, "r") as input_file:
        num_employees, beer = map(int, input_file.readline().split())
        beer_preferences = input_file.readline().strip()
    return num_employees, beer, beer_preferences


# if __name__ == "__main__":
#     employees_num, beer_for_party, likes = read_input("input_txt")
#     write_to_file("output_txt", greedy_algorithm(employees_num, beer_for_party, likes))
