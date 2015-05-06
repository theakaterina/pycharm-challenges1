from test_helper import run_common_tests, failed, passed, get_file_output


def check_answers(answers):
    if answers[0] == str(range(1, 21)):
        passed()
    else:
        failed("Your first answer is incorrect. Did you include 20?")
    if answers[1] == str(range(0, 31, 2)):
        passed()
    else:
        failed("Your second answer is incorrect. Did you include 30? Is it just even numbers?")
    if answers[2] == str(range(99, 0, -1)):
        passed()
    else:
        failed("Your third answer is incorrect. Count from 99 all the way to 1.")


if __name__ == '__main__':
    run_common_tests()
    attempts = get_file_output()
    check_answers(attempts)