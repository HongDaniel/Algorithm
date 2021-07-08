function solution(nums) {
    const half = nums.length / 2;
    const set = new Set(nums);
    return half < set.size ? half : set.size;
}
