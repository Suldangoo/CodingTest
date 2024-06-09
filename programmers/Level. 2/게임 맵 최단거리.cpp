// 프로그래머스 Lv.2 게임 맵 최단거리

#include <vector>
#include <queue>

using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int solution(vector<vector<int>> maps)
{
    int r = maps.size(); // 행의 개수
    int c = maps[0].size(); // 열의 개수
    queue<pair<int, int>> q;
    
    q.push({0, 0});
    maps[0][0] = 1;
    
    while(!q.empty())
    {
        // 1. 큐의 최상단 노드 좌표를 꺼내오기
        int x = q.front().first;
        int y = q.front().second;
        int step = maps[x][y]; // 해당 맵의 발걸음 불러오기
        q.pop();
        
        // 2. 현재 위치에서 네 방향으로 확인
        for(int i = 0; i < 4; i++)
        {
            // 3. 새로운 위치 구하기
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 4. 맵 바깥이라면 무시
            if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                continue;
            // 5. 벽이거나, 이미 지나간 곳인 경우 무시
            if (maps[nx][ny] != 1)
                continue;
            // 6. 해당 방향을 큐에 추가하며 이동횟수 표시
            q.push({nx, ny});
            maps[nx][ny] = step + 1;
        }
    }
    
    if(maps[r-1][c-1] == 1) // 목적지가 1인 상태라면 -1 리턴
        return -1;
    else
        return maps[r-1][c-1];
}