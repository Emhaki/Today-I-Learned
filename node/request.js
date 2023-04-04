module.exports.A = 1

module.exports.encrypt = function encrypt(data) {
    return 'encrypted data';
}

function send(url, data) {
    const encryptedData = encrypt(data);
    console.log(`${encryptedData} is being sent to ${url}`);
}

module.exports = {
    send,
}