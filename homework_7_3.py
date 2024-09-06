class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r') as file:
                entire_content = file.read().replace('\n', ' ')
                entire_content = entire_content.lower()
                entire_content = entire_content.replace(',', ' ')
                entire_content = entire_content.replace('.', ' ')
                entire_content = entire_content.replace('!', ' ')
                entire_content = entire_content.replace('?', ' ')
                entire_content = entire_content.replace(' - ', ' ')
                entire_content = entire_content.replace('=', ' ')
                entire_content = entire_content.replace(';', ' ')
                entire_content = entire_content.replace(':', ' ')
                entire_content = entire_content.split()
                all_words[i] = entire_content
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        x = 0
        for name, words in self.get_all_words().items():
            position = next((i+1 for i, w in enumerate(words) if w == word), None)
            result[name] = position
        return result


    def count(self, word):
        word = word.lower()
        count_ = {}
        for name, words in self.get_all_words().items():
            x = 0
            for w in words:
                if word == w:
                    x += 1
            count_[name] = x
        return count_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего






