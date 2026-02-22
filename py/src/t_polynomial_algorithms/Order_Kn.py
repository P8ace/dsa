"""
If the input string is empty, return an empty list.
Define a result list to hold the output strings. Have it contain just an empty string to start (we need that one element to build on).
Iterate over the input digits. For each of them:

    If the digit is any invalid character, i.e. not found in the provided digit_to_letters dictionary, raise a ValueError to abort the function:
        raise ValueError(f"invalid digit: {digit}")

    Get the string of letters that can be represented by the current digit, from digit_to_letters.
    Define a new_result list – empty to start with.
    Enter two more nested for loops. For each existing letter combo in result, then for each letter in the current digit's letters:
        Append to the new_result list the concatenation of the existing combo plus the new letter.
    Outside of the two nested loops, but still inside the main loop over digits, set result equal to the new_result.

After the main loop, return the result.
"""


def letter_combinations(digits):
    if digits == "":
        return []
    result = [
        "",
    ]
    for digit in digits:
        if digit not in digit_to_letters.keys():
            raise ValueError(f"invalid digit: {digit}")
        letters = digit_to_letters[digit]
        new_result = []
        for combo in result:
            for letter in letters:
                new_result.append(combo + letter)
        result = new_result
        print(result)
    return result


# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
