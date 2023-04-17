#include<iostream>
#include<string>
#include<stack>

using namespace std;

int main(){
    int n;
    cin>>n;

    for(int i=0; i<n; i++){
        string str;
        cin>>str;

        stack<char> st;

        string result = "YES";

        for(int j=0; j<str.size(); j++){
            if(str[j] == '('){
                st.push(str[j]);
            }else{
                if(st.empty()){
                    result = "NO";
                    break;
                }else{
                    st.pop();
                }
            }
        }

        if(!st.empty()){
            result = "NO";
        }
        cout<<result<<"\n";
    }

    return 0;
}