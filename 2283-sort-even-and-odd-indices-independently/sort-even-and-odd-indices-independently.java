class Solution {
    public int[] sortEvenOdd(int[] nums) {
        int n = nums.length;
        // int[] odd = new int[n/2];
        // int[] odd = new int[n/2 +1];
        List<Integer> odd = new ArrayList<>();
        List<Integer> even = new ArrayList<>();

        for(int i = 0; i < n; i++){
            if(i % 2 == 0){
                even.add(nums[i]);
            }
            else{
                odd.add(nums[i]);
            }
        }

        odd.sort(Collections.reverseOrder());
        Collections.sort(even);
        int x=0, y = 0;
        for(int i = 0; i < n; i++){
            if(i%2 == 0){
                nums[i] = even.get(x++);
            }
            else{
                nums[i] = odd.get(y++);
            }
        }
        return nums;

    }
}