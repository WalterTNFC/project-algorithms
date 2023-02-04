def is_palindrome_recursive(word, low_index, high_index):
    if len(word) is None:
        return False

    # Falso se o ultimo e primeiro
    # caracteres forem diferentes
    if word[low_index] != word[high_index]:
        return False

    if low_index == high_index or (low_index - high_index) == 1:
        return True

    next_index = low_index + 1
    past_index = high_index - 1

    verify = is_palindrome_recursive(word, next_index, past_index)

    return verify
