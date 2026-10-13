class Solution:
    def isSubtree(self, t, s):
        if not s:
            return True
        if not t:
            return False

        if self.sameTree(t, s):
            return True

        return (
            self.isSubtree(t.left, s) or
            self.isSubtree(t.right, s)
        )

    def sameTree(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return (
            self.sameTree(a.left, b.left) and
            self.sameTree(a.right, b.right)
        )