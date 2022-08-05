class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if 0 <= index < len(self):
            return self._data[index]

        raise IndexError

    def in_queue(self, value, key):
        for file in self._data:
            if file[key] == value:
                return True

        return False
