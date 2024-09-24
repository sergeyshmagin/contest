from random import choices as ch


class MarsURLEncoder:

    def __init__(self):
        self.str_storage = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        hash_val = ''.join(
            ch([x for x in long_url if x not in [':', '/', '-', '.', '_']], k=6))

        while hash_val not in self.str_storage.keys():
            hash_val = ''.join(
                ch([x for x in long_url if x not in [':', '/', '-', '.', '_']], k=6))
            self.str_storage[hash_val] = long_url

        return 'https://ma.rs/' + hash_val

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.str_storage[short_url[-6:]]


new = MarsURLEncoder()
short_url = new.encode(
    'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
print(short_url)
print(new.decode(short_url))
