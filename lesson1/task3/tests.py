from test_helper import run_common_tests, failed, passed, get_file_output


def check_answers(answer):
    if answer == ['True True True True True True']:
        passed()
    else:
        failed("Something isn't True!")


if __name__ == '__main__':
    run_common_tests()
    attempt = get_file_output()
    check_answers(attempt)

