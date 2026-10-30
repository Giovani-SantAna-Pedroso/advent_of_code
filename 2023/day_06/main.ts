const fs = require('node:fs/promises')

console.log("Day 6")

const path_file = process.argv[2] as string

const getFileInfo = async (path: string): =>{
  try{
    const data = await fs.readFile(path, 'utf8')
		const tmp = data.split('\n').slice(0, -1)

		const findNumbers = (text:string) =>{
			const regex = /[0-9]+/g
			const test = [...text.matchAll(regex)]
			const numbers = test.map(number=> parseInt(number[0])) 

			return numbers
		}

		const times = findNumbers(tmp[0])
		const distances = findNumbers(tmp[1])

    return {raw: data, times, distances }
  } catch(err){
    console.error("An error happened", err.message)
    return{data:null}
  }
}

const getPossibleTimes = (time:number, distance:number) =>{
	console.log(`time: ${time}, distance: ${distance}`)
	const delta = (time * time) + (distance * 4)
	const minTime = Math.ceil((- time + Math.sqrt(delta))/2)
	const maxTime = Math.floor((- time - Math.sqrt(delta))/2)
	console.log(delta)
	console.log(minTime)
	console.log(maxTime)
}


const main = async ()=>{
  const fileData = await getFileInfo(path_file)
	const toTest = 2
	getPossibleTimes(fileData.times[toTest], fileData.distances[toTest])
}

main()
