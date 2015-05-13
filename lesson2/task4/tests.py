from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    not_correct = placeholders[0]
    while_condition = placeholders[1]
    user_input = placeholders[2]
    equals_to = placeholders[3]
    less_than = placeholders[4]
    if not_correct == "True":  # TODO: your condition here
        passed()
    else:
        failed("When we start, should the user be correct or incorrect?")
    if while_condition == "not_correct":
        passed()
    else:
        failed("We want the loop to keep running when what is True?")
    if "raw_input(" in user_input:
        passed()
    else:
        failed("This is where we ask the user to guess the number")
    if "==" in equals_to:
        passed()
    else:
        failed("When does the user win?")
    if "<" in less_than:
        passed()
    else:
        failed("When should we say higher than?")



if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


