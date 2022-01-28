class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def is_incl(A, B):
    if B is None:
        return True
    if A is None:
        return False
    if A.val != B.val:
        return False
    return is_incl(A.left, B.left) and is_incl(A.right, B.right)


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None:
            return False
        if B is None:
            return False
        return is_incl(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(4)
    t3 = TreeNode(5)

    t1.left = t2
    t1.right = t3

    t4 = TreeNode(1)
    t5 = TreeNode(2)
    t2.left = t4
    t2.right = t5
    A = t1

    B = TreeNode(4)
    B.left = TreeNode(0)

    solution = Solution()

    print(solution.isSubStructure(A, B))
