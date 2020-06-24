def first_word(text: str) -> str:
    return text.split()[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))