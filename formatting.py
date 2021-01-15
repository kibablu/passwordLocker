def my_print(txt):
    print(txt)


msg_template = """Hello {name},
Thank you for joining {website}. We are very happy
to have you.
"""


def format_msg(my_name="Justin", my_website="cfe.sh"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg


def base_function(
    *args, **kwargs
):  # We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
    # *args (Non Keyword Arguments)
    # **kwargs (Keyword Arguments)
    print(args, kwargs)


def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print(sum)
