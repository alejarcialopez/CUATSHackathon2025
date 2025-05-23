20/03/205

This is the first Hackathon I have attended. The first five hours are workshops introducing you to common data structures and algorithms together with practice problems. 
At midnight, problems are released. These consist of Leetcode medium/hard questions.

Important concepts:
  Hashmaps:
  Hashmaps have access, insert, and delete complecity of O(1)

  Kadane's algorithm: return max consecutive sum of elements in an array
    maxSum = nums[0]
    curSum = 0
    for n in nums:
      curSum = max(curSum,0)
      curSum += n
      maxSum= max(maxSum, curSum)
    return maxSum

  Two pointers: 
  Have a L (left) and R (right) pointer, both starting at some indices of the array, with L being the leftmost one and R the rightmost one. L is incremented and R is decremented, sometimes one at a time, other times both at the same time. This continues until the pointers meet each other.
  An important example is binary search (log n).
    L = start, R = end
    while L <= R 
      M = (L+R) // 2
      if target > arr[M]
        L = M + 1
      else if target < arr[M]
        R = M - 1
      else
        return M
    return does not exist
  
  Linked list: consists of nodes that have a value and pointers to one or more nodes, usually a previous and next node. The upside of linked lists is that they have insert and delete complexities of O(1) (if the reference to the node exists)

  Binary trees: Like a linked list. Each node has a left and right child pointer and a value. Properties:
    Root node: no parent
    Leaf node: no children
    Height of a tree: root node to lowest leaf node
    Depth of a node: distance to root (root has depth 1)
    Balanced tree: a tree is balanced if |height of left tree - height of right tree | <= 1




    Search in a sorted tree (Left child is smaller than parent, Right child is bigger than parent):
      def search(root, target):
        if not root:
          return false
        if target > root.val:
          return search(root.right, target)
        else if target < root.val:
          return search(root.left, target)
        else:
          return true 
        
      Depth First Search: commonly used to traverse trees. Always go left first then look at value. Go as deep as possible before backtracking.
        def inorder(root):
          if not root:
            return
          inorder(root.left)
          print(root.val)
          inorder(root.right)
        
        def preorder(root):
          if not root:
            return
          print(root.val)
          preorder(root.left)
          preorder(root.right)

        def postorder
 
      Breadth First Search: visit nodes on one level before moving to the next.




Problems:

01 / 01: TwoSum
  Problem: Given an array of numbers, output two distinct indices for which their respective elements add up to a target integer.
  Key idea: loop through the elements and use a hashmap to "remember" already seen numbers so that they can be accessed in O(1) if needed.

02 / 704: Binary search
  Use two pointers.

03 / 206: Reverse linked list
