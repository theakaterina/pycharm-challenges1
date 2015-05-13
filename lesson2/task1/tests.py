from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    placeholders = get_file_output()
    placeholder = placeholders[-1]
    if placeholder == "Congrats, you win!":
        passed()
    else:
        failed("The program should end with us winning")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


