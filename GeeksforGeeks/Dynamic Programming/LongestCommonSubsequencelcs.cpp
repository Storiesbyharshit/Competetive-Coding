int lcs(int x, int y, string s1, string s2){
    
    // your code here
    int dp[x+1][y+1];
    for(int i=0;i<=x;i++) dp[i][0]=0;
    for(int i=0;i<=y;i++) dp[0][i]=0;
    
    if (dp[x][y] != -1)
        return dp[x][y];
        
        
    if (x == 0 || y == 0)
    {dp[x][y] = 0; }
    
    else
    {
        if(s1[x-1]==s2[y-1])
        return dp[x][y]=1+lcs(x-1,y-1,s1,s2);
        else
        return dp[x][y]=max(lcs(x-1,y,s1,s2),lcs(x,y-1,s1,s2));
    }
    
    return dp[x][y];
}
