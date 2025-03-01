function containsDuplicate(nums: number[]): boolean {
    let set = new Set<number> (nums);
    return (nums.length > set.size);
};