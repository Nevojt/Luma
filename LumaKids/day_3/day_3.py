hello: str = "Hello"
world: str = "world!"

user: str = input("Enter your username ")
def foo(user:str):
    print(f"{hello} {user}! {world}")

foo(user)