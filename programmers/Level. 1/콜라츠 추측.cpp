// 프로그래머스 Lv.1 콜라츠 추측

#include <string>
#include <vector>

using namespace std;


int solution(int num) {
    int count = 0;
    
    while (count < 500) {
        if (num == 1)
            return count;
        else if (num % 2 == 0)
            num /= 2;
        else
            num = num * 3 + 1;
        
        count++;
    }
    
    return -1;
}