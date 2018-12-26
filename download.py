import requests
import os

index = 1

with open('all.txt', 'r') as f:
    for url in f:
        print('Processing {}. image'.format(index))
        print('Downloading {}'.format(url[:-1]))
        try:
            img_name = url.split('/')[-1].strip()
            if os.path.isfile('data/{}'.format(img_name)):
                print('Already downloaded. Skipping')
                index += 1
                continue
        except Exception as e:
            print('Cant extract image name from given URL.')
            print(str(e))
            continue

        path = 'data/{}'.format(img_name)
        with open(path, 'wb') as img:
            try:
                cont = requests.get(url).content
            except Exception as e:
                print('Cant get the content')
                print(str(e))
                continue
            try:
                img.write(cont)
            except Exception as e:
                print('Cant save the downloaded image')
                print(str(e))
        index += 1
