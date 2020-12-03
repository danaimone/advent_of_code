import csv


class Password:
    def __init__(self, letter, at_least_times, at_most_times, password):
        self.letter = letter
        self.at_least_times = at_least_times
        self.at_most_times = at_most_times
        self.password = password

    def print_rule(self):
        print(f"Letter: {self.letter}")
        print(f"Appears at least {self.at_least_times} times")
        print(f"Appears at least {self.at_most_times} times")
        print(f"Password: {self.password}")

    def check_if_valid_pass_interpreted(self):
        character_count = self.password.count(self.letter)
        return self.at_least_times <= character_count <= self.at_most_times

    def check_if_valid_pass_actual(self):
        first_position_index = int(self.at_least_times - 1)
        second_position_index = int(self.at_most_times - 1)

        first_position = self.password.find(self.letter, first_position_index)
        second_position = self.password.find(self.letter, second_position_index)

        in_first_position = bool(first_position == first_position_index)
        in_second_position = bool(second_position == second_position_index)

        return in_first_position ^ in_second_position


def password_policy(file_name, delimiter):
    """
    Given a file of passwords separated by spaces, return the amount of passwords that follow
    their given rule.
    :return: The amount of valid passwords, according to a given rule defined in the file.
    """
    password_reader = csv.reader(open(file_name), delimiter=delimiter)
    count = 0
    for line in password_reader:
        letter, rule, password = line[1].split(":")[0], line[0].split("-"), line[2]
        at_least = int(rule[0])
        at_most = int(rule[1])
        password = Password(letter, at_least, at_most, password)
        if password.check_if_valid_pass_actual():
            count += 1

    return count


if __name__ == "__main__":
    print(password_policy("Day 2/passwords", " "))
