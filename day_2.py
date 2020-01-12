def main():
    file = open("day-2-input.txt", "r")
    program_file = file.read().strip().split(",")
    part_1_answer = get_int_code(program_file,46,59)
    print(part_1_answer)
    print(get_part_2_answer(program_file, 19690720))

def get_int_code(program_file, swap_a, swap_b):
    memory = [int(x) for x in program_file]
    memory[1] = swap_a
    memory[2] = swap_b
    operation_end = 4
    while operation_end <= len(memory):
        operation = memory[operation_end-4:operation_end]
        if operation[0] == 1: memory[operation[3]] = memory[operation[1]] + memory[operation[2]]
        elif operation[0] == 2: memory[operation[3]] = memory[operation[1]] * memory[operation[2]]
        elif operation[0] == 99: break
        operation_end += 4
    return memory[0]

def get_part_2_answer(program_file, target_score):
    noun = 0
    verb = 0
    output = get_int_code(program_file,noun,verb) 
    while output != target_score and verb <= 99:
        if noun == 99:
            noun = 0
            verb += 1
        else: 
            noun += 1
        output = get_int_code(program_file,noun,verb)
    if output == target_score:
        return (noun * 100 + verb)
    else:
        return None

        
