def build_from_disk_map(map:str):
    disk = []
    file_id = 0
    is_free_space = False
    for value in map:
        if is_free_space:
            disk.extend(['.' for i in range(int(value))])
        else:
            disk.extend([str(file_id) for i in range(int(value))])
            file_id += 1
        is_free_space = not is_free_space
    return disk

def fragment_disk(disk:list):
    for i in range(len(disk)):
        if i >= len(disk):
            break
        if disk[i] != '.':
            continue
        last_element = disk[-1]
        while last_element == '.':
            disk = disk[:-1]
            last_element = disk[-1]
        if i >= len(disk):
            break
        disk[i] = last_element
        disk = disk[:-1]
    return disk

def reorder_disk(disk:list):
    pass

def calculate_result(disk:list):
    result = 0
    for i, v in enumerate(disk):
        if v != '.':
            result += i * int(v)
    return result

def main():
    example_input = '2333133121414131402'

    with open('input.txt') as file:
        input = file.read().strip()

    disk = build_from_disk_map(input)
    fragmented_disk = fragment_disk(disk)
    result = calculate_result(fragmented_disk)
    print(result)

main()
