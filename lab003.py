import lab_chat

def get_username():
    username = input("Enter your username: ")
    username = username.strip()
    username = username.upper()
    return username





def get_group():
    group = input("What room do you want to join?: ")
    group = group.strip()
    group = group.upper()
    return group




def get_message():
    message = input("What message do you want to send?: ")
    message = message.strip()
    return message



def initialize_chat():
    username = get_username()
    group = get_group()

    node = lab_chat.get_peer_node(username)
    lab_chat.join_group(node, group)

    channel = lab_chat.get_channel(node, group)
    return channel


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")


if __name__ == "__main__":
    start_chat()