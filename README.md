def chat_task(ctx, pipe, n, group):  # function name is chat_task

def get_peer_node(username): # function name is get_peer_node

def join_group(node, group): # function name is join_group

def get_channel(node, group): # function name is get_channel

n: a peer to peer node that helps set the username

group: the peer to peer group you want to join

poller: UNSURE

items: what the message contains in the peer to peer

pipe: The communication pipeline for messages

message: the message that is being sent in the pipe

cmds:UNSURE

msg_type: Tells the connection who is messaging

peer_username: tells the connection the user's name

intended group: The intended receiver of the message

ctx: This is a ZeroMQ Connection Context

The get_peer_node method returns n, I think that it creates a new pyre peer with the given username and stars the connection.

The join_group method returns nothing it seems to just make the given node join a chat group

The chat_task method returns nothing and seems to run a loop that listens on two sockets

the get_channel method returns whatever zhelper.zthread_fork returns it seems to activate in some way chat_task
