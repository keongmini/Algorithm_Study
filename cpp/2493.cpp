#include<iostream>
#include<stack>
#include<vector>

using namespace std;

int main(){
    int n;
    cin>>n;

    int nums[500001];

    for(int i=0; i<n; i++){
        cin>>nums[i];
    }

    stack<int> st;

    vector<int> result;

    for(int i=0; i<n; i++){
        int num = nums[i];

        while(!st.empty() && nums[st.top()] < num){
            st.pop();
        }

        if(st.empty()){
            result.push_back(0);
        }else{
            result.push_back(st.top() + 1);
        }

        st.push(i);
    }

    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<" ";
    }

    return 0;
}