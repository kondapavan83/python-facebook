def wiggle_sort(nums):
    for i,v in enumerate(nums):
         if i!=0 and i!=len(nums)-1:
                 if i%2!=0:
                         if nums[i-1]>=nums[i]:
                                 temp=nums[i-1]
                                 nums[i-1]=nums[i]
                                 nums[i]=temp
                         if nums[i]<=nums[i+1]:
                                 temp=nums[i]
                                 nums[i]=nums[i+1]
                                 nums[i+1]=temp
    return(nums)
