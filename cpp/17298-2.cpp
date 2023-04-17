#include<iostream>
#include<stack>

using namespace std;
int nums[1000001];
stack<int> st;

int result[1000001];

int main(){
    int n;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>nums[i];
    }

    st.push(0);

    for(int i=1; i<n; i++){
        while(!st.empty() && nums[st.top()] < nums[i]){
            result[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }

    while(!st.empty()){
        result[st.top()] = -1;
        st.pop();
    }

    for(int i=0; i<n; i++){
        cout<<result[i]<<" ";
    }

    return 0;
}