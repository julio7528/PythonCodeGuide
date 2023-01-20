var spawn = require('child_process').spawn;
spawn('notepad.exe', [], {
    detached: true,
    stdio: 'ignore'
}).unref();