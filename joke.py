import requests # pip install requests


def len_joke() -> int:
    joke = get_joke()

    print()

    print('The joke from get_joke():', joke)

    print()

    return len(joke)



def get_joke() -> str:

    url = 'https://api.chucknorris.io/jokes/random'

    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'no joke'

    return joke 


if __name__ == '__main__':
    print(get_joke())            