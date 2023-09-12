#!/usr/bin/node
const file_storage = require('fs');

const file_arguement = file_storage.readFileSync(process.argv[2]).toString();
const storage_arguement = file_storage.readFileSync(process.argv[3]).toString();
file_storage.writeFileSync(process.argv[4], file_arguement + storage_arguement);

