import sys

message  = sys.argv[1]
REVERT   = 'revert'
ROLLBACK = 'rollback'
DEPLOY   = 'deploy'

def main():
    message_array = message.lower().split(' ')

    for word in message_array:
        if word == REVERT or word == ROLLBACK:
            return ROLLBACK

    return DEPLOY

print( main() )
