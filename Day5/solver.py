def load_rules_and_updates() -> tuple[list, list]:
    rules = []
    updates = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            if line and '|' in line:
                rules.append(line.split('|'))
                continue
            if line:
                updates.append(line.split(','))
    return (rules, updates)

def abides_rules(rules:list, update:list) -> bool:
    for i, value in enumerate(update):
        relevant_rules = [rule for rule in rules if rule[1] == value]
        for rule in relevant_rules:
            cant_follow = rule[0]
            if cant_follow in update[i:]:
                return False
    return True

def reorder_update(rules:list, update:list) -> list:
    #swap values violating rules until it matches
    while not abides_rules(rules, update):
        for i, value in enumerate(update):
            relevant_rules = [rule for rule in rules if rule[1] == value]
            cant_follows = [rule[0] for rule in relevant_rules if rule[0] in update[i:]]
            if not cant_follows:
                continue
            cant_follow_index = update.index(cant_follows[0])
            update[i] = cant_follows[0]
            update[cant_follow_index] = value
            break
    return update

def main():
    sum_middle_pages_correctly_ordered = 0
    sum_middle_pages_wrong_ordered = 0
    rules, updates = load_rules_and_updates()
    for update in updates:
        assert len(update) % 2 == 1, "No middle page"
        if abides_rules(rules, update):
            sum_middle_pages_correctly_ordered += int(update[len(update) // 2])
        else:
            update = reorder_update(rules, update)
            sum_middle_pages_wrong_ordered += int(update[len(update) // 2])

    print('Sum of middle pages of correct updates:', sum_middle_pages_correctly_ordered)
    print('Sum of middle pages of reordered updates:', sum_middle_pages_wrong_ordered)

main()
