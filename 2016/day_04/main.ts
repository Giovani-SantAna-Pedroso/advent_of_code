//aa
import fs from "node:fs";

const filePath = process.argv[2];
const file = Bun.file(filePath);

const lines = (await file.text()).split("\n").slice(0, -1);

const linesInfo = lines.map((line) => {
  const splited = line.slice(0, -1).split("[");
  const sector = splited[0].split("-").findLast(() => true);

  return { name: splited[0], key: splited[1], sector };
});
// console.log(linesInfo);

const checkRoom = (room: { name: string; key: string; sector: string }) => {
  // console.log(room);
  let letters: { letter: string; val: string }[] = [];
  for (let a of room.key) {
    let amountA = 0;
    for (let letter of room.name) amountA += letter == a ? 1 : 0;

    letters.push({ letter: a, val: `${amountA}${a}` });
  }
  console.log(letters);
  letters = letters.sort((x, y) => {
    const [numX, charX] = [parseInt(x.val), x.letter];
    const [numY, charY] = [parseInt(y.val), y.letter];

    if (numY !== numX) return numY - numX; // maior frequência primeiro
    return charX.localeCompare(charY);
  });
  console.log(letters);

  for (let i = 0; i < room.key.length; i++) {
    console.log(room.key[i], letters[i].letter);
    if (room.key[i] != letters[i].letter) {
      console.log(room.key[i], letters[i].letter);
      return 0;
    }
  }

  return parseInt(room.sector);
};

const ansA = linesInfo.reduce((acc, val) => {
  const valRoom = checkRoom(val);
  console.log(valRoom);
  return valRoom + acc;
}, 0);

// console.log("ans A", ansA.reduce((acc, val)));
console.log("ans A", ansA);
