import re


def validate_input(caption, validation_function):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                data_string = input(caption)
                if validation_function(data_string):
                    return func(data_string)
                else:
                    print(f'Try again, {caption}')
        return wrapper
    return decorator


def validate_existence_of_ID(caption, validation_function):
    def decorator(func):
        def wrapper(data_string, iterable_collection):
            while True:
                data_string = input(caption)
                if validation_function(data_string, iterable_collection) and Validator.validate_ID(data_string):
                    return func(data_string, iterable_collection)
                else:
                    print(f'Try again, {caption}')
        return wrapper
    return decorator


class Validator:
    # implement validate name
    @staticmethod
    def validate_ID_of_not_existing_freelancer(ID, iterable_collection):
        if iterable_collection.find_ID(ID) == -1:
            return True
        return False

    @staticmethod
    @validate_existence_of_ID('Enter ID of yet not existing  freelancer: ', validate_ID_of_not_existing_freelancer)
    def get_ID_of_not_existing_freelancer(ID_string, iterable_collection):
        return ID_string


    @staticmethod
    def validate_ID_of_existing_freelancer(ID, iterable_collection):
        if iterable_collection.find_ID(ID) == -1:
            return False
        return True

    @staticmethod
    @validate_existence_of_ID('Enter ID of already existing freelancer: ', validate_ID_of_existing_freelancer)
    def get_ID_of_existing_freelancer(ID_string, iterable_collection):
        return ID_string

    @staticmethod
    def validate_natural_number(some_string):
        if Validator.validate_int(some_string):
            return int(some_string) >= 0
        return False

    @staticmethod
    def validate_float(some_string):
        try:
            float(some_string)
            return True
        except Exception as exc:
            return False

    @staticmethod
    def validate_int(some_string):
        if Validator.validate_float(some_string):
            try:
                int(some_string)
                return True
            except Exception as exc:
                return False
        return False

    @staticmethod
    def validate_boundaries(number, lower_bound, upper_bound):
        return lower_bound <= number <= upper_bound

    @staticmethod
    def validate_string_with_letters_only(string_data):
        return all(letter.isalpha() for letter in string_data)

    @staticmethod
    def validate_capitalized(string_data):
        return string_data == string_data.capitalize()

    @staticmethod
    def validate_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        return bool(re.match(email_pattern, email))

    @staticmethod
    def validate_phone_number(phone_number):
        pattern = r'^(\+?380\d{9}|380\d{9})$'
        return bool(re.match(pattern, phone_number))

    @staticmethod
    def validate_ID(ID):
        if all(Validator.validate_natural_number(digit) for digit in str(ID)):
            return len(ID) == 8
        return False

    @staticmethod
    def validate_salary(salary):
        if Validator.validate_float(salary):
            return Validator.validate_boundaries(float(salary), 0, 100000)
        return False

    @staticmethod
    def validate_availability(availability):
        if Validator.validate_float(availability):
            return Validator.validate_boundaries(float(availability), 0, 72)
        return False

    @staticmethod
    def validate_position(position):
        try:
            user_position = FREELANCER.Position[position]
        except Exception as exc:
            return False
        return True

    @staticmethod
    @validate_input("Enter your ID: ", validate_ID)
    def get_ID(ID_string):
        return ID_string

    @staticmethod
    def validate_name(name):
        # if Validator.validate_string_with_letters_only(name):
            # return Validator.validate_capitalized(name)
        return name

    @staticmethod
    @validate_input("Enter your name: ", validate_name)
    def get_name(name_string):
        return name_string

    @staticmethod
    @validate_input("Enter your email: ", validate_email)
    def get_email(email_string):
        return email_string

    @staticmethod
    @validate_input("Enter your phone number: ", validate_phone_number)
    def get_phone_number(phone_number_string):
        return phone_number_string

    @staticmethod
    @validate_input("Enter your availability: ", validate_availability)
    def get_availability(availability_string):
        return float(availability_string)

    @staticmethod
    @validate_input("Enter your salary: ", validate_salary)
    def get_salary(salary_string):
        return float(salary_string)

    @staticmethod
    @validate_input("Enter your position: ", validate_position)
    def get_position(position_string):
        return position_string

    @staticmethod
    def validate_file_name(file_name):
        try:
            with open(file_name, 'r') as file:
                return True
        except Exception as exc:
            return False

    @staticmethod
    @validate_input('Enter your file: ', validate_file_name)
    def get_file_name(file_name_string):
        return file_name_string

    @staticmethod
    @validate_input('Enter your float: ', validate_float)
    def get_float(float_string):
        return float_string

    @staticmethod
    @validate_input('Enter your int: ', validate_int)
    def get_int(int_string):
        return int_string

    @staticmethod
    @validate_input('Enter your natural number: ', validate_natural_number)
    def get_natural_number(natural_number_string):
        return natural_number_string

    @staticmethod
    def validate_parameter(parameter, parameters=('name', 'surname', 'department', 'salary')):
        if parameter in parameters:
            return True
        return False

    @staticmethod
    @validate_input('Enter your parameter: ', validate_parameter)
    def get_parameter(parameter_string):
        return parameter_string

    @staticmethod
    @validate_input('Enter your value: ', validate_string_with_letters_only)
    def getLetterString(letter_string):
        return letter_string

    @staticmethod
    def validateWorker(name, surname, department, salary):
        errors = {}
        if not Validator.validate_string_with_letters_only(name):
            errors['name'] = 'only letters'
        if not Validator.validate_string_with_letters_only(surname):
            errors['surname'] = 'only letters'
        # have no idea how I can validate department
        if not Validator.validate_float(str(salary)):
            errors['salary'] = 'positive float'

        return errors
