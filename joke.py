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


def get_joke_with_exception() -> str:

    url = 'https://api.chucknorris.io/jokes/random'

    # print()
    # print(type(requests.exceptions.Timeout))
    # print()

    try: 

        response = requests.get(url, timeout=30)

        response.raise_for_status()

    except requests.exceptions.Timeout:

        return 'no joke'

    # except requests.exceptions.ConnectionError:
    #     pass    

    except requests.exceptions.HTTPError:
        return 'HTTPError was raised'     

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'no joke'

    return joke     


# if __name__ == '__main__':
#     print(get_joke())            