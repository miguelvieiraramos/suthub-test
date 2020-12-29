import requests


def request_data():
    headers = {
        'Content-Type': 'application/json',
        'api_key': 'eb9484921d678843bbfdd6bf460a1df7'
    }
    request = requests.get('https://api.suthubservice.com/v0/sales', headers=headers)
    if request.status_code == 200:
        return request.json()
    return None


def get_dogs(data):
    dogs = {}
    for contract in data['response']:
        for policy in contract.get('policies'):
            for covered_good in policy.get('covered_goods'):
                if covered_good.get('Cão ou gato') == 'Cão':
                    if covered_good.get('Nome') in dogs:
                        dogs[covered_good.get('Nome')] += 1
                    else:
                        dogs[covered_good.get('Nome')] = 1
    return dogs


def write_csv(dogs):
    with open('dogs.csv', 'w') as file:
        file.write('nome_pet;contador\n')
        for name, count in dogs.items():
            file.write(f'{name};{count}\n')


if __name__ == '__main__':
    data = request_data()
    if data:
        dogs = get_dogs(data)
        write_csv(dogs)
        print('dogs.csv was written.')
    else:
        print('It was not possible to complete the execution.')
