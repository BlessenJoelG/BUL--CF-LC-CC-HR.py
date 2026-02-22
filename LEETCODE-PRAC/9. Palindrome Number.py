class Solution:
  def isPalindrome(self, x: int) -> bool:
    z = 0
    pal = x
    while(x!=0):
        y = x%10
        z = z*10+y
        x = int(x/10)
    if pal == z:
        return True
    else:
        return False