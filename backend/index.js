const express = require('express');
const app = express(); 
const port = 3000; // public open port 
const fs = require('fs') // filesystem stuff
const { parse } = require('csv-parse'); // parse csv

app.get('/', (req, res) => {
    res.send('test') 
})

app.get('/csv/region/:region', (req, res) => {
    const region = req.params.region // get the region from the URL 
    // to get US data visit: localhost:3000/csv/region/us
    // to get UK data visit: localhost:3000/csv/region/gb
    const csvData = [] // each row gets pushed to this array forming the CSV in data format 
    fs.createReadStream(`./${region}.csv`) // load up the path to csv, this can be dynamic later
        .pipe(parse({ delimiter: ",", from_line: 2})) // delimiter is what separates the columns, from_line is the line that the data begins from, 2 means we skip the title row
        .on("data", (row) => {
            console.log(`...gathering region: ${region}...`) // gathering is printed each time the stream gathers a row
            csvData.push(row) // row gets pushed to csvData array 
        })
        .on("end", () => {
            console.log('finished parsing csv file') // end event sent meaning stop parsing stream
            const readableCSV = JSON.parse(JSON.stringify(csvData)) // convert csvData array to JSON so its readable in the browser (for later frontend use)
            console.log('csvDataArray: ', csvData) // data as array
            console.log('readableCSV: ', readableCSV) // data as JSON
            res.json(readableCSV) // Send JSON response to client
        })
        .on("error", (err) => {
            console.log('err: ', err.message) 
        })
})

app.listen(port, () => {
    console.log(`CSV backend listening at http://localhost:${port}`)
})