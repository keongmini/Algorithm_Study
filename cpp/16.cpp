#include<iostream>
#include<algorithm>
using namespace std;

int a[60], b[60];
int main(){
    char str[100];
    int i;

    cin>>str;
    for(i=0; str[i] != '\0'; i++){
        if(str[i] >= 65 && str[i] <= 90){
            a[str[i] - 64] ++;
        }
        else a[str[i] - 70]++;
    }

    cin>>str;
    for(i=0; str[i] != '\0'; i++){
        if(str[i] >= 65 && str[i] <= 90){
            b[str[i] - 64] ++;
        }
        else b[str[i] - 70]++;
    }

    for(i=1;i<=52;i++){
        if(a[i] != b[i]){
            cout<<"NO\n";
            exit(0);
        }
    }
    cout<<"YES\n";
    
    return 0;
}