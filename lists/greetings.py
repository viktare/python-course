friends = ['silvia', 'mirko', 'marco', 'amet', 'mattia', 'massimiliano']


def greet(arr: list[str]):
    for el in arr:
        print(f"Greetings, {el.title()}")

greet(friends)