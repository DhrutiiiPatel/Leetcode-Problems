class Solution:
    def minimumRecolors(self, blocks, k):
        n=len(blocks)
        recolor=W=blocks[:k].count('W')
        for l in range(n-k):
            W+=(blocks[l+k]=='W')-(blocks[l]=='W')
            recolor=min(recolor, W)
        return recolor
        
