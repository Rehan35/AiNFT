async function main() {
  // Grab the contract factory 
  const MyNFT = await ethers.deployContract("MyNFT");

  // Start deployment, returning a promise that resolves to a contract object
  // await MyNFT.waitForDeployement(); // Instance of the contract 
  console.log("SimpleStorage Contract Address:", await MyNFT.getAddress());
  console.log("Token id: ", await MyNFT.tokenId());
}

main()
 .then(() => process.exit(0))
 .catch(error => {
   console.error(error);
   process.exit(1);
 });