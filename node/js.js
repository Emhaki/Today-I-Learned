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

// .join()
// 대상 배열의 모든 요소를 구분자로 연결한 문자를 반환
var arr = ['apple', 'banana', 'pear']
console.log(arr.join()) // apple,banana,pear
console.log(arr.join(', ')) // apple, banana, pear
console.elog(arr.join('/')) // apple/banana/pear

// .map()
// 대상 배열의 길이만큼 주어진 콜백을 실행하고, 콜백의 반환 값을 모아 새로운 배열을 반환
var numbers = [1, 2, 3, 4]
var newNumbers = numbers.map(item => item * 2)
console.log(newNumbers) // [2, 4, 6, 8]
console.log(numbers) // [1, 2, 3, 4]

var users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]
// 전개 연산자로 mapping
var newUsers = users.map(user => {
    return {
        ...user,
        isValid: true,
        email: null,
    }
})
console.log(newUsers)

// .pop()
// 대상 배열에서 마지막 요소를 제거하고 그 요소를 반환
// 대상 배열 원본 변경
var fruits = ['apple', 'banana', 'pear']
console.log(fruits.pop()) // 'pear'
console.log(fruits) // ['apple', 'banana']

// .push()
// 대상 배열의 마지막에 하나 이상의 요소를 추가하고, 배열의 새로운 길이를 반환
// 대상 배열 원본 변경
var fruits = ['apple', 'banana', 'pear']
var newLength = fruits.push('peach')
console.log(newLength) // 4
console.log(fruits) // ['apple', 'banana', 'pear', 'peach']
fruits.push('mango', 'strawberry')
console.log(fruits) // ['apple', 'banana', 'pear', 'peach', 'mango', 'strawberry']

// .reduce()
// 대상 배열의 길이만큼 주어진 콜백을 실행하고, 마지막에 호출되는 콜백의 변환 값을 반환
// 각 콜백의 반환 값은 다음 콜백으로 전달
var numbers = [1, 2, 3, 4]
var sum = numbers.reduce((accumulator, currentValue) => 
    {
    accumulator + currentValue
    }, 0)
console.log(sum) // 10

var users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]

// 나이 계산
var totalAge = users.reduce((acc, cur) => acc + cur.age, 0)
console.log(totalAge) // 30

// 모든 이름 추출
var names = users
    .reduce((acc, cur) => {
        acc.push(cur.name)
        return acc
    }, []).join(', ')
console.log(names) // Neo, Myeonghak

// .reverse()
// 배열의 순서를 반전
// 대상 배열 원본이 변경
let arr = [1, 2, 3, 4]
let reversed = arr.resverse()
console.log(reversed) // [4, 3, 2, 1]
console.log(arr) // [4, 3, 2, 1]

// .shift() == popleft()
// 대상 배열에서 첫 번째 요소를 제거, 제거된 요소를 반환
// 대상 배열 원본 변경
let arr = [1, 2, 3, 4]
console.log(arr.shift()) // 1
console.log(arr) // [2, 3, 4]

// .slice()
// 대상 배열의 일부를 추출해 새로운 배열 반환
// 두 번째 인수 직전까지 추출, 두 번째 인수를 생략하면 대상 배열의 끝까지 추출
let arr = ['A', 'B', 'C', 'D']
console.log(arr.slice(0, 2)) // ['A', 'B']
console.log(arr.slice(2, -1)) // ['C']
console.log(arr.slice(2)) // ['D']

// .some()
// 대상 배열의 어떤 요소라도 콜백 테스트를 통과하는지 확인
let arr = [1, 2, 3, 4]
let isValid = arr.some(item => item > 2)
console.log(isValid) // true\

// .sort()
// 대상 배열을 콜백의 반환 값(음수, 양수, 0)에 따라 정렬
// 콜백을 제공하지 않으면, 요소를 문자열로 변환하고 유니코드 코드 포인트 순서로 정렬
// 대상 배열 원본 변경
let numbers = [1, 5, 100, 20]
numbers.sort()
console.log(numbers) // [1, 20, 100, 5]
numbers.sort((a, b) => a - b)
console.log(numbers) // [1, 5, 20, 100]

let users = [
    { name: 'Neo', age: 20 },
    { name: 'Myeonghak', age: 10 },
]

users.sort((a, b) => a.age - b.age)
console.log(users) // 내림차순 나이순으로 정렬

// .splice()
// 대상 배열 요소를 추가하거나 삭제하거나 교체
// 대상 배열 원본이 변경
let arr = [1, 2, 3, 4]
arr.splice(1, 0, 'X') // 삽입위치, 제거수, 삽입할 요소
console.log(arr) // [1, 'X', 2, 3, 4]

// .unshift()
// 새로운 요소를 대상 배열에 맨 앞에 추가하고 새로운 배열의 길이 반환
// 대상 배열 원본이 변경
var arr = [1, 2, 3, 4]
console.log(arr.unshift(5)) // 5
console.log(arr) // [5, 1, 2, 3, 4]

// Array.from()
// 유사 배열을 실제 배열로 반환
var arraylike = {
    0: 'A',
    1: 'B',
    2: 'C',
    length: 3,
}

console.log(arraylike.constructor === Array) // false
console.log(arraylike.constructor === Object) // true // 객체데이터
// arraylike.forEach(item => console.log(item))
Array.from(arraylike).forEach(item => console.log(item))

// Array.isArray()
// 배열 데이터인지 확인
var array = ['A', 'B', 'C']
var arraylike = {
    0: 'A',
    1: 'B',
    2: 'C',
    length: 3,
}

console.log(Array.isArray(array)) // true
console.log(Array.isArray(arraylike)) // false

// Object.assign()
// 하나 이상의 출처(Source) 객체로부터 대상(Target) 객체로 속성을 복사하고 대상 객체를 반환
var target = { a: 1, b: 2 }
var source = { c: 3, d: 4 }
var source2 = { e: 5, f: 6 }
// var result = Object.assign(target, source, source2)
var result = {
    ...target,
    ...source,
    ...source2
}
console.log(target) // { a: 1, b: 3, c: 5, d: 6}
console.log(result) // { a: 1, b: 3, c: 5, d: 6}

// Object.entries()
// 주어진 객체의 각 속성과 값으로 하나의 배열 만들어 요소로 추가한 2차원 배열을 반환
var user = {
    name: 'emhaki',
    age: 20,
    isValid: true,
    email: 'hzdkv@example.com',
}
console.log(Object.entries(user))
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value} 입니다.`)
}

// Object.keys()
// 주어진 객체의 속성 이름을 나열한 배열
console.log(Object.keys(user)) // ['name', 'age', 'isValid', 'email']

// Object.values()
// 주어진 객체의 값을 나열한 배열을 반환
console.log(Object.values(user)) // ['emhaki', 20, true, 'hzdkv@example.com']

// E.dataset
// 요소의 각 data 속성 값을 얻거나 저장
const el = document.querySelector('.child')
const str = 'Hello World'
const obj = { a: 1, b: 2 }

el.dataset.helloWorld = str
el.dataset.object = JSON.stringify(obj) // 문자화

console.log(el.dataset.helloworld)
console.log(el.dataset.object)
console.log(JSON.parse(el.dataset.object))