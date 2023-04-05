// 호이스팅(Hoisting)
hello();

function hello() {
    console.log("Hello World");
}

// 구조 분해 할당(Destructuring assignment)
const user = {
    name: 'emhaki',
    age: 20
}

function getName({name}) {
    const { name } = user;
    return name;
}

function getEmail({email = '이메일이 없습니다.'}) {
    return email;
}

console.log(getName(user)); // 'emhaki'
console.log(getEmail(user)); // '이메일이 없습니다.'

// 나머지 매개변수(Rest parameters)
function sum(...rest) {
    console.log(rest);
    return rest.reduce(function(acc, cur) {
        return acc + cur;
    }, 0)
}

// 화살표 함수(Arrow functions)
const sum = function() {}
const sum = () => {}
function sum(a, b) {
    return a + b;
}
const sum = (a, b) => a + b;

// 콜백(Callback)
const a = callback => {
    callback()
    console.log('A')
}

const b = () => {
    console.log('B')
}
a(b)

// 재귀(Recursive function)
let i = 0
const aa = () => {
    console.log('A')
    i += 1
    if (i < 4) {
        aa();
    }
}

const userA = { name: 'A', parent: null }
const userB = { name: 'B', parent: userA }
const userC = { name: 'C', parent: userB }
const userD = { name: 'D', parent: userC }

const getRoottUser = (user) => {
    if (user.parent) {
        return getRoottUser(user.parent)
    }
    return user
}

console.log(getRoottUser(userD)) // userA 객체

// this
// 일반 함수의 this는 호출 위치에서 정의
const userK = {
    firstName: 'Myeonghak',
    lastName:'Lee',
    age: 20,
    getFullName: function() {
        return `${this.firstName} ${this.lastName}`
    }
}

console.log(userK.getFullName()) //'Myeonghak Lee'

// 화살표 함수의 this는 자신이 선언된 함수 범위에서 정의
function user() {
    this.firstName = 'Neo',
    this.lastName = 'anda'

    return {
        firstName: 'Myeonghak',
        lastName:'Lee',
        age: 20,
        getFullName: () => {
            return `${this.firstName} ${this.lastName}`
        }
    }
}

const u = user()
console.log(u.getFullName()) //'Neo anda'

/// 화살표 함수의 this는 자신이 선언된 함수(멕시컬) 범위에서 정의 
const timer = {
    title: 'Timer',
    timeout: function () {
        console.log(this.title)
        setTimeout(() => {
            console.log(this.title)
        }, 1000)
    }
}
timer.timeout() // Timer

// .indexof() 일치하는 첫 번째 인덱스 반환, 없으면 -1 반환
var str = 'Hello World'
console.log(str.indexOf('world')) // 6
console.log(str.indexOf('MH')) // -1

if (!str.includes('MH')) {
    console.log('not found')
}

// .padEnd() 대상 문자의 길이(length)가 지정된 길이보다 작으면
// 주어진 문자를 지정된 길이까지 끝에 붙여 새로운 문자를 반환
var str = '12345'
console.log(str.padEnd(8, '0')) // 12345000
console.log(str.padEnd(10, '!')) // 12345!!!!!
console.log(str.padStart(10, '!')) //!!!!!12345

// .replace()
// 대상 문자에서 메인(문자, 정규식)과 일치하는 부분을 교체한 새로운 문자를 반환.

var str = 'Hello, Hello?!'
console.log(str.replace('Hello', 'Hi')) // Hello, Hi!
console.log(str.replace(/Hello/g, 'Hi')) // Hi, Hi?!

// .slice()
// 대상 문자의 일부를 추출해 새로운 문자를 반환
var str = 'Hello world!'
console.log(str.slice(0, 5)) // Hello
console.log(str.slice(6, -1)) // world
console.log(str.slice(6)) // world!
console.log(str) // Hello wolrd!

//.split()
// 대상 문자를 주어진 구분자로 나눠 배열로 반환
var str = 'Apple, Banana, Pear'
console.log(str.split(', ')) // ['Apple', 'Banana', 'Pear']
console.log(str.split('').reverse().join('')) // reaP, ananaB, elppA

// .toFixed()
// 숫자를 지정된 고정 소수점 표기까지 표현하는 `문자로 반환`
var num = 3.141592
console.log(num.toFixed(2)) // 3.14 // string
console.log(parseFloat(num.toFixed(2))) // 3.14 // number 

// .toLocaleString()
// 숫자를 현지 언어 형식의 문자로 반환
var num = 1000000
console.log(nuu.toLocaleString()) // 1,000,000
console.log(`${nuu.toLocaleString()}원`) // 1,000,000원

// Number.parseInt() 또는 parseInt()
// 주어진 값(숫자, 문자)을 파싱해 특정 진수의 형태로 반환
var num = 3.14
console.log(Number.parseInt(num, 10)) // 3

// .at()
// 대상 배열을 인덱싱한다.
// 음수 값을 사용하면 뒤에서부터 인덱싱
var arr = ['a', 'b', 'c']
console.log(arr.at(0)) // a
console.log(arr.at(-1)) // c

// .concat()
// 대상 배열과 주어진 배열을 병합해 새로운 배열을 반환
var arr1 = ['a', 'b', 'c']
var arr2 = ['d', 'e', 'f']
var arr3 = arr1.concat(arr2)
var arr4 = [...arr1, ...arr2] 
console.log(arr3) // ['a', 'b', 'c', 'd', 'e', 'f']
console.log(arr4) // ['a', 'b', 'c', 'd', 'e', 'f']

// .every()
// 대상 배열의 모든 요소가 콜백 테스트에서 참을 반환하는지 확인
var arr = [1, 2, 3, 4]
var isValid = arr.every(item => item < 5)
console.log(isValid) // true

// .filter()
// 주어진 콜백 테스트를 통과하는 모든 요소를 새로운 배열로 반환
// 모든 요소가 테스트를 통과하지 못하면 빈 배열을 반환
var numbers = [1, 2, 3, 4, 31]
var filteredNumbers = numbers.filter(number => number < 30)
console.log(filteredNumbers) // [1 ,2, 3, 4]

var users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]
var adults = users.filter(user => user.age >= 19
)
console.log(adults) // [{ name: 'Myeonghak', age: 20 }]

// .find()
// 대상 배열에서 콜백 테스트를 통과하는 첫 번째 요소를 반환
var arr = [1, 2, 3, 4]
var foundItem = arr.find(item => item > 2)
console.log(foundItem) // 3

var users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]
var foundUser = users.find(user => user.name === 'Myeonghak')
console.log(foundUser) // { name: 'Myeonghak', age: 10 }

// .findIndex()
// 대상 배열에서 콜백 테스트를 통과하는 첫 번째 요소의 인덱스 번호를 반환
var arr = [1, 2, 3, 4]
var index = arr.findIndex(item => item > 2)
console.log(index) // 2

// .flat()
// 대상 배열의 모든 하위 배열을 지정한 깊이(Depth)까지 이어붙인 새로운 배열을 생성
// 깊이의 기본값은 1
var arr = [1, 2, [3, 4, [5, 6]]]
console.log(arr.flat()) // [1, 2, 3, 4, [5, 6]]
console.log(arr.flat(2)) // [1, 2, 3, 4, 5, 6]
console.log(arr.flat(Infinity)) // [1, 2, 3, 4, 5, 6]

// .forEach()
// 대상 배열의 길이만큼 주어진 콜백을 실행
var arr = [1, 2, 3, 4]
arr.forEach(item => console.log(item)) // 1 2 3 4

for (let i = 0; i < arr.length; i += 1) {
    console.log(arr[i]) // 1 2 3 4
}

// .includes()
// 대상 배열이 특정 요소를 포함하고 있는지 확인
var arr = [1, 2, 3, 4]
console.log(arr.includes(3)) // true
console.log(arr.includes(5)) // false

var users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]
console.log(users.includes({ name: 'Myeonghak', age: 10 })) // false (참조형임)
var neo = users[0]
console.log(users.includes(neo)) // true


