// require('dotenv').config();
// const ethers = require('ethers');

// // Get Alchemy API Key
// const API_KEY = process.env.API_KEY;

// // Define an Alchemy Provider
// // const provider = new AlchemyProvider("sepolia", API_KEY);

// const provider = ethers.getDefaultProvider("sepolia", {
//     alchemy: process.env.API_URL,
// });


// const contract = require("../artifacts/contracts/MyNFT.sol/MyNFT.json");

// // console.log(JSON.stringify(contract.abi));

// const privateKey = process.env.PRIVATE_KEY;
// const signer = new ethers.Wallet(privateKey, provider);

// // Get contract ABI and address
// const abi = contract.abi;
// const contractAddress = process.env.CONTRACT_ADDRESS;

// // Create a contract instance
// const myNftContract = new ethers.Contract(contractAddress, abi, signer);

// const tokenUri = "https://gateway.pinata.cloud/ipfs/QmWNQHtfUeSHfr4LTz7hp9c1RhG7dLLSdPQ58ZyndHADWA";

// // Call mintNFT function
// const mintNFT = async () => {
//     let nftTxn = await myNftContract.mintNFT(process.env.PUBLIC_KEY, tokenUri);
//     await nftTxn.wait();
//     console.log(`NFT Minted! Check it out at: https://sepolia.etherscan.io/tx/${nftTxn.hash}`);
// }

// mintNFT()
//     .then(() => process.exit(0))
//     .catch((error) => {
//         console.error(error);
//         process.exit(1);
//     });

require("dotenv").config();
const API_URL = process.env.API_URL;
const PUBLIC_KEY = process.env.PUBLIC_KEY;
   const PRIVATE_KEY = process.env.PRIVATE_KEY;

const { createAlchemyWeb3 } = require("@alch/alchemy-web3");

const web3 = createAlchemyWeb3(API_URL);

const contract = require("../artifacts/contracts/MyNFT.sol/MyNFT.json");

// console.log(JSON.stringify(contract.abi));

const nftContract = new web3.eth.Contract(contract.abi, process.env.CONTRACT_ADDRESS);

async function mintNFT(tokenURI) {
    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce

  //the transaction
    const tx = {
      'from': PUBLIC_KEY,
      'to': process.env.CONTRACT_ADDRESS,
      'nonce': nonce,
      'gas': 500000,
      'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
    };

    const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY)
  signPromise
    .then((signedTx) => {
      web3.eth.sendSignedTransaction(
        signedTx.rawTransaction,
        function (err, hash) {
          if (!err) {
            console.log(
              "The hash of your transaction is: ",
              hash,
              "\nCheck Alchemy's Mempool to view the status of your transaction!"
            )
          } else {
            console.log(
              "Something went wrong when submitting your transaction:",
              err
            )
          }
        }
      )
    })
    .catch((err) => {
      console.log(" Promise failed:", err)
    });
  }

  mintNFT("https://gateway.pinata.cloud/ipfs/QmR1BPQKANreucYVYT6rBcfEGdWpnogAExquyKCiyzzppC");
