from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    answers = get_file_output()
    if answers[0] == str(range(1, 21)):
        passed()
    else:
        failed("answer 1 wrong")
    if answers[1] == str(range(0, 31, 2)):
        passed()
    else:
        failed("answer 2 wrong")
    if answers[2] == str(range(99, 0, -1)):
        passed()
    else:
        failed("answer 3 wrong")



