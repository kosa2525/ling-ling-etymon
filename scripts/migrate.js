const fs = require('fs');
const path = require('path');

const appJsPath = path.join(__dirname, '..', 'app.js');
const wordsJsonPath = path.join(__dirname, '..', 'data', 'words.json');

const content = fs.readFileSync(appJsPath, 'utf-8');
const match = content.match(/const WORDS = (\[[\s\S]*?\n\]);/);

if (match) {
    let evalContent = match[1];
    let WORDS;
    try {
        WORDS = eval(evalContent);
    } catch (e) {
        console.error("Failed to eval WORDS:", e);
        process.exit(1);
    }

    const dir = path.dirname(wordsJsonPath);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(wordsJsonPath, JSON.stringify(WORDS, null, 4), 'utf-8');
    console.log("Migration successful. Extracted " + WORDS.length + " words.");
} else {
    console.log("Could not find WORDS array in app.js.");
}
