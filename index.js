#!/usr/bin/env node

const pkg = require('./package.json');

if (process.argv.includes('--version')) {
    console.log(pkg.version);
} else {
    console.log('UXLint — AI-powered UX checker');
    console.log('Coming soon. https://uxlint.dev');
}