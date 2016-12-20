#! /usr/local/bin/node

var fs = require('fs');
var sleep = require('sleep').sleep;

var start = 420285
// el ultimo bloque es ~436031

request = require('request');
var f = function(i) {
  return function(callback) {
    var options = {
      uri: 'http://blockchain.info/block-height/'+i+'?format=json'
    }
    var stream = request(options);

    console.log(i);
    stream.once('data', function(data) {
      var head = data.toString().substr(0,99);
      head = head + "}]}"
      head = JSON.parse(head)
      var id = head.blocks[0].hash;
      console.log(id);
      if(id.indexOf('0000000000000000001d07076713514505') > -1) {
        console.log('found!')
        console.log(id);
        process.exit(); 
      }
      callback();
      
    })
  };
}
var async = require('async')
var g = function(i) {
  async.parallel([
    f(i),
    f(i+1),
    f(i+2),
    f(i+3),
    f(i+4)
  ], function(err, results) {
    g(i+5);
  });
}

g(start);
