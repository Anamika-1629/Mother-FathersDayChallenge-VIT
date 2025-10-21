class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            
            if set_bits in prime_set:
                count += 1
                
        return count

def main():
    print("--- 762. Prime Number of Set Bits (Python) ---")
    
    try:
        left = int(input("Enter the left bound (integer): "))
        right = int(input("Enter the right bound (integer): "))
    except ValueError:
        print("Invalid integer input for bounds.")
        return

    if left > right:
        print("Error: Left bound must be less than or equal to the Right bound.")
        return

    solution = Solution()
    result = solution.countPrimeSetBits(left, right)

    print(f"\nInput: left = {left}, right = {right}")
    print(f"Output (Count of numbers with prime set bits): {result}")

if __name__ == "__main__":
    main()