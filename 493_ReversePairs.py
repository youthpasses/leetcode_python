# coding:utf-8
# @makai
# 17/2/21

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, s, e):
    	if s >= e: return 0
    	m = (s + e) / 2
    	cnt = self.mergeSort(nums, s, m) + self.mergeSort(nums, m + 1, e)
    	i = s
    	while i <= m:
    		j = m + 1
    		while j <= e and (nums[i] > nums[j] * 2):
    			j += 1
    		cnt += j - (m + 1)
    		i += 1
    	nums[s : e+1] = sorted(nums[s : e+1])
    	return cnt

print Solution().reversePairs([255139,3480,4835,3140,3734,2078,2259,3780,3625,2149,4672,647,3039,845,265,126,2578,1592,2522,4562,7,4987,4389,3811,1248,3827,1838,5364,1488,4165,4752,2389,2124,3566,1294,3683,4173,4420,977,3859,2627,2339,2782,4584,2925,158,4235,4231,2087,5423,3113,172,2696,265,5072,3542,2372,4532,4362,1837,923,2766,5304,5431,3234,4984,4386,2875,1876,462,3472,1659,4565,1312,666,4207,1681,4753,1228,3379,3391,3211,1211,4894,732,250,2990,5135,3113,531,562,5382,2833,2888,1299,4149,2468,3775,4187,1793,3697,4391,1037,5427,5129,1827,2490,69,2476,412,5384,3951,1379,5143,2263,2251,5244,640,5460,3886,2881,4829,1581,441,3972,3547,2205,355,4281,2472,651,5024,1779,2417])


'''
Python version : TL
Here is JAVA version
'''
'''
public class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length-1);
    }
    private int mergeSort(int[] nums, int s, int e){
        if(s>=e) return 0; 
        int mid = s + (e-s)/2; 
        int cnt = mergeSort(nums, s, mid) + mergeSort(nums, mid+1, e); 
        for(int i = s, j = mid+1; i<=mid; i++){
            while(j<=e && nums[i]/2.0 > nums[j]) j++; 
            cnt += j-(mid+1); 
        }
        Arrays.sort(nums, s, e+1); 
        return cnt; 
    }
}
'''
