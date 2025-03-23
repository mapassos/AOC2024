import argparse


class SearchWords():
    DIRECTIONS = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1)
    )


    def __init__(self, tab):
        self.tab = tab
        self.dim = (len(tab), len(tab[0]))

    def searchncount(self, word):
        self.count = 0
        for row in range(self.dim[0]):
            for col in range(self.dim[1]):
                if self.tab[row][col] == word[0]:
                    for dx, dy in self.DIRECTIONS:
                        x = row
                        y = col
                        for i in range(1, len(word)):
                            x += dx
                            y += dy
                            if 0 <= x < self.dim[0] and 0 <= y < self.dim[1]:
                                if self.tab[x][y] == word[i]:
                                    if i == len(word) - 1:
                                        self.count += 1
                                else:
                                    break


        return self.count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default = 'test.txt',
        help = 'Name of the file'
    )

    args = parser.parse_args()

    with open(args.file) as f:
        tab = f.read().split()

    WORD = 'XMAS'

    search = SearchWords(tab)
    print(search.searchncount(WORD))

if __name__ == '__main__':
    main()
