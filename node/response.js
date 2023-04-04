function decrypt(data) {
    return 'decrypt data';
}

function read() {
    return decrypt('data');
}

console.log('we are in the response module')

module.exports = {
    read,
    decrypt
}