import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]

def mirage_maintenance(data):
    total = 0
    for line in data:
        nums = [int(num) for num in line.split()]
        diff = [nums[-1]]

        while True:
            seq = []
            for i in range(1, len(nums)):
                seq.append(nums[i] - nums[i-1])

            diff.insert(0, seq[-1])

            if all(num == 0 for num in seq):
                total += extrapolate(diff)
                break

            nums = seq
    return total
            

def extrapolate(nums):
    extra = [0]

    for num in nums:
        extra.append(extra[-1] + num)
        
    return extra[-1]



print(f"Solution for part 1 is: {mirage_maintenance(PUZZLE)}")