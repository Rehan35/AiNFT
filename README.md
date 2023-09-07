# AiNFT
After using midjourney API to generate an image, I use Pinata as my IPFS service to store the image on a blockchain service. I then use the deploy nft script and mint nft to deploy the contract then mint the nft.

# How to run
py main.py (This will generate the url link for the midjourney image with the prompt you used to generate.)\
py view-image.py (Paste the url link into the view-image.py variable which takes the link and this script will display the image based on the url)\

From here, you will have to use Pinata, or another ipfs service to store your image on a node in the blockchain.\
Once you do so, you can run the script to mint an nft.\

node deploy.js (This will run the script to deploy the contract. It will create an address for the token, Save this Adress for the mint script)\
node mint-nft.js (This will deploy the NFT to the ethereum blockchain. Right now, it will deploy to the Sepolia Testnet, but you can change the location of deployement in the code.)


# Notes
view-image.py and main.py allow Midjourney AI Art generation.
Follow this medium post for a more detailed instruction: https://medium.com/pinata/how-to-build-an-app-nft-7c57b51698e7



