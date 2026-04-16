def most_common_char(text: str) -> str:
    a_lot = text[0]
    for char in text:
        if text.count(char) > text.count(a_lot):
            a_lot = char
        return char

text = "hello world"
result = most_common_char(text)
print(result)