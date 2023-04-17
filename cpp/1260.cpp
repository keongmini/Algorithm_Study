#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int n, m, v;
int map[1001][1001];
int visited[1001];

void dfs(int x){
    visited[x] = 1;
    cout<<x<<" ";

    for(int i=1; i<=n; i++){
        if(map[x][i] == 1 && visited[i] == 0){
            dfs(i);
        }
    }
}

int main(){
    cin>>n>>m>>v;

    for(int i=0; i<m; i++){
        int k, v;
        cin>>k>>v;

        map[k][v] = 1;
        map[v][k] = 1;
    }

    dfs(v);

    cout<<"\n";

    fill_n(visited, 1001, 0);
    
    queue<int> q;
    q.push(v);
    visited[v] = 1;
    cout<<v<<" ";

    while(q.size() != 0){
        int now = q.front();
        q.pop();

        for(int i=1; i<=n; i++){
            if(visited[i] == 0 && map[now][i] == 1){
                visited[i] = 1;
                q.push(i);
                cout<<i<<" ";
            }
        }
    }


    return 0;
}