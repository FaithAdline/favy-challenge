def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == 'am':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minute:02d}"

def check_positive_numbers(a, b, c):
    positive_count = sum(1 for num in [a, b, c] if num > 0)
    return positive_count == 2

def calculate_consonant_value(word):
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    substrings = [consonant_values[char] for char in word if char in consonant_values]
    return max(substrings, default=0)

if __name__ == "__main__":
    # Test the functions with sample data
    print(convert_to_24_hour_format(8, 30, 'am'))  # Should print '0830'
    print(convert_to_24_hour_format(8, 30, 'pm'))  # Should print '2030'
    print(check_positive_numbers(2, 4, -3))  # Should print True
    print(check_positive_numbers(-4, 6, 8))  # Should print True
    print(calculate_consonant_value("zodiacs"))  # Should print 26
    print(calculate_consonant_value("strength"))  # Should print 57

