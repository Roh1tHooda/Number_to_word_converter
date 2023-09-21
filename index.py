def number_to_words(number):
    # Define lists for words representing numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def recursive_convert(number):
        if number == 0:
            return ""
        elif number < 10:
            return ones[number]
        elif number < 20:
            return teens[number - 10]
        elif number < 100:
            return tens[number // 10] + " " + recursive_convert(number % 10)
        else:
            return ones[number // 100] + " hundred " + recursive_convert(number % 100)

    if number == 0:
        return "zero"
    
    words = ""
    for i in range(len(thousands)):
        if number % 1000 != 0:
            words = recursive_convert(number % 1000) + " " + thousands[i] + " " + words
        number //= 1000

    return words.strip()

# Input a number and convert it to words
try:
    number = int(input("Enter a number (0 to 999,999,999): "))
    if 0 <= number <= 999999999:
        words = number_to_words(number)
        print(f"{number} in words: {words}")
    else:
        print("Number out of range.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
