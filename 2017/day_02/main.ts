// Test
console.log("Day 2");
const fileInput = Bun.file(Bun.argv[2]);

const lines = (await fileInput.text()).split("\n").slice(0, -1);
const linesTreated = lines.map((x) => x.split("\t").map((y) => parseInt(y)));
// const linesTreated = lines.map((x) => x.split(" ").map((y) => parseInt(y)));
const linesMinMax = linesTreated.map((x) => ({
  max: Math.max(...x),
  min: Math.min(...x),
}));

console.log(
  "Ans 1:",
  linesMinMax.reduce((acc, crr) => acc + (crr["max"] - crr["min"]), 0),
);

// const line = linesTreated[2];
const divs = [];
for (let line of linesTreated) {
  for (let i = 0; i < line.length; i++) {
    const tmp = [...line];
    tmp.splice(i, 1);
    for (let j of tmp) {
      if (line[i] % j == 0) divs.push(line[i] / j);
    }
  }
}
console.log(
  "Ans 2:",
  divs.reduce((acc, crr) => acc + crr, 0),
);
