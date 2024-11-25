document.getElementById('helloButton').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/hello', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('responseMessage').innerText = "请求失败";
    });
});
