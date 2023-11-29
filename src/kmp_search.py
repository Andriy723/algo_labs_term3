def kmp_search(needle, haystack):
    pattern_length = len(needle)
    text_len = len(haystack)

    prefix_suffix = [0] * pattern_length
    j = 0

    calculate_prefix_suffix(needle, pattern_length, prefix_suffix)

    i = 0
    indexes = []
    while i < text_len:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == pattern_length:
            indexes.append(i - j)
            # print("Pattern is at index", str(i - j))
            j = prefix_suffix[j - 1]

        elif i < text_len and needle[j] != haystack[i]:
            if j != 0:
                j = prefix_suffix[j - 1]
            else:
                i += 1

    return indexes


def calculate_prefix_suffix(needle, pattern_length, prefix_suffix):
    length = 0
    var = prefix_suffix[0]
    i = 1

    while i < pattern_length:
        if needle[i] == needle[length]:
            length += 1
            prefix_suffix[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_suffix[length - 1]
            else:
                prefix_suffix[i] = 0
                i += 1
