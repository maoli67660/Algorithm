# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # print("preorder = ", preorder)
        # print("inorder = ", inorder)

        root_value = preorder[0]
        tree = TreeNode(root_value)
        root_index_inorder = inorder.index(root_value)

        # print('root_index_inorder = ', root_index_inorder)

        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]
        left_preorder = preorder[1:len(left_inorder)]
        right_preorder = preorder[1 + len(right_inorder):]

        print('@  left_inorder', left_inorder)
        print('@  left_preorder', left_preorder)
        tree.left = self.buildTree(left_inorder, left_preorder)

        #tree.right = self.buildTree(right_inorder, right_preorder)

        return tree


if __name__ == '__main__':
    solution = Solution()
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    tree = solution.buildTree(preorder, inorder)

    print(tree.val)
    print(tree.left.val, '  ', tree.right.val)


