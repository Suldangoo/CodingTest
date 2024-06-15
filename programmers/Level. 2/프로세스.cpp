// 프로그래머스 Lv.2 프로세스

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Process
{
    int idx; // 해당 프로세스의 번호
    int pri; // 해당 프로세스의 우선순위
};

int solution(vector<int> priorities, int location) {
    // 1. Queue를 생성한다.
    queue<Process> p;
    
    for (int i = 0; i < priorities.size(); i++)
    {
        Process process;
        process.idx = i;
        process.pri = priorities[i];
        p.push(process);
    }
    
    int count = 0;
    while (!p.empty())
    {
        // 2. 0번 프로세스를 꺼내고, max 우선순위가 아니라면 큐의 끝에 삽입한다.
        Process process = p.front();
        p.pop();
        
        if (process.pri < *max_element(priorities.begin(), priorities.end()))
            p.push(process);
        else
        {
            // 3. max 우선순위의 프로세스라면, 실행 카운트를 1 쌓고 내가 찾는 프로세스인지 확인한다.
            count++;
            if (process.idx == location)
                break;
            priorities[process.idx] = 0; // 실행했으므로 해당 프로세스 번호의 우선순위 최소화
        }
    }
    
    return count;
}