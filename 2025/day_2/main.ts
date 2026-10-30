console.log("hello => day 2");
console.log();

const file = Bun.file(Bun.argv[2]);
const fileContent = await file.text();
let entries = fileContent.split(",");
entries = entries.map((x) => x.replace("\n", ""));

const invalidID = [];

for (let i of entries) {
  const limits = i.split("-").map((x) => parseInt(x));

  for (let j = limits[0]; j <= limits[1]; j++) {
    console.log(j);
  }
}
