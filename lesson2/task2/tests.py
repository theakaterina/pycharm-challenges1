from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    placeholders = get_file_output()
    placeholder = placeholders[0]
    if placeholder == "[1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0]":  # TODO: your condition here
        passed()
    else:
        failed("Make sure your value are all floats. Do not change the odd_integers list")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


