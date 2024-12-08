from dataclasses import dataclass

@dataclass
class Equation:
    result: int
    arguments: list[int]

def read_equations() -> list[Equation]:
    equations = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            line = line.split(':')
            equation = Equation(int(line[0]), [int(v) for v in line[1].strip().split(' ')])
            equations.append(equation)
    return equations

def partial_eval(equation:Equation, operators:list) -> int:
    assert len(operators) <= len(equation.arguments) - 1, "To many operators"
    result = equation.arguments[0]
    for i,operator in enumerate(operators):
        match operator:
            case '+':
                result += equation.arguments[1 + i]
            case '*':
                result *= equation.arguments[1 + i]
            case '||':
                result = int(str(result) + (str(equation.arguments[1 + i])))
    return result

def solve_equation(equation:Equation, operators=[]):
    result = partial_eval(equation, operators)
    if result > equation.result or (len(operators) == len(equation.arguments) - 1 and result < equation.result):
        return None

    if result == equation.result and len(operators) == len(equation.arguments) - 1:
        return operators

    if (correct_operators := solve_equation(equation, operators + ['*'])):
        return correct_operators
    elif (correct_operators := solve_equation(equation, operators + ['||'])):
        return correct_operators
    return solve_equation(equation, operators + ['+'])


def main():
    equations = read_equations()
    total = 0
    for equation in equations:
        if result := solve_equation(equation):
            print(f"Solved {equation} - {result}")
            total += equation.result
    print(f"Total: {total}")

main()
