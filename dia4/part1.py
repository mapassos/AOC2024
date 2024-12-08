def main():
    with open(r'test.txt') as f:
        tab = f.read().split()
    word = 'XMAS'
    search = SearchWords(tab)
    count = search.searchncount(word)
    print(count)
    input('---')

class SearchWords():
    def __init__(self, tab):
        self.tab = tab
        self.dim = (len(tab), len(tab[0]))

    def searchncount(self, word):
        self.count = 0
        for row in range(self.dim[0]):
            for col in range(self.dim[1]):
                if self.tab[row][col] == word[0]:
                    self.searcharound(word[1:], row, col)
        return self.count       
                
    def searcharound(self, word, i, j):
        #sides left/right
        if i - 1 >= 0 and self.tab[i - 1][j] == word[0]:    self.searchsides(word[1:], i - 1, j, '(i - 1, j)')
        if i + 1 < self.dim[0] and self.tab[i + 1][j] == word[0]:   self.searchsides(word[1:], i + 1, j, '(i + 1, j)')
        #sides up/down
        if j - 1 >= 0 and self.tab[i][j - 1] == word[0]:    self.searchsides(word[1:], i, j - 1, '(i, j - 1)')
        if j + 1 < self.dim[0] and self.tab[i][j + 1] == word[0]:    self.searchsides(word[1:], i, j + 1, '(i, j + 1)')
        #diags main
        if i - 1 >= 0 and j - 1 >= 0 and self.tab[i - 1][j - 1] == word[0]: self.searchsides(word[1:], i - 1, j - 1, '(i - 1, j - 1)')
        if i + 1 < self.dim[0] and j + 1 < self.dim[1] and self.tab[i + 1][j + 1] == word[0]:   self.searchsides(word[1:], i + 1, j + 1, '(i + 1, j + 1)')
        #diags anti
        if i - 1 >= 0 and j + 1 < self.dim[1] and self.tab[i - 1][j + 1] ==  word[0]:    self.searchsides(word[1:], i - 1, j + 1, '(i - 1, j + 1)')
        if i + 1 < self.dim[0] and j - 1 >= 0 and self.tab[i + 1][j - 1] == word[0]:  self.searchsides(word[1:], i + 1, j - 1, '(i + 1, j - 1)')

    def searchsides(self, word, i, j, nextpos: str):
        pos =  eval(nextpos)
        if len(word) > 0:
            if 0 <= pos[0] < self.dim[0] and 0 <= pos[1] < self.dim[1] and word[0] == self.tab[pos[0]][pos[1]]:
                self.searchsides(word[1:], pos[0], pos[1], nextpos)
        else:
            self.count += 1
            return
        return

if __name__ == '__main__':
    main()
