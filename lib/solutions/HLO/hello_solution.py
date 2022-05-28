

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """
    Says hello to a friend

    friend_name: A string showing a name
    """
    if type(friend_name) != str:
        raise TypeEror("friend_name should be a string")

    return("Hello, " + friend_name + "!")




