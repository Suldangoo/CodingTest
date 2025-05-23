// PCCP 기출문제 9번
// 프로그래머스 Lv.1 지폐 접기

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;
    sort(wallet.begin(), wallet.end());
    
    while (1) {
        sort(bill.begin(), bill.end());
        
        if (bill[0] <= wallet[0] && bill[1] <= wallet[1])
            break;
        
        bill[1] /= 2;
        answer++;
    }
    
    return answer;
}