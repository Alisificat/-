import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2] # т.к нужен индекс делим с получением int
    return sum(abs(x - median) for x in nums)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python min_moves.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        nums = [int(line.strip()) for line in f]

    print(min_moves(nums))