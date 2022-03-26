class Solution:
    def frequencySort(self, s):
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        freq_map = {k: v for k, v in sorted(freq_map.items(), key=lambda item: item[1], reverse=True)}
        result = ""
        for key in freq_map.keys():
            result = result + key * freq_map[key]
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.frequencySort('aaaaabbcddeffffffff')
    print(result)
