from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[1]
    if "raw_input(" in placeholder:
        passed()
    else:
        failed("Remember to use raw_input(prompt)")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


