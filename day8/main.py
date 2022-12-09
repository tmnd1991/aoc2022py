from dataclasses import dataclass

@dataclass
class Tree:
  height: int
  def __repr__(self) -> str:
   return str(self.height)

@dataclass
class Woods:
    trees: list[list[Tree]]
    def addTree(self, row: int, tree: Tree) -> 'Woods':
        self.trees = pad_or_truncate(self.trees,row + 1,[])
        self.trees[row].append(tree)


    def buildRowAfterCol(self, row: int, col: int) -> list[Tree]:
        return self.trees[row][col+1:]
    
    def buildRowBeforeCol(self, row: int, col: int) -> list[Tree]:
        x = self.trees[row][:col]
        x.reverse()
        return x
    
    def buildColPrevRow(self, row: int, col: int) -> list[Tree]:
        for i in range(row -1, -1, -1):
            yield self.trees[i][col]
    
    def buildColAfterRow(self, row: int, col: int) -> list[Tree]:
        for i in range(row+1, len(self.trees)):
            yield self.trees[i][col]

    def isVisible(self, row: int, col: int) -> bool:
        h = self.trees[row][col].height
        return all(map(lambda t: t.height < h, self.buildRowBeforeCol(row,col))) or \
        all(map(lambda t: t.height < h, self.buildRowAfterCol(row,col))) or \
        all(map(lambda t: t.height < h, self.buildColAfterRow(row, col))) or \
        all(map(lambda t: t.height < h, self.buildColPrevRow(row, col)))
    
    def viewScore(self, row: int, col: int) -> int:
        h = self.trees[row][col].height
        rowBeforeCol = list(self.buildRowBeforeCol(row, col))
        rowAfterCol = list(self.buildRowAfterCol(row, col))
        colAfterRow = list(self.buildColAfterRow(row, col))
        colBeforeRow = list(self.buildColPrevRow(row, col))
        rowBeforeColLower = list(take_until(rowBeforeCol, lambda x: x.height >= h))
        rowAfterColLower = list(take_until(rowAfterCol, lambda x: x.height >= h))
        colAfterRowLower = list(take_until(colAfterRow, lambda x: x.height >= h))
        colBeforeRowLower = list(take_until(colBeforeRow, lambda x: x.height >= h))

        # print(f"{row}, {col} => {h}")
        # print(f"rowBeforeCol: {rowBeforeCol}")
        # print(f"rowAfterCol: {rowAfterCol}")
        # print(f"colAfterRow: {colAfterRow}")
        # print(f"colBeforeRow: {colBeforeRow}")
        # print(f"rowBeforeColLower: {rowBeforeColLower}")
        # print(f"rowAfterColLower: {rowAfterColLower}")
        # print(f"colAfterRowLower: {colAfterRowLower}")
        # print(f"colBeforeRowLower: {colBeforeRowLower}")
        return (len(rowBeforeColLower) + (0 if rowBeforeCol else 0)) * \
            (len(rowAfterColLower)+ (0 if rowAfterCol else 0)) * \
            (len(colAfterRowLower)+ (0 if colAfterRow else 0)) * \
            (len(colBeforeRowLower)+ (0 if colBeforeRow else 0))

from typing import TypeVar
from typing import Callable
T = TypeVar('T')
def pad_or_truncate(some_list: list[T], target_len: int, default: T) -> list[T]:
    return some_list[:target_len] + [default]*(target_len - len(some_list))

def genlen(gen) -> int:
    sum=0
    for i in gen:
        sum+=1
    return max(1,sum)

def parseWoods() -> Woods:
    woods = Woods([[]])
    with(open('input','r')) as file:
        lines = file.read().splitlines()
        for lineNum, line in enumerate(lines):
            for c in line:
                woods.addTree(lineNum, Tree(int(c)))
    return woods
def problem1():
    woods = parseWoods()
    sum=(len(woods.trees) * 2 + len(woods.trees[0]) * 2) - 4
    for r in range(1, len(woods.trees) -1):
      for c in range(1, len(woods.trees[r]) - 1):
        if woods.isVisible(r,c):
            sum += 1
    print(sum)

def take_until(iterable, condition):
    for item in iterable:
        yield item
        if condition(item):
           return            

def problem2gen(woods: Woods):
    for r in range(0, len(woods.trees)):
      for c in range(0, len(woods.trees[r])):
        vs = woods.viewScore(r,c)
        # print(f"score of {r},{c} is {vs}")
        yield vs

def problem2():
    woods = parseWoods()
    # for r in woods.trees:
        # print(r)
    print(max(problem2gen(woods)))

problem1() # 1814
problem2()