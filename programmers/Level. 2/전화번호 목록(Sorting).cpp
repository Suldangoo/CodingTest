// 프로그래머스 Lv.2 전화번호 목록
// Sorting / Loop를 활용

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    // 1. phone_book 배열을 sorting한다.
    sort(phone_book.begin(), phone_book.end());
    
    // 2. 1중 loop를 돌며 앞 번호가 뒷 번호의 접두어인지 확인한다.
    for (int i = 0; i < phone_book.size() - 1; i++)
        if (phone_book[i+1].find(phone_book[i]) == 0)
            return false;
    
    // 3. 마지막까지 루프를 돌았지만 없다면, 접두어가 없다는 것이다.
    return true;
}