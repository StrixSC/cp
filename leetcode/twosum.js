let twoSum2 = function(nums, target) {
  let sorted = nums.sort((a,b) => a-b);
  console.log(sorted);
  let pointer1 = 0;
  let pointer2 = sorted.length - 1;

  for(let i = 0; i < sorted.length; i++) {
    let sum = sorted[pointer1] + sorted[pointer2];
    console.log(sum)
    if(sum === target)
      return [pointer1, pointer2];
    if(sum > target)
      pointer2--;
    else if(sum < target)
      pointer1++;
  }

  return [];
}

let twoSum = function(nums, target) {
  let map = new Map();
  for(let i = 0; i < nums.length; i++) {
    let mapValue = map.get(target - nums[i]);
    if(mapValue !== undefined)
     return [mapValue, i];
    else
      map.set(nums[i], i);
  }
}

console.log(twoSum([2,7,11,5], 9));
