import random
from collections import Counter

def generate_random_numbers(n):
    return [random.randint(100, 999) for _ in range(n)]

def classify_number(number):
    digits = [int(digit) for digit in str(number)]
    unique_digits = len(set(digits))
    if unique_digits == 1:
        return "AAA"
    elif unique_digits == 2:
        return "AAB"
    elif unique_digits == 3:
        return "ABC"
    else:
        raise ValueError("Invalid number of unique digits")

def poker_test(numbers):
    classifications = [classify_number(number) for number in numbers]
    counts = Counter(classifications)
    return counts

def print_poker_test_results(counts, n):
    print("Classification | Count | Expected | Chi-Square")
    print("---------------------------------------------")
    expected_counts = {
        "AAA": n * 1 / 1000,  # Only 1 way out of 1000
        "AAB": n * 9 / 1000,  # 9 ways out of 1000
        "ABC": n * 720 / 1000,  # 720 ways out of 1000
    }
    chi_square = 0
    for classification, count in counts.items():
        expected_count = expected_counts[classification]
        chi_square_component = (count - expected_count) ** 2 / expected_count
        chi_square += chi_square_component
        print(f"{classification:14} | {count:5} | {expected_count:8.2f} | {chi_square_component:10.4f}")
    print("---------------------------------------------")
    print(f"Total Chi-Square Value: {chi_square:.4f}")

if __name__ == "__main__":
    n = 1000  # Number of random numbers to generate
    random_numbers = generate_random_numbers(n)
    counts = poker_test(random_numbers)
    print_poker_test_results(counts, n)