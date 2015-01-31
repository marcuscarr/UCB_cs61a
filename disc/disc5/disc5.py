def remove_all(el, lst):
    """Removes all instances of el from lst.
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """

    while el in lst:
        lst.remove(el)


def add_this_many(x, y, lst):
    """ Adds y to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    """

    lst_short = list(lst)
    remove_all(x, lst_short)

    for _ in range(len(lst) - len(lst_short)):
        lst.append(y)


def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> y = reverse(x)
    >>> y
    [1, 5, 4, 2, 3]
    """
    return(lst[::-1])

class Email:
    """Every email object has 3 instance attributes: the message, the
    sender (their name), and the addressee (the destination’s name).
    """
    def __init__(self, msg, sender, addressee):
        self.msg = msg
        self.sender = sender
        self.addressee = addressee

class Postman:
    """Each Postman has an instance attribute clients, which is a
    dictionary that associates client names with client objects.
    """
    def __init__(self):
        self.clients = dict()

    def send(self, email):
        """Take an email and put it in the inbox of the client it is
        addressed to."""
        try:
            self.clients[email.addressee.name].receive(email)
        except KeyError:
            print("%s is not a client of that postman" % email.addressee.name)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it to the
        clients instance attributes.
        """
        assert client_name not in self.clients.keys(), "%s is already in use" % client_name
        assert client not in self.clients.values(), "%s is already registered with this postman" % client.name

        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is used
    for addressing emails to the client), mailman (which is
    used to send emails out to other clients), and inbox (a
    list of all emails the client has received).
    """

    def __init__(self, mailman, name):
        self.inbox = list()
        self.mailman = mailman
        self.name = name
        self.mailman.register_client(self, self.name)

    def compose(self, msg, recipient):
        """Send an email with the given message msg to the given recipient."""
        return Email(msg, self, recipient)

    def receive(self, email):
        self.inbox.append(email)

Bob = Postman()
Charlie = Client(Bob, "Charlie")
Daisy = Client(Bob, "Daisy")
Frank = Postman()
Fred = Client(Frank, "Fred")
c_to_d = Email("Hi Daisy", Charlie, Daisy)
