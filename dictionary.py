class HashTable:
    def __init__(self):
        table_size = 10
        self.table_size = table_size
        self.data_list = [[] for _ in range(table_size)]

    def _get_index(self, key):
        key_hash = hash(key)
        key_index = key_hash % self.table_size
        return key_index

    def _find_in_parent(self, parent_list, key):
        for index in range(len(parent_list)):
            node = parent_list[index]
            [i_key, i_value] = node
            if i_key == key:
                return [index, i_value]
        return None

    def insert(self, key, value):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)

        if find_result is None:
            parent_list.append([key, value])
        else:
            [index, _] = find_result
            parent_list[index] = [key, value]
    
    def remove(self, key):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)

        if find_result is not None:
            [index, _] = find_result
            parent_list.pop(index)
    
    def get(self, key):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)
        if find_result is None:
            return 'Not found'
        [_,value] = find_result
        return value

    def check_exist(self, key):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)
        if find_result is None:
            return False
        return True

ht = HashTable()

#Choice 1: Load the data from the file
def loadData():
    with open('words.txt', encoding='utf-8') as f:
        words_lst = f.read().splitlines()

    words_key = []
    words_value = []
    for i in range(len(words_lst)):
        words_key.append(words_lst[i].split(':')[0].lower())
        words_value.append(words_lst[i].split(':')[1])

        ht.insert(words_key[i],words_value[i])
    print(ht.data_list)

#Choice 2: Insert a new word
def addNewWords():
    new_word = input('Enter a new word: ')
    if ht.check_exist(new_word) == True:   #check existing
        print('This word has been exist, please choose another word!')
        return menu()
    else:
        meaning = input('Translate to Vietnamese: ')
        ht.insert(new_word, meaning)    #add new employee info to ht
        with open('words.txt','a', encoding='utf-8') as f:
            f.write(new_word+': '+meaning+'\n')   
        return print('------------------','\n'
                    'New word:',new_word,'\n'
                    'Meaning:',meaning,'\n'
                    )

#Choice 3: Search a word
def searchWord():
    word = input('Enter a word: ')
    return print(ht.get(word))

#Choice 4: Edit a word
def editWord():
    print(ht.data_list[1])
    # input_word = input('Enter a word: ')
    # for word in ht.data_list[0]:
    #     if word == input_word:
    #         print('Old data:', ht.data_list[1])
    #         ht.data_list[1].update(input('Enter the new data: '))

#Choice 5: Delete a word
def deleteWord():
    word = input('Enter a word: ')
    return ht.remove(word)

# Menu
def menu():
    MENU_SHOW = """
+-------------------Menu------------------+
Person Tree:
1. Load the data from the file.
2. Insert a new word.
3. Search a word
4. Edit a word
5. Delete a word
+-----------------------------------------.+
Your selection: """
    OPERATION = [0, loadData, addNewWords, searchWord, editWord,deleteWord]
    while True:
        select = int(input(MENU_SHOW).strip())
        try:
            if select == 0:
                break
            else:
                OPERATION[select]()
        except IndexError:
            print('Please enter an other number')
            continue

while True:
    menu()