from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":
        passed()
    else:
        failed()


def check_answers(answer):
    if "49 bottles of beer on the wall, 49 bottles of beer. You take one down, pass it around, 48 bottles" in answer[50]:
        passed()
    else:
        failed("Something is wrong with the middle lines")

    if "1 bottle of beer on the wall, 1 bottle of beer. You take it down, pass it around," \
            " go to the store and buy some more!" in answer:
        passed()
    else:
        failed("Your line about the last bottle isn't quite right.")

if __name__ == '__main__':
    run_common_tests()
    attempt = get_file_output()
    check_answers(attempt)