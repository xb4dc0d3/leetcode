class Solution:
    
    def isSafe(self, image, sr, sc, newColor):
        return 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == newColor
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        row = [1, -1, 0, 0]
        col = [0, 0, 1, -1]
        
        
        # base case
        if not image or not len(image):
            return image
        
        target = image[sr][sc] # processed
        
        # if target then return the list image
        if target == newColor:
            return image
        
        image[sr][sc] = newColor
        
        
        for k in range(len(row)):
            if self.isSafe(image, row[k]+sr, col[k]+sc, target):
                self.floodFill(image, row[k]+sr, col[k]+sc, newColor)
                
        return image
        
        
