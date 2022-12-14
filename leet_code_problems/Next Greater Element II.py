
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new=nums*2
        stack=[]
        res=[-1]*len(new)
        for i in range(len(new)-1,-1,-1):
            while stack and stack[-1]<=new[i]:
                stack.pop()
            if not stack:
                res[i]=-1
            else:
                res[i]=stack[-1]
            stack.append(new[i])
        final=res[:len(nums)]
        return final
        
        
        
        
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        out=[-1]*len(nums)
        #nums2=nums.copy()
        tail=1
        if len(nums)==1: return out
        for i in range(len(nums)): 
         if nums[i] < nums[(i + 1) % len(nums)]:
            out[i] = nums[(i + 1) % len(nums)]
         else :
            tail = (i + 1) % len(nums)
            while tail != i:
               if tail >= len(nums):
                  tail = 0
               if tail == i:
                  break
               if nums[i] < nums[tail]:
                  out[i] = nums[tail]
                  break
               else:
                  tail += 1
            
            # while (head!=tail):
            #     if nums[head]<nums[tail]:
            #         out[i]=nums[tail]
            #         head=(head+1) % len(nums)
            #         tail=(tail+1) % len(nums)
            #         break
            #     else:
            #         tail=(tail+1) % len(nums)
            # if head==tail:
            #     head=(head+1)%len(nums)
            #     tail=(tail+2)%len(nums)
            #     if nums.index(i) == len(nums)-1:
            #       tail = 0
                
        return out
    #Timecomplexity O(n**2)
    #Spacecomplexity O(n)
