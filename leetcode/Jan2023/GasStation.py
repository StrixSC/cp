class Solution:
    def canCompleteCircuitNaive(self, gas: list[int], cost: list[int]) -> int:
        station_count = len(gas)
        weights = [gas[i]/cost[i] if cost[i] != 0 else gas[i] for i in range(station_count)]
        res = -1
        tried = 0
        weight_index = weights.index(max(weights))
        while res == -1 and tried < station_count:
            current_index = weight_index
            visited = 0
            remaining_gas = gas[current_index]
            tried += 1
            while visited < station_count:
                remaining_gas -= cost[current_index]
                if remaining_gas < 0:
                    weights[weight_index] = -1000
                    weight_index = weights.index(max(weights))
                    break
                current_index += 1
                visited += 1
                if current_index > station_count  - 1:
                    current_index = 0
                remaining_gas += gas[current_index]

                if visited == station_count:
                    res = weight_index

        return res

    def canCompleteCircuit(self, gas: list[int], cost: list[int]):
        if sum(gas) < sum(cost):
            return -1 
        
        remaining_gas = index = 0
        for i in range(len(gas)):
            remaining_gas += gas[i] - cost[i]
            if remaining_gas < 0:
                remaining_gas = 0
                index = i + 1
        return index 

print(Solution().canCompleteCircuit(gas=[1,2,3,4,5], cost = [3,4,5,1,2]))
print(Solution().canCompleteCircuit(gas=[2,3,4], cost = [3,4,3]))
print(Solution().canCompleteCircuit(gas=[5,8,2,8], cost = [6,5,6,6]))

