from test_helper import run_common_tests, failed, passed, get_file_output


def check_answers(answers):
    if answers[0] == "362880":
        passed()
    else:
        failed("Oh no! That's not 9 factorial.")


if __name__ == '__main__':
    run_common_tests()
    attempt = get_file_output()
    check_answers(attempt)

