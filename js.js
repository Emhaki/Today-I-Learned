function fetchData() {
    return new Promise((resolve, reject) => {
        // 비동기 요청
        const sucess = true;
        if(sucess) {
            resolve('success');
        } else {
            reject('fail');
        }
    })
}

fetchData()
    .then((response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log(error);
    })

fetchData()

async function makeRequest() {
    try {
        const response1 = await fetchData('https://jsonplaceholder.typicode.com/posts/1');
        const jsonResponse1 = await response1.json();
        console.log(jsonResponse1);
    } catch (error) {
        console.log(error);
    } finally {
        console.log('---모든 작업 끝---')
    }
}

makeRequest();