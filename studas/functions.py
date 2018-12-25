
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

def whisper(text):
    return text.lower() + "..."

greet(whisper)

print(list(map(whisper, ["hello", "HELLO!", "Hi"])))
