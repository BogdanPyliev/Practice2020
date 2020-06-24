def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))
