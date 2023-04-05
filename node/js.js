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
