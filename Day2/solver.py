def read_reports():
    reports = []
    with open('input.txt') as file:
        for line in file:
            report = line.split(' ')
            report = list(map(int,report))
            reports.append(report)
    return reports

def is_safe(report:list):
    increasing, decreasing = False, False

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff > 3 or diff == 0:
            return False
        if report[i] < report[i + 1]:
            increasing = True
        else:
            decreasing = True
    if increasing and decreasing:
        return False
    return True


def main():
    reports = read_reports()
    n_safe = 0
    n_safe_with_dampener = 0
    for report in reports:
        if is_safe(report):
            n_safe += 1
            n_safe_with_dampener += 1
        else:
            #sorry for brute force, was late on time
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if is_safe(new_report):
                    n_safe_with_dampener += 1
                    break

    print('Task 1:',n_safe)
    print('Task 2:',n_safe_with_dampener)

main()
