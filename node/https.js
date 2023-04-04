const request = require('./request');
const response = require('./response');

function makeRequest(url, data) {
    // 요청을 보내기
    request.send(url, data);
    // 데이터 return 하기
    return response.read();
}

const responseData = makeRequest('https://naver.com', 'any data');
console.log(responseData)