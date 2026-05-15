int min(int a, int b) {
    if (a < b) return a;
    return b;
}

int maxArea(int* height, int heightSize) {
    int i = 0,j = heightSize - 1;
    int maxArea = 0;
    int currArea;

    while (i < j) {
        currArea = min(height[i], height[j]) * (j - i);
        if (currArea > maxArea) {
            maxArea = currArea;
        }
        else if (height[i] > height[j]) {
            j--;
        }
        else {
            i++;
        }
    }

    return maxArea;
    
    
}