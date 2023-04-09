#include <iostream>
using namespace std;
int main(){
    char a[100];
    int result = 0, cnt = 0, i;
    cin>>a;

    for(i = 0; a[i] != '\0'; i++){
        if(a[i] >= 48 && a[i] <= 57){
            result = result * 10 + (a[i] - 48);
        }
    }

    cout<<result<<" ";

    for(i=1;i<=result;i++){
        if(result%i == 0) cnt++;
    }

    cout<<cnt<<"\n";

    return 0;
}