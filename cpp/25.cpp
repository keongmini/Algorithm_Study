#include<iostream>
#include<vector>
using namespace std;

int main(){
    int i, j, n;
    cin>>n;
    vector<int> a(n);
    vector<int> b(n);

    for(i=0; i<n; i++){
        cin>>a[i];
    }

    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            if(a[i] < a[j]){
                b[i]++;
            }
        }
        
        cout<<(b[i] + 1)<<" ";
    }



    return 0;
}