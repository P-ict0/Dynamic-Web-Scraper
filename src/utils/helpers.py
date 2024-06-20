def prompt_yes_no(question, enter_is_yes=True):
    """
    Prompt the user with a yes/no question and return True for 'yes' and False for 'no'.
    Continue prompting until a valid response is given.

    :param question: Question to ask the user
    :param enter_is_yes: Whether pressing 'Enter' should be counted as 'yes'

    :return: True for 'yes' and False for 'no'
    """
    valid_responses = {"y": True, "n": False, "": enter_is_yes}

    while True:
        options = "Y/n" if enter_is_yes else "y/N"
        response = input(f"{question} {options}: ").strip().lower()
        if response in valid_responses:
            return valid_responses[response]
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
