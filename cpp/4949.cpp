#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main(){
    string str = "";

    while(1){
        getline(cin, str);

        if(str == "."){
            break;
        }

        stack<char> st;
        string answer = "yes";

        for(int i=0; i<str.size(); i++){
            if(str[i] == '(' || str[i] == '['){
                st.push(str[i]);
            }else if(str[i] == ')'){
                if(st.empty() || st.top() != '('){
                    answer = "no";
                    break;
                }else{
                    st.pop();
                }
            }else if(str[i] == ']'){
                if(st.empty() || st.top() != '['){
                    answer = "no";
                    break;
                }else{
                    st.pop();
                }
            }
        }

        if(!st.empty()){
            answer = "no";
        }

        cout<<answer<<endl;

    }


    return 0;
}