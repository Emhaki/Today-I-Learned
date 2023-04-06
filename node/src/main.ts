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
    age: number
    isValid: boolean
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
