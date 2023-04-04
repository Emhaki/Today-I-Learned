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