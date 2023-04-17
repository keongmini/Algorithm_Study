#include<iostream>
#include<queue>
using namespace std;

int n, m;
int map[101][101];
int visited[101];

int main(){
    cin>>n;
    cin>>m;

    for(int i=0; i<m; i++){
        int k, v;
        cin>>k>>v;
        
        map[k][v] = 1;
        map[v][k] = 1;
    }

    queue<int> q;
    q.push(1);
    visited[1] = 1;

    int result = 0;

    while(!q.empty()){
        int now = q.front();
        q.pop();

        for(int i=1; i<=n; i++){
            if(map[now][i] == 1 && visited[i] == 0){
                visited[i] = 1;
                result ++;
                q.push(i);
            }
        }
    }

    cout<<result;


    

    return 0;
}