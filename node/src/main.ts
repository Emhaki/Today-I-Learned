// 자바스크립트 기반의 정적 타입 문법을 추가한 프로그래밍 언어
// 타입스크립트(정적 타입) - 코드 작성 단계에서 타입 오류 확인!

// 문자
let str: string
let red: string = 'Red'
let green: string = 'Green'
let myColor: string = `My color is ${red}`
let yourColor: string = 'Your color is' + green

// 숫자
let num: number
let intager: number = 6
let float: number = 3.14
let infinity: number = Infinity
let nan: number = NaN

// 불린
let isBoolean: boolean
let isDone: boolean = false

// Null / Undefined
let nul: null
let und: undefined
nul = null
console.log(nul);
console.log(und)

// 배열
const fruits: string[] = ['apple', 'banana', 'cherry']
const numbers: number[] = [1, 2, 3]
const union: (string|number) [] = ['apple', 1, 2, 'banana', 'cherry', 3]
const array: number[] = [1, 2, 3]

// 객체
const abj: object = {}
const arr: object = []
const func: object = function () {}

interface User {
    name: string,
    readonly age: number
    isValid?: boolean
}

const userA: User = {
    name: 'Emhaki',
    age: 20,
    isValid: true
}
const userB: User = {
    name: 'Luna',
    age: 30,
    isValid: false
}

// 함수
const add = function (x: number, y: number): number {
    return x + y
}
const a: number = add(1, 2)

const hello = function (): void {
    console.log('Hello World!');
}
const h: void = hello()

/// Any
let hello2: any = 'Hello World!'
hello2 = 123
hello2 = false
hello2 = null
hello2 = {}
hello2 = []
hello2 = function () {}

// Unkown
const aa: any = 123
const u: unknown = 123
// any는 되지만 unknown 타입은 에러를 반환
const any: any = aa
const boo: boolean = aa
const num2: number = aa
const arr2: string[] = aa
const obj: { x: string, y: number } = aa

// Tuple
const tuple: [string, number, boolean] = ['a', 1, true]
const users: [number, string, boolean] [] = [[1, 'a', true], [2, 'b', false], [3, 'c', true]]

// Void // return 키워드 작성하지 않을 때 반환되는 값
function hello3(msg: string): void {
    console.log(`Hello ${msg}`);
}
const hi: void = hello3('world')

// Never // 사용할 일이 별로 없음
const nev: number[] = []
nev.push(3)

// Union
let union2: (string | number | boolean)
union2 = 'Hello'
union2 = 123
union2 = false

/// Intersection
interface User2 {
    name: string,
    age: number
}
interface Validation {
    isValid: boolean
}
const mh: User2 & Validation = {
    name: 'Emhaki',
    age: 20,
    isValid: true
}

// 타입 단언(Assertion)
// 단언 키워드 - as
// Non-null 단언 연산자 - !

// 1) 요소를 못 찾을 수 있음
// const el = document.querySelector('body') as HTMLBodyElement
// el.textContent = 'Hello World!' 
const el = document.querySelector('body')
if (el) {
    el.textContent = 'Hello World!' 
}

// 2)
function getNumber(x: number | null | undefined) {
    if (x) {
        return Number(x.toFixed(2))
    }
}
getNumber(3.141592)
getNumber(null) // 이 경우 타입에러 발생

// 3)
function getValue(x: string | number, isNumber: boolean) {
    if (isNumber) {
        return Number((x as number).toFixed(2))
    } else {
        return (x as string).toUpperCase()
    }
}
getValue('hello world', false)
getValue(3.141592, true) // 3.14

// 할당 단언
let num4!: number
console.log(num4)
num4 = 123

// 타입 가드(Guards)
function logText(el: Element) {
    console.log(el.textContent)
}

// 요소를 찾지 못하면 null이 나옴 -> if문으로 처리
const h1El = document.querySelector('h1')
if (h1El instanceof HTMLHeadingElement) {
    logText(h1El)
}

function add2(val: string | number | boolean) {
    let res = 'Result => '
    if (typeof val === 'number') {
        res += val.toFixed(2)
    } 
    if (typeof val === 'string') {
        res += val.toUpperCase()
    }
    console.log(res)
}

add2(3.141592) // 3.14
add2('Hello World!') // HELLO WORLD!

// 인터페이스(Interface)
// 선택적 속성 - ?
// 읽기전용 속성 - readonly
interface User {
    name: string
    readonly age: number
    isValid?: boolean
}
const haki: User = {
    name: 'Emhaki',
    age: 20,
    isValid: true
}
const haki2: User = {
    name: 'Luna',
    age: 30,
}

// 인터페이스(Interface)
// 함수 타입 - 호출 시그니처(Call Signature)
interface GetName {
    (message: string): string
}

interface User3 {
    name: string
    age: number
    getName: (message: string) => string
}
const emhaki: User3 = {
    name: 'Emhaki',
    age: 20,
    getName(message: string) {
        console.log(message)
        return this.name
    }
}
emhaki.getName('Hello!')

// 인덱스 시그니처(Index Signature)
// 배열
interface Fruits {
    [item: number]: string
}
const fruits2: Fruits = ['Apple', 'Banana', 'Orange']
console.log(fruits2)
// 0: Apple
// 1: Banana
// 2: Orange

// 객체
interface User4 {
    [key: string]: unknown
    name: string
    age: number
}
const emhaki2: User4 = {
    name: 'Emhaki',
    age: 20
}
emhaki2['isValid'] = true
emhaki2['emails'] = ['emhaki@gmail.com', 'test@gmail.com']
console.log(emhaki2)

// 인터페이스 확장(상속)
interface User6 {
    name: string
    age: number
}
interface User7 extends User6 {
    isValid: boolean
}
// User6는 name, age 2가지 정의
const emahki3: User6 = {
    name: 'Emhaki',
    age: 20
}
// User7은 User6 확장되어 3가지 정의
const emahki4: User7 = {
    name: 'Emhaki',
    age: 20,
    isValid: true
}

// 타입 별칭(Alias)
type TypeA = string
type TypeB = string | number | boolean
type User8 = {
    name: string
    age: number
    isValid: boolean
} | [string, number, boolean]

// 위에 | 를 통해 2가지 방식을 선언했기 때문에 아래 2가지 방법 가능
const UserC: User8 = {
    name: 'Emhaki',
    age: 20,
    isValid: true
}
const UserD: User8 = ['Emhaki', 20, true]
// param이 string이라면, number라면 조건 형성
function someFunction(param: TypeB): TypeA {
    switch (typeof param) {
        case 'string':
            return param.toUpperCase()
        case 'number':
            return param.toFixed(2)
        default:
            return 'Boolean'
    }
}

// 함수 - 명시적 this
interface Cat {
    name: string
    age: number
}
const cat: Cat = {
    name: 'wishkat',
    age: 3
}
// this는 Cat이라는 객체 데이터가 될 것이라고 명시적으로 선언
function hello22(this: Cat, message: string) {
    console.log(`Hello ${this.name}, ${message}`)
}
hello22.call(cat, 'You are pretty awesome') // Hello wishkat, You are pretty awesome

// 함수 - 오버로딩(Overloading)
// 1)
function add4(a: string, b: string) {
    return a + b
}
function add5(a: number, b: number) {
    return a + b
}
add4('hello', 'world~') // 'hello world~'
add5(10, 20) // 30

// 2)
function add6(a: string, b: string): string
function add6(a: number, b: number): number
function add6(a: any, b: any) {
    return a + b
}
add6('hello', 'world~') // 'hello world~
add6(10, 20) // 30

// 클래스
// 접근 제어자(Access Modifiers)
/// public - 어디서나 자유롭게 접근 가능, 클래스 바디에서 생략 가능
/// protected - 나와 파생된 후손 클래스 내에서 접근 가능
/// private - 내 클래스에서만 접근 가능

class UserA {
    // body
    first: string
    last: string
    age: number
    /// public
    // public first: string = ''
    // public last: string = ''
    // public age: number = 0

    /// protected
    // public first: string = ''
    // public last: string = ''
    // public age: number = 0

    /// private
    // public private first: string = ''
    constructor(first: string, last: string, age: number) {
        this.first = first
        this.last = last
        this.age = age
    }
    getAge() {
        return `${this.first} ${this.last} is ${this.age}`
    }
}
class UserB extends UserA {
    getAge() {
        return `${this.first} ${this.last} is ${this.age}`
    }
}
class UserCC extends UserB {
    getAge() {
        return `${this.first} ${this.last} is ${this.age}`
    }
}
const neo = new UserCC('Neo', 'Shinji', 18)
console.log(neo.first)
console.log(neo.last)
console.log(neo.age)