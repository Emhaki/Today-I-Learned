import { send } from './request.mjs';
import { read } from './response.mjs';

function makeRequest(url, data) {
    // 요청을 보내기
    send(url, data);
    // 데이터 return 하기
    return read();
}

const responseData = makeRequest('https://naver.com', 'any data');
console.log(responseData)