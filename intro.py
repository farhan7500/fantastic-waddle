import os
def get_configs():
    return os.environ.get('FANTASTIC_CONFIG')

def get_secrets():
    return os.environ.get('FANTASTIC_PASSWORD')


if __name__ == '__main__':
    print(f'Secrets are {get_secrets()}')
    print(f'Configs are {get_configs()}')

