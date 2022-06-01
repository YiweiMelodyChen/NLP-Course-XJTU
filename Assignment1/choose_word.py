import io
import re


class Counter:
    def __init__(self, path):
        self.mapping = dict()
        with io.open(path, encoding="utf-8") as f:
            data = f.read()
            words = [s.lower() for s in re.findall("\w+", data)]
        for word in words:
            self.mapping[word] = self.mapping.get(word, 0) + 1

    def most_common(self, m, n):
        assert m > 0, "n should be large than 0"
        return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[m:n]


if __name__ == '__main__':
    output_path = './dataset/enwiki-tiny-choose.txt'
    output_file = open(output_path, 'w', encoding="utf-8")
    most_common = Counter("./dataset/enwiki-tiny.txt").most_common(200, 700)
    for item in most_common:
        print(item)
        output_file.write(item[0] + '\n')
    output_file.close()


