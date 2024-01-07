const fs = require('fs')
console.log("Day 2")

const file = process.argv[2]
console.log(file)

const getGameInfo = (game )=>{
  //get the Id
  [id, data] = game.split(':')
  id = id.slice(5)
  // console.log("id", id)

  data = data.split(';')
  let rounds = []

  data.forEach(element => {
    let plays = element.split(',');
    let round = {}
    plays.forEach(play=>{
      play = play.split(' ').slice(1);
      // console.log(play)
      round[play[1]]= parseInt(play[0])
    })
    rounds.push(round)
  });
  // console.log(rounds)

  return { id, rounds}
}

const isTheGamePossible = (dices, gameInfo) =>{
  tmp = gameInfo.rounds.map(game=>{
    if(game.red > dices.red) return 0
    if( game.green > dices.green) return 0
    if( game.blue > dices.blue) return 0
    return 1

  })
  // console.log(tmp)
  // console.log()
  if(tmp.includes(0)) return 0

  return parseInt(gameInfo.id) 
}

const getMaxDices = (gameInfo) =>{
  // console.log(gameInfo.rounds)
  let maxBlue = 0 
  let maxRed = 0 
  let maxGreen = 0 

  gameInfo.rounds.forEach(x=>{
    if(x['blue'] > maxBlue) maxBlue = x['blue']
    if(x['green'] > maxGreen) maxGreen = x['green']
    if(x['red'] > maxRed) maxRed= x['red']
  })

  return {maxBlue: parseInt(maxBlue), maxRed: parseInt(maxRed), maxGreen: parseInt(maxGreen)}
}

const getPower = (maxDices) =>{
  let power = 1 
  for(let x in maxDices){
    // console.log(maxDices[x])
    power *= maxDices[x]
    // console.log(power)
  }

  return power
}


// Read the file data to get the data
fs.readFile(file,'utf-8',(err, data)=>{
  if(err){
    console.error(err)
  }
  const lines = data.split('\n')

  //This information was given in the site:
  const dicesAvalible={blue:14, green:13,red:12}
  let possibleGames =[]

  lines.forEach(line=>{
    if(line!==""){
      gameInfo = getGameInfo(line)
      possibleGames.push(isTheGamePossible(dicesAvalible, gameInfo))
    }
  })
  const answerPart1 = possibleGames.reduce((prev, acc)=> prev +acc)
  console.log("The answer for part 1 the question is: ",answerPart1)


  let answerPart2 = 0 
  lines.forEach(line=>{
    if(line !=""){
      // console.log(line)
      let game = getGameInfo(line)
      // console.log(game)
      let max = getMaxDices(game)
      // console.log(max)
      let power = getPower(max) 
      // console.log(power)
      answerPart2 += power
      // console.log('\n---------------------------\n')
    }
  })
  console.log("The answer for the part 2 is: ",answerPart2)

})


