from dataclasses import dataclass
from typing import Callable

@dataclass
class TreeNode:
  name: str
  size: int
  childrens: list['TreeNode']
  parent: 'TreeNode' = None
  
  def isFolder(self) -> bool:
    return self.childrens
  
  def addChildren(self, treeNode: 'TreeNode'):
    self.size = None
    self.childrens.append(treeNode)
    treeNode.parent = self

def visitTree(t: TreeNode):
    s=t.name + ' '
    if t.isFolder():
        s+='folder '
    else:
        s+='file ' + str(t.size)
    if t.parent:
        s+=' parent = ' + t.parent.name
    print(s)
    for c in t.childrens:
        visitTree(c)

def sizeVisit(t: TreeNode) -> int:
    if t.isFolder():
        sum = 0
        for c in t.childrens:
            sum += sizeVisit(c)
        return sum
    else:
        return t.size

def recurseSubFolders(t: TreeNode) -> list[TreeNode]:
    if t.isFolder():
        l = []
        for c in t.childrens:
            if c.isFolder():
                l.append(c)
                l.extend(recurseSubFolders(c))
        return l
    else:
        return []

def filterVisit(t: TreeNode, cutoff: int, soFar: list[TreeNode]) -> list[TreeNode]:
    if t.isFolder():
        if sizeVisit(t) <= cutoff:
            soFar.append(t)
            soFar.extend(recurseSubFolders(t))
        else:
            for c in t.childrens:
                filterVisit(c, cutoff, soFar)
        return soFar
    else:
        return []

def foldersBiggerVisit(t: TreeNode, cutoff: int, soFar: list[TreeNode]) -> list[TreeNode]:
    if t.isFolder():
        if sizeVisit(t) >= cutoff:
            soFar.append(t)
            for c in t.childrens:
                foldersBiggerVisit(c,cutoff, soFar)
            return soFar
        else:
            return soFar
    else:
        return []


def parseCommand(s: str, currentNode: TreeNode) -> TreeNode:
    if s[:2] == 'cd':
        arg = s[2:].strip()
        if arg == '/':
            while currentNode.parent:
                currentNode = currentNode.parent
            return currentNode
        elif arg == '..':
            currentNode = currentNode.parent
            return currentNode
        else:
            return next(x for x in currentNode.childrens if x.name == arg)
    else:
      return currentNode

def updateCurrentNode(currentNode: TreeNode, line):
    splits = line.split(' ')
    if (splits[0] == 'dir'):
        currentNode.addChildren(TreeNode(splits[1],None,[]))
    else:
        currentNode.addChildren(TreeNode(splits[1],int(splits[0]),[]))
    return currentNode

def parseTree() -> TreeNode:
    with(open('input','r')) as file:
        lines = file.read().splitlines()
        root = TreeNode("/",None,[])
        currentNode = root
        for line in lines:
            if line.startswith('$'):
                currentNode = parseCommand(line[2:], currentNode)
            else:
                currentNode = updateCurrentNode(currentNode, line)
        return root

def problem1():
    root = parseTree()    
    folders = filterVisit(root,100000,[])
    foldersSizes = map(lambda f: sizeVisit(f), folders)
    return sum(foldersSizes)

def problem2():
    root = parseTree()
    totalSpace =  70000000
    neededSpace = 30000000
    usedSpace = sizeVisit(root)
    remainingSpace = totalSpace - usedSpace
    spaceToFree = neededSpace - remainingSpace
    return min(map(lambda t: sizeVisit(t), foldersBiggerVisit(root,spaceToFree,[])))
    

# print(problem1())
print(problem1())
print(problem2())