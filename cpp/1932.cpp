#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;
vector<vector<int>> nums;

vector<int> results;

void Count(int i, int result){
    if (i == n - 1){
        results.push_back(result);
        cout<<result;
        return;
    }

    for(int x=0; x<=i; x++){
        int result1 = result + nums[i + 1][x];
        int result2 = result + nums[i + 1][x + 1];

        Count(i + 1, result1);
        Count(i + 1, result2);
    }
}

int main(){
    cin>>n;

    for(int i=0; i<n; i++){
        vector<int> now;
        for(int j=0; j<=i; j++){
            int tmp;
            cin>>tmp;
            now.push_back(tmp);
        }
        nums.push_back(now);
    }

    Count(0, nums[0][0]);

    sort(results.begin(), results.end());

    cout<<results[results.size() - 1]<<endl;

    return 0;
}