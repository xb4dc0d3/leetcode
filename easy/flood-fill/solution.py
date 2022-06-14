class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
      
        # 8 possibility of each adjacent
        row = [-1, -1, -1, 0, 0, 1, 1, 1]
        col = [-1, 0, 1, 0, 0, 0, -1, 0, 1]
        
        def isSafe(image, sr, sc, newColor):
            return 0 <= sr < len(image) and 0 <= sc < len(image) and image[sr][sc] == newColor
        
        # base case
        if not image or not len(image):
            return 
        
        target = image[sr][sc] # processed
        
        if target == newColor:
            return
        
        image[sr][sc] = newColor
        
        
        for k in range(len(row)):
            if isSafe(image, row[k]+sr, col[k]+sc, target):
                self.floodFill(image, row[k]+sr, col[k]+sc, newColor)
                

        return image
