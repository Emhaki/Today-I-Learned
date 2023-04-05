// 데이터 타입 확인
console.log(typeof 'Hello' === 'string'); // true
console.log(typeof 123 === 'number'); // true
console.log(typeof false === 'boolean'); // true
console.log(typeof undefined === 'undefined'); // true
console.log(typeof null === 'object'); // true
console.log(typeof [] === 'object'); // true
console.log(typeof {} === 'object'); // true
console.log(typeof function () {} === 'function'); // true

console.log({}.constructor === Array); // true
console.log({}.constructor === Object); // true
console.log(Object.prototype.toString.call(null).slice(8, -1) === 'Null'); // true

console.log(typeof new String('Hello') === 'object'); // true
console.log(typeof new Number(123) === 'object'); // true
console.log(typeof new Boolean(false) === 'object'); // true
console.log(typeof new Undefined() === 'object'); // true
console.log(typeof new Null() === 'object'); // true

function checkType(data) {
    Object.prototype.toString.call(data).slice(8, -1);
}
console.log(checkType(null)); // Null
console.log(checkType(123)); // Number
console.log(checkType(false)); // Boolean
console.log(checkType(undefined) === 'Undefined'); // true

// 할당 (Assignment)
const a = 3
a = a + 3 // 잘못된 표현

let b = 3
b = b + 3 // 옳은 표현
b += 3

// 증감 (Increment/Decrement)
let c = 3
console.log(c++); // 3
console.log(c) // 4 

console.log(c--); // 3
console.log(--c); // 2

// 부정 (Nagative)
console.log(!true); // false
console.log(!false); // true
console.log(!''); // true
console.log(!null)  // true

// 비교 (Comparison)
const d = 1
const e = 3
console.log(d == e); // false
console.log(d != e); // true
console.log(d === e); // false
console.log(d !== e); // ture

// 논리 (Logical)
const f = true
const g = true

// and 연산자
if (f && g) {
    console.log('모두가 참!')
}

// or 연산자
if (f || g) {
    console.log('모두가 참!')
}

// Nullish 병합 연산자
const n = 0
const num2 = n ?? 7
console.log(num2); // 0
console.log(null ?? 1) // 1
console.log(undefined ?? 1) // 1
console.log(null ?? undefined) // undefined
console.log(null ?? 1 ?? 2) // 1
console.log(false ?? 1 ?? 2) // false

// 삼항(Ternary)
console.log(n < 2 ? '참' : '거짓') // 참
function getAlert(message) {
    return message ? message : '메세지가 존재하지 않습니다.'
}
getAlert('안녕하세요~')

// 전개 연산자(spread Operator)
const arr = [1, 2, 3, 4, 5]
const arr2 = [6, 7, 8, 9, 10]

const arr3 = arr.concat(arr2)
console.log(arr3); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 선택적 체이닝(Optional chaining)
const user = undefined
console.log(user?.name) // undefined

const userA = {
    name: 'emhaki',
    age: 20,
    address: {
        city: 'Seoul',
        state: 'Korea'
    }
}

const userB = {
    name: 'Neo',
    age: 20,
}

function getCity(user) {
    // return user.address.city // X
    return user.address?.city || '주소 없음' // O
}
// 선택적 체이닝을 통해 예외사항 처리
console.log(getCity(userA)) // Seoul
console.log(getCity(userB)) // '주소 없음'

// Switch 조건문
function price(fruit) {
    switch (fruit) {
        case 'Apple':
            return 1000
        case 'Orange':
            return 2000
        case 'Banana':
            return 3000
        default:
            return 0
    }
}

// For 반복문
for (let i = 0; i < 10; i++) {
    console.log(i) // 0 1 2 3 4 5 6 7 8 9
}

// For of 반복문
const fruit = ['Apple', 'Orange', 'Banana']

for (let i = 0; i < fruit.length; i++) {
    console.log(fruit[i]) // Apple, Orange, Banana
}

for (const A of fruit) {
    console.log(A) // Apple, Orange, Banana
}

// For in 반복문
const userC = {
    name: 'emhaki',
    age: 20,
}
// 객체 데이터
for (const key in userC) {
    console.log(key)
    console.log(userC[key]) // 20
}

// Do while 반복문
let k = 0
do {
    console.log(k) // 0
    k += 1
} while (k < 4)