if (process.argv.length <= 2) {
  console.log("USAGE: " + __filename + " hostname.com")
  process.exit(-1)
}

const hostname = process.argv[2]

console.log(`Checking IP of: ${hostname}`)

const dns = require('dns');

const hostnameLookup = (hostname) => {
  dns.lookup(hostname, (err, addresses, family) => {
    console.log(addresses);
  });
}

if (process.argv.length <= 2) {
  console.log("USAGE: " + __filename + " IPADDR")
  process.exit(-1)
}

console.log(`Checking IP of: ${hostname}`)

hostnameLookup(hostname);

process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', (data) => {
  console.log("Hello " + data.toString())
  process.exit()
});

process.on('exit', () => {
  console.log('Thanks for the info!')
});