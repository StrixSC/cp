function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const tmp = nums1.concat(nums2);
    tmp.sort((a:number, b:number) => a-b);
    let median = 0;
    const half = Math.floor((tmp.length-1)/2);
    console.log(tmp)
    if(tmp.length % 2 === 0) {
        median = (tmp[half] + tmp[half + 1])/2;
    } else {
        median = tmp[half];
    }
    return median;
};