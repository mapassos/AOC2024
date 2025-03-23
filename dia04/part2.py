import argparse

class SearchWords():
    def __init__(self, tab):
        self.tab = tab
        self.dim = (len(tab), len(tab[0]))

    def searchncount(self):
        self.count = 0
        for row in range(1, self.dim[0] - 1):
            for col in range(1, self.dim[1] - 1):
                if self.tab[row][col] == 'A':
                    self.searchdiag(row, col)
        return self.count                      

    def searchdiag(self, i, j):
        diag_letters = [
            self.tab[pos[0]][pos[1]] for pos in (
                (i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1)
            )
        ]

        main_diag = set(diag_letters[:2])
        anti_diag = set(diag_letters[2:])
        if {'S', 'M'} == main_diag == anti_diag:
            self.count += 1

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

    search = SearchWords(tab)
    print(search.searchncount())


if __name__ == '__main__':
    main()
