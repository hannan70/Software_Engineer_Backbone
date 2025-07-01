#include <iostream>
#include <vector>
using namespace std;

vector<int> towSum(vector<int>&nums , int target) {

    int i, j;
    int length = nums.size();
    for(i = 0; i < length; i++) {
        for(j = i + 1; j < length; j++) {
            if(nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {};
}



int main() {
     vector<int> nums = {2,7,11,15};
     int target = 95;

     vector<int> result = towSum(nums, target);

     cout << "[" << result[0] << ", " << result[1] << "]" << endl;


    return 0;
}

