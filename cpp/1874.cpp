#include<iostream>
#include<stack>
#include<queue>
#include<vector>

using namespace std;

int main(){
    int n;
    cin>>n;

    queue<int> q;
    for(int i=0; i<n; i++){
        int tmp;
        cin>>tmp;
        q.push(tmp);
    }

    stack<int> st;
    vector<char> result;

    for(int i=1; i<=n; i++){
        st.push(i);
        result.push_back('+');

        while(!st.empty() && st.top() == q.front()){
            st.pop();
            q.pop();
            result.push_back('-');
        }
    }

    if(!st.empty() || !q.empty()){
        cout<<"NO\n";
    }else{
        for(int i=0; i<result.size(); i++){
            cout<<result[i]<<'\n';
        }
    }





    return 0;
}