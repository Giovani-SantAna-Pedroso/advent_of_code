const fs = require('node:fs/promises')
console.log("day 4")
// production aa 

const path_file = process.argv[2]

// all the important info of the card such as the raw data 
// the information of each line etc
const getFileInfo = async (path) =>{
  try{
    const data = await fs.readFile(path, 'utf8')
    // console.log(data)
    const lines = data.split('\n').slice(0,-1)
    // console.log(lines)
    return {raw: data, lines: lines }
  } catch(err){
    console.error("An error happened", err.message)
    return{data:null}
  }
}

//This will get the info of the line such as, the card, the winning numbers and the numbers that you have
const getLinesInfo = (line) =>{
  const cardAndNumbers = line.split(':')
  const cardNumber = parseInt(cardAndNumbers[0].split(/\s+/g)[1]);
  const numbers = cardAndNumbers[1].split('|')
  let [winningNumbers, myNumbers] = cardAndNumbers[1].split('|') 

  //convert in a list of numbers
  winningNumbers = winningNumbers.split(/\s+/g).slice(1,-1);
  myNumbers = myNumbers.split(/\s+/g).slice(1)

  winningNumbers = winningNumbers.map(n=> parseInt(n))
  myNumbers = myNumbers.map(n=> parseInt(n))

  let myWinningNumbers = 0
  winningNumbers.forEach(wn =>{
    if (myNumbers.includes(wn)) myWinningNumbers += 1 ;
  })

  

  let points = 0
  if (myWinningNumbers != 0 ) points = 2**(myWinningNumbers - 1) 

  return {cardN: cardNumber, winningNumbers, myNumbers, myWinningNumbers, points}
}
//answer 
const answerPart1 = (lines) =>{
  let ans = 0 
  lines.forEach(line=> ans += line.points)
  console.log(`The answer for the part 1 is ${ans}`)
}

const answerPart2 = (lines) =>{
  let ans =0
  //recursive 
  const recursive = (line) =>{
    ans ++
    // console.log(line)
    const wins = line.myWinningNumbers
    for(let i = wins;i!=0;i--){
      let next = line.cardN +i -1
      // console.log("next", next)
      if(wins!=0) recursive(lines[next] )
      // console.log(ei)
    }

  }

  // x(lines[0])
  lines.forEach(line=>recursive(line))
  console.log(`The answer for the part 2 is ${ans}`)
}


const main = async ()=>{
  const file = await getFileInfo(path_file)
  // console.log(file)
  // const line = getLinesInfo(file.lines[5])
  // console.log(line)
  const linesData = file.lines.map(line=>getLinesInfo(line))

  // console.log(linesData)
  answerPart1(linesData)
  answerPart2(linesData)

}

main()
