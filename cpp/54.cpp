#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<char> s;
    char a[50];
    int i;
    cin>>a;

    for(i=0; a[i]!='\0'; i++){
        if(a[i] == '('){
            s.push(a[i]);
        }else{
            if(s.empty()){
                cout<<"NO\n";
                break;
            }else{
                s.pop();
            }
        }
    }

    if(s.empty()){
        cout<<"YES\n";
    }else{
        cout<<"NO\n";
    }

    return 0;
}