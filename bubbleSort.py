class BubbleSorter:
    def __init__(self, data):
        self.list = data

    def display(self):
        print(f"Current data: {self.list}")

    def sort(self):
        n = len(self.list)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                    swapped = True
            print(f"After round {i + 1}: {self.list}")
            if not swapped:
                break

if __name__ == '__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    sorter.display()

    sorter.sort()

    print("After sorting:")
    sorter.display()

