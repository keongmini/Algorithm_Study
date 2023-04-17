#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin>>n;

    int result = -2147000000;
    int idx = -1;

    for(int i=0; i<n; i++){
        vector<int> nums;
        
        for(int j=0; j<5; j++){
            int tmp;
            cin>>tmp;
            nums.push_back(tmp);
        }

        int maxNum = -2147000000;

        for(int j=0; j<5; j++){
            for(int k=j+1; k<5; k++){
                for(int s = k+1; s<5; s++){
                    maxNum = max(maxNum, (nums[j] + nums[k] + nums[s]) % 10);
                }
            }
        }
        
        if(maxNum > result){
            idx = i + 1;
            result = maxNum;
        }else if(maxNum == result){
            idx = max(idx, i + 1);
        }

    }

    cout<<idx;

    return 0;
}