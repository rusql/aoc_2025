def get_safe_position(start_pos: int, instr: str) -> tuple[int, int]:
    if len(instr) < 2:
        raise ValueError("Instruction invalid. Length too short")
    direction = instr[0].upper()
    if direction not in ("L", "R"):
        raise ValueError("Instruction must start with 'L' or 'R'")

    if not instr[1:].strip().isdigit():
        raise ValueError(f"Instruction invalid. Invalid number of turns")
    turns: int = int(instr[1:])
    if turns < 0:
        raise ValueError("Instruction invalid. Invalid number of turns")

    delta = -turns if direction == "L" else turns
    position = start_pos + delta
    position %= 100

    zero_crosses = int(turns/100)

    if start_pos == 0:
        return position, zero_crosses

    if position == 0:
        zero_crosses += 1
    elif delta > 0 and position < start_pos:
        zero_crosses += 1
    elif delta < 0 and position > start_pos:
        zero_crosses += 1
        
    return position, zero_crosses


def get_day01(file_path: str, start_pos: int):
    position = start_pos
    zero_position_count = 0
    zero_cross_count = 0
    cross_count = 0
    with open(file_path, "r") as f:
        for line in f:
            instr = line.strip()
            position, cross_count = get_safe_position(position, instr)
            zero_cross_count += cross_count
            if position == 0:
                zero_position_count += 1
    return zero_position_count, zero_cross_count

p = get_day01("day01_input.txt", 50)
print(f"password = {p}")