const fs = require('fs');

let app_config;
app_config = fs.readFileSync('../app-config.json');
app_config = JSON.parse(app_config);

app_config.background - '#333333';
app_confid = JSON.stringify(app_config, null, 4);

fs.writeFileSync('../app-config.json', app_config);