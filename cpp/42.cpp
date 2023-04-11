#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int n, m, i, left=0, right, mid, tmp;
    cin>>n>>m;
    right=n-1;
    vector<int> nums;

    for(i=0;i<n;i++){
        cin>>tmp;
        nums.push_back(tmp);        // 동적배열에 데이터 append
    }

    sort(nums.begin(), nums.end());

    while(left<=right){
        mid = (left + right) / 2;

        if(nums[mid] < m){
            left++;
        }else if(nums[mid] > m){
            right--;
        }else{
            cout<<mid+1;
            break;
        }
    }

    return 0;
}