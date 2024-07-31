// 프로그래머스 Lv.3 네트워크

#include <string>
#include <vector>

using namespace std;

bool isVisited[201];

void DFS(int start, int n, vector<vector<int>> computers) {
    isVisited[start] = true; // 방문처리
    
    // 해당 컴퓨터에서 존재할 수 있는 모든 컴퓨터의 번호까지
    for(int i = 0; i < n; i++) {
        // 방문하지 않았고, 연결되어있다면
        if (!isVisited[i] && computers[start][i] == 1)
            DFS(i, n, computers); // 해당 컴퓨터로 DFS
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    // 1. 모든 컴퓨터에 대해 방문하지 않았다면 DFS로 방문
    for(int i = 0; i < n; i++) {
        if(!isVisited[i]){
            DFS(i, n, computers);
            answer++; // 네트워크 개수 증가
        }
    }
    
    return answer;
}