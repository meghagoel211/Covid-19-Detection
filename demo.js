let spawn = require('child_process').spawn

let process = spawn('python', ["./main.py", "xray1.jpeg"]);

process.stdout.on('data', function(data){
    console.log("In Js " + data.toString())
    console.log('From Js ' + JSON.parse(data.toString()).data);
});
/*process.stdout.on('error', (err) => {
    console.log(err);
});*/