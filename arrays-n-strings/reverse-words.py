def reverseChars(message, left_index, right_index):
   # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1


def reverseWords(words):
    reverseChars(words, 0, len(words) - 1)
    i = 0
    for j in range(len(words)):
        if j == len(words) or j == ' ':
            reverseChars(words, i, j - 1)
        i = j + 1


words = ['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
         'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd']

reverseWords(words)

print(words)
