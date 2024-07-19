import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1 = 0
PART_2 = 0

def mirage_maintenance(data):
    global PART_1, PART_2
    for line in data:
        nums = [int(num) for num in line.split()]
        diff = [nums[-1]]
        part_one_first_values = [nums[0]]

        while True:
            seq = []
            for i in range(1, len(nums)):
                seq.append(nums[i] - nums[i-1])

            diff.insert(0, seq[-1])
            part_one_first_values.insert(0, seq[0])

            if all(num == 0 for num in seq):
                PART_1 += extrapolate(diff)
                PART_2 += extrapolate(part_one_first_values, True)
                break

            nums = seq
    return PART_1
            

def extrapolate(nums, part_2 = False):
    extra = [0]
    if part_2:
        for num in nums:
            extra.append(num - extra[-1])
        return extra[-1]
    else:
        for num in nums:
            extra.append(extra[-1] + num)
        return extra[-1]


mirage_maintenance(PUZZLE)
print(f"Solution for part 1 is: {PART_1}")
print(f"Solution for part 2 is: {PART_2}")