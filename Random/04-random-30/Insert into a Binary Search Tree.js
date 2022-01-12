/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
 var insertIntoBST = function(root, value) {
    let node = new TreeNode(value);
    if(!root){
        root = node
        return root
    }
    let current = root
    while(current){
        if(value < current.val){
            if(!current.left){
                current.left = node
                return root
            }
            current = current.left
        } else {
            if(!current.right){
                current.right = node
                return root
            }
            current = current.right
        }
    }
    return root
};
