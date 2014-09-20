import sys


def read_env():
    def no_env():
        print "[WARNING] No environment is found, defaulting to 'development'"
        return 'development'

    args = sys.argv
    if len(args) == 1:
        return no_env()

    if sys.argv[1] == 'development' or sys.argv[1] == 'dev' or sys.argv[1] == 'debug':
        return 'development'

    if sys.argv[1] == 'staging' or sys.argv[1] == 'stage':
        return 'staging'

    if sys.argv[1] == 'production' or sys.argv[1] == 'prod':
        return 'production'

    return no_env()
