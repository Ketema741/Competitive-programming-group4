class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row, col = len(image), len(image[0])

        for i in range(row):
            left, right = 0, col - 1

            while left <= right:
                image[i][left], image[i][right] = image[i][right]^1, image[i][left]^1
                left += 1
                right -= 1

        return image