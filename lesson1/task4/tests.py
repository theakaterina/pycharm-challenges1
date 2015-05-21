from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[1]
    if "elif bikes < people:" in placeholder:
        passed()
    elif "elif people > bikes:" in placeholder:
        passed()
    elif "elif bikes > people:" in placeholder:
        passed()
    elif "elif people > bikes:" in placeholder:
        passed()
    else:
        failed("You have to use the elif statement, and make sure your spaces are in the right places.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()