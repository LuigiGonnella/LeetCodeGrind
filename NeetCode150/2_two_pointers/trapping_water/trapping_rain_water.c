//! WATER BY LEVEL -->  SUB-OPTIMAL O(N^2 * H)

int trap(int* height, int heightSize) {
    int l, r, currArea;
    int totArea = 0;
    int currMax, prevMax;
    int leftHeight;

    for (int i = 1; i<heightSize-1; i++ ) {
        l = i - 1;
        r = i + 1;
        leftHeight = height[l];
        prevMax = -1;
        while (leftHeight > height[i]) {
            currMax = height[i];
            while (r < heightSize && height[r] < leftHeight) {
                printf("%d\n", height[r]);
                if (height[r] > currMax) {
                    currMax = height[r];
                }
                r ++;
            }

            

            if (r < heightSize && currMax != prevMax) {
                printf("left height at index %d with value %d\n right height at index %d and max inner height with value %d\n", l, leftHeight, r, currMax);
                currArea = (r - 1 - l) * (leftHeight - currMax) ;
                totArea += currArea;
                printf("curr area --> %d\n tot area --> %d\n\n\n", currArea, totArea);
                prevMax = currMax;
            }
            leftHeight--;
            r = i + 1;
        }
    }
    
    return totArea;
}

//! WATER AT EACH INDEX --> OPTIMAL O(N)
//TWO POINTERS SOLUTION

int max(int a , int b) {
    if (a > b) return a;

    return b;
}

int trap(int* height, int heightSize) {
    int l = 0, r = heightSize - 1;
    int left_height, right_height;
    int tot_water = 0;

    left_height = height[l];
    right_height = height[r];
    while (l < r) {
        if (left_height < right_height) {
            l++;
            left_height = max(left_height, height[l]);
            tot_water += (left_height - height[l]);
            
            
        }
        else {
            r--;
            right_height = max(right_height, height[r]);
            tot_water += (right_height - height[r]);
        }

    }

    return tot_water;

}