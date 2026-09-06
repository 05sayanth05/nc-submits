class TimeMap:

    def __init__(self):
        self.__data: dict[str, list[tuple[int, str]]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.__data:
            self.__data[key] = []

        self.__data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.__data.get(key)
        if not vals:
            return ""
        
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            tm = vals[mid][0]

            if tm <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
