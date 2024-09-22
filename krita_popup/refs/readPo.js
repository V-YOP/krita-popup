const { readFileSync } = require('fs')
const process = require('process')
let [,,...texts] = process.argv

texts = ['Selection', 'Action']

if (texts.length === 0) {
    console.error('No text given')
    process.exit(1)
}

process.chdir(__dirname)

const po = JSON.parse(readFileSync('krita.po.json', 'utf-8'))


for (const {c, en, zh} of po) {
    if (zh.length > 100) {
        continue
    }
    for (const text of texts) {
        if (!en.includes(text) && !zh.includes(text)) {
            continue
        }
        if (c) {
            console.log(`Krita.instance().krita_i18nc("${c}", "${en}") # ${zh}`)
        } else {
            console.log(`Krita.instance().krita_i18n("${en}")  #  ${zh}`)
        }
    }
}