"""#Decorator to print a border around output.
def border(func):
    def wrapped():
        print("=========")
        func()
        print("=========")
    return wrapped

@border
def greet():
    print("Hello, world!")

greet()"""

"""#Decorator that prints a welcome message.
def welcome(func):
    def run():
        print("Welcome!")
        func()
    return run

@welcome
def start():
    print("Program started")

start()"""

"""#Decorator that converts result to lowercase.
def lower(func):
    def run():
        return func().lower()
    return run

@lower
def get_text():
    return "HELLO PYTHON"

print(get_text())"""

"""#Decorator that repeats function 2 times.
def repeat(func):
    def run():
        func()
        func()
    return run

@repeat
def greet():
    print("Hi")

greet()"""

"""#Decorator to show function has finished.
def finish(func):
    def run():
        func()
        print("Finished!")
    return run

@finish
def task():
    print("Doing task")

task()"""

#Decorator that prints length of the returned string.
def length(func):
    def run():
        text = func()
        print("Length:", len(text))
        return text
    return run

@length
def message():
    return "Hello World"

message()







