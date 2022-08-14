class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        oper = ['+','-','*','/']
        for item in tokens:
            if item not in oper:
                nums.append(int(item))
            else:
                num2, num1 = nums.pop(), nums.pop()
                #print(num1, item, num2)
                if item == oper[0]:
                    nums.append(num1+num2)
                elif item == oper[1]:
                    nums.append(num1-num2)
                elif item == oper[2]:
                    nums.append(num1*num2)
                else:
                    nums.append(int((num1*1.0)/(num2*1.0)))
                                
        return nums[0]
            
