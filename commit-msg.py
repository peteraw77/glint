#!/usr/bin/python
import sys
import xmlrpc.client

# server address
server_url = 'http://localhost:8000'

def get_commit_msg():
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg

def main():
    msg = get_commit_msg()
    header = msg.split('\n')[0]

    # check for capitalization
    if header[0] == header[0].lower():
        print('Commit title must start with a capital letter')
        sys.exit(1)

    # check for punctuation
    if header[-1] in {'.','!','?'}:
        print('Trailing punctuation is not permitted')
        sys.exit(1)

    # check for length
    if len(header) > 50:
        print('Commit title must be less than 50 characters')
        sys.exit(1)
    if len(msg) > 124:
        # length is including the \n character
        print('Commit body must be 72 characters or less')
        sys.exit(1)

    # check tense
    with xmlrpc.client.ServerProxy(server_url) as proxy:
        if not proxy.is_imperative(header):
            print('Commit title must be in imperative tense.')
            sys.exit(1)
        else:
            sys.exit(0)

if __name__ == '__main__':
    main()
