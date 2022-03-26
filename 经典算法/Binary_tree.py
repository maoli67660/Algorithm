#定义二叉树的结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 从前序和中序建立二叉树
def buildTree_pre_in_order(preorder,inorder):
    if len(inorder) == 0:
        return None
    
    root_val = preorder[0]
    inorder_root_index = inorder.index(root_val)
    left_inorder = inorder[:inorder_root_index]
    right_inorder = inorder[inorder_root_index+1:]
    
    left_preorder = preorder[1:inorder_root_index+1]
    right_preorder = preorder[inorder_root_index+1:]
    root = TreeNode(root_val)
    root.left = buildTree_pre_in_order(left_preorder, left_inorder)
    root.right = buildTree_pre_in_order(right_preorder, right_inorder)
    return root
    
    
   
# 从中序和后序建立二叉树
def buildTree_in_post_order(inorder, postorder):
    if len(postorder) == 0:
        return None
    
    root_val = postorder[-1]
    inorder_root_index = inorder.index(root_val)
    
    left_inorder = inorder[:inorder_root_index]
    right_inorder = inorder[inorder_root_index+1:]
    
    left_postorder = postorder[:inorder_root_index]
    right_postorder = postorder[inorder_root_index:-1]
    
    root = TreeNode(root_val)
    root.left = buildTree_in_post_order(left_inorder, left_postorder)
    root.right = buildTree_in_post_order(right_inorder, right_postorder)
    return root




# 前中后序遍历方法

def preorder_visit(r):
    if r:
        print(r.val, end=' ')
        preorder_visit(r.left)
        preorder_visit(r.right)
        
def inorder_visit(r):
    if r:
        inorder_visit(r.left)
        print(r.val, end=' ')
        inorder_visit(r.right)
        
def postorder_visit(r):
    if r:
        postorder_visit(r.left)
        postorder_visit(r.right)
        print(r.val, end=' ')

# Test case
#     3
#    / \
#   9  20
#     /  \
#    15   7
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
