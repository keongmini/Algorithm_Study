#include<iostream>
using namespace std;

int main(){
    char a[101], b[101];
    int i, p=0;
    cin.getline(a, 101);    // 공백 입력

    for(i=0; a[i]!='\0'; i++){
        if(a[i] != ' '){
            if(a[i]>=65 && a[i]<=90){
                b[p++]=a[i] + 32;
            }
            else b[p++] = a[i];
        }
    }

    b[p]='\0';
    cout<<b<<"\n";

    return 0;
}