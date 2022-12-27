class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        res.append(celsius + 273.15)
        res.append(celsius * 1.80 + 32.00)
        return res
        