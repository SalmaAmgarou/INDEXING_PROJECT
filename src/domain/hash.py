from typing import List, Union
from src.domain.utils import get_dictionary_key, get_dictionary_element

class Hash:
    def __init__(self, size=23):
        self.size = size
        self.table_size = 0
        self.hash_table: List[Union[None, dict]] = [None] * size

    def hash_function(self, key):
        return key % self.size

    def linear_probing_insert(self, key, element):
        address = self.hash_function(key)
        if self.table_size != self.size:
            while self.hash_table[address] is not None:
                address = (address + 1) % self.size

            self.hash_table[address] = {key: element}
            self.table_size += 1

            return address

        return 'Full List'

    def quadratic_probing_insert(self, key, element):
        address = self.hash_function(key)
        if self.table_size != self.size:
            i = 1
            while self.hash_table[address] is not None:
                address = (address + i*i) % self.size
                i += 1

            self.hash_table[address] = {key: element}
            self.table_size += 1

            return address

        return 'Full List'

    def double_hashing_insert(self, key, element):
        address = self.hash_function(key)
        if self.table_size != self.size:
            i = 1
            while self.hash_table[address] is not None:
                address = (address + i*self.hash_function2(key)) % self.size
                i += 1

            self.hash_table[address] = {key: element}
            self.table_size += 1

            return address

        return 'Full List'

    def delete_element(self, key=None, index=None):
        if key is not None:
            element, index = self.get_element(key)
        if index is not None:
            self.hash_table[index] = None
            element = None
        else:
            return 'Missing Key'

        next_index = (index + 1) % self.size

        while self.hash_table[next_index] is not None:
            if get_dictionary_key(self.hash_table[next_index]) == 'A':
                pass
            elif self.hash_function(get_dictionary_key(self.hash_table[next_index])) == next_index:
                pass
            else:
                self.linear_probing_insert(get_dictionary_key(self.hash_table[next_index]),
                                           get_dictionary_element(self.hash_table[next_index]))
                self.hash_table[next_index] = None
            next_index = (next_index + 1) % self.size

        return element

    def set_position_available(self, key):
        element, index = self.get_element(key)
        if index is not None:
            self.hash_table[index] = {'A': 'Available'}
        else:
            return 'Missing Key'

    def delete_all_available_positions(self):
        for index in range(0, self.size):
            if get_dictionary_key(self.hash_table[index]) == 'A':
                self.delete_element(index=index)

    def get_element(self, key):
        index = self.hash_function(key)
        count = 0
        while self.hash_table[index] is not None:
            if count == self.table_size:
                return 'Missing Key', None
            if get_dictionary_key(self.hash_table[index]) == key:
                return self.hash_table[index][key], index
            index = (index + 1) % self.size
            count += 1

        return 'Missing Key', None

    def print_hash_table(self):
        for i in range(len(self.hash_table)):
            print(i, self.hash_table[i])

    # Helper function for double hashing
    def hash_function2(self, key):
        return 8 - (key % 8)
