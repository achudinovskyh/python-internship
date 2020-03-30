from functools import reduce


class NumberHolder:
    def __init__(self, number):
        print('NumberHolder created with number:', number)
        self.number = number

    def __del__(self):
        print('NumberHolder with number:', self.number, 'deleted.')

    def is_divisible_by(self, divisor):
        return self.number % divisor == 0

    def multiply_by(self, multiplicator):
        return self.number * multiplicator


class Multiplicator:
    @staticmethod
    def static_action(first, second):
        return (lambda a, b : a * b)(first, second)


class NumberHolderChild(NumberHolder):
    _protected_number = 10

    def __init__(self, number):
        super().__init__(number)

    def __is_string(self):
        return isinstance(self.number, str)


class NumberHolderGrandChild(NumberHolderChild):
    def __init__(self, number):
        super().__init__(number)

    @staticmethod
    def static_action(first, second):
        temp = first * second
        while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first

        lcm = temp // (first + second)
        gcf = int(temp / lcm)
        return lcm, gcf


if __name__ == "__main__":
    # 1st task
    five_holder = NumberHolder(5)
    ten_holder = NumberHolder(10)
    print('Checking is 5 divisible by 2:', five_holder.is_divisible_by(2))
    print('Checking is 10 divisible by 2:', ten_holder.is_divisible_by(2))

    print('Multiply 10 by 2:', ten_holder.multiply_by(2))

    print('Multiply 23 by 12 with static method:', Multiplicator.static_action(23, 12))

    # 2nd task
    seven_holder_child = NumberHolderChild(7)
    print('Checking is 7 string:',  seven_holder_child._NumberHolderChild__is_string())
    print('Checking is 7 divisible by 2 with parent method:', seven_holder_child.is_divisible_by(2))
    print('Checking protected variable:', seven_holder_child._protected_number)

    # 3rd task
    three_holder_grand_child = NumberHolderGrandChild(3)
    print('LCM and GCF for 23 and 12 with static method:', three_holder_grand_child.static_action(23, 12))

    # 4th task
    # Use map to print the square of each numbers rounded
    # to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    # Fix all three respectively.
    map_result = list(map(lambda x: round(x * x, 2), my_floats))
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 + num2, my_numbers)

    print('map_result:', map_result)
    print('filter_result result:', filter_result)
    print('reduce_result', reduce_result)
