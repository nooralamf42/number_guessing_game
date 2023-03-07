from random import randint as randomnummber
from flask import Flask

app = Flask(__name__)

styleBegin = "<body style='text-align:center; font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif; " \
             "padding:50px 0;'>"
styleEnd = "</body>"


@app.route("/")
def homepage():
    return f"{styleBegin}<h1>Guess a number</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
           f"<p>Enter your guess number in the url.</p>{styleEnd}"


right_number = randomnummber(1, 10)
print(right_number)


@app.route(f"/<guessed_number>")
def is_true(guessed_number):
    if int(guessed_number) == right_number:
        return f"{styleBegin}<h1 style='color:green'>You found me</h1>" \
               f"<img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif'> {styleEnd}"
    elif int(guessed_number) > right_number:
        return f"{styleBegin}<h1 style='color:red'>Guessed number is too high!</h1>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2VkYjc0Mjk4NGQwY2IzYWViMDQ1N" \
               f"2UwOTdmMTA3ZjMzM2ZkNmQzOCZjdD1n/w3J7mstYCISqs/giphy.gif'>{styleEnd}"

    elif int(guessed_number) < right_number:
        return f"{styleBegin}<h1 style='color:blue'>Guessed number is too low</h1>" \
               f"<img src='https://media.giphy.com/media/H2GT0TQBAlbuo/giphy.gif'>{styleEnd}"


if __name__ == "__main__":
    print("running")
    app.run(debug=True)
