"""Script for generating data in backend in urls.txt file for Siege"""

import requests


def get_ids(retry=True):
    r = requests.get('http://127.0.0.1:8000/api/test_app/entries/')
    if r.status_code == 200:
        entries_data = r.json()
        if not entries_data:
            if retry:
                requests.post('http://127.0.0.1:8000/api/test_app/entries/random/')
                return get_ids(retry=False)
            else:
                raise Exception('Unable to generate entries')
        return [entry['id'] for entry in entries_data]
    else:
        raise Exception('Invalid response from server')


def generate(entries_ids):
    with open('urls1.txt', 'w') as f:
        lines = ['BASE_URL=http://127.0.0.1:8000/api/test_app/entries/\n']
        for entry_id in entries_ids:
            lines.append(f'$(BASE_URL){entry_id}/\n')
        f.writelines(lines)

    with open('urls2.txt', 'w') as f:
        f.write('http://127.0.0.1:8000/api/test_app/user_request/ POST')


if __name__ == '__main__':
    generate(get_ids())
