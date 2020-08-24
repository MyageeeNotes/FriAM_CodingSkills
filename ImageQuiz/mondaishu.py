class Mondaishu:
    def __init__(self, data):
        self.file_data = data
        self.data = []
        self.now = -1

    def next(self):
        self.now += 1
        if self.now < len(self.file_data):
            self.data = self.file_data[self.now].split(',')
        else:
            self.now -= 1
            self.data = self.file_data[self.now].split(',')
            print("最後の問題まで答えました！")
