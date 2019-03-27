// skillsGen.js
// A framework for simplifying the display and maintenance of skillset information used in resumes, websites, etc.
// Author : Ben Nowak

const ksa = document.querySelector('#ksa-main')


// var treeData;
//
// var oReq = new XMLHttpRequest();
// oReq.onload = reqListener;
// oReq.open("get", "yourFile.txt", true);
// oReq.send();
//
// function reqListener(e) {
//     treeData = JSON.parse(this.responseText);
// }

const pathToFile = '../config/skillset.json';
let skillset;

function jsonStringParse(str){
  output = "";
  let depth = 0;

}

function reqListener() {
  skillset = JSON.parse(this.responseText);
  console.log(skillset);
  ksa.innerHTML = `<pre>${JSON.stringify(skillset, null, '  ')}</pre>`;
}

let reqJSON = new XMLHttpRequest();
reqJSON.addEventListener("load", reqListener);
reqJSON.open('GET',pathToFile);
reqJSON.send();
