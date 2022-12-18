function maxProfit(prices) {
    const min = Math.min(...prices);
    const min_index = prices.indexOf(min);
    const max = Math.max(...prices.splice(min_index + 1));
    return Math.abs(max) === Infinity ? 0 : Math.abs(max-min);
};