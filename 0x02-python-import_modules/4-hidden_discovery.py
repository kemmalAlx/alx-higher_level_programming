#!/usr/bin/python3

if __name__ == "__main__":
    """Program that prints all the names defined by the compiled
    module hidden_4.pyc (please download it locally)."""

    import hidden_4

    lists = dir(hidden_4)

    for my_list in lists:
        if my_list[0:2] != "__":
            print(my_list)
