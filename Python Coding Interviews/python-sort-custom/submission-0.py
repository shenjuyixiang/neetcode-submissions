from typing import List


def get_word_lenth(words: str) -> int:
    return len(words)


def sort_words(words: List[str]) -> List[str]:

    words.sort(key=get_word_lenth, reverse= True)
    return words


def get_absolute_value(numbers: int) -> int:
    return abs(numbers)


def sort_numbers(numbers: List[int]) -> List[int]:

    numbers.sort(key=get_absolute_value, reverse= False)
    return numbers


# do not modify below this line
print(
    sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"])
)

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
