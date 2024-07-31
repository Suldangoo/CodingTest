// 프로그래머스 Lv.2 기능 개발

#include <string>
#include <vector>

using namespace std;

struct Process
{
    int progress;
    int speed;
};

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    // 1. Process 배열 생성
    vector<Process> p;
    
    for (int i = 0; i < progresses.size(); i++) {
        Process process;
        process.progress = progresses[i];
        process.speed = speeds[i];
        p.push_back(process);
    }
    
    // 2. 반복문 안에서 Process의 progress에 speed를 증감
    while (!p.empty()) {
        for (int i = 0; i < p.size(); i++)
            p[i].progress += p[i].speed;
        
        // 3. 가장 앞의 Process의 progress가 100 이상이라면, 앞에서부터 프로세스 종료
        if (p.front().progress >= 100) {
            int count = 0;
            while (!p.empty() && p.front().progress >= 100) {
                p.erase(p.begin());
                count++;
            }
            answer.push_back(count);
        }
    }
    
    return answer;
}