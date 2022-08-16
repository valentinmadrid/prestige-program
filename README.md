# prestige-program

On-chain program for managing XP tokens &amp; badges!

## Structure / Ideas

Here is an example on how I would structure the program:

User wallet interactions

- Create Prestige DAO Account:
  This will allow a user to create a Prestige Account: - initiate XP TokenAccount - link GitHub id to PrestigeAccount - submit a name

Dao Wallet Interactions:
(These interactions should be inside of a GitHub action that has an authority that signs the transactions)

- GitHub Issue Resolved:
  This will airdrop XP Tokens to the Wallet associated to the GitHub account depending on what type of Issue has been resolved: - Check if the Github user that made an Issue is the same as in the on chain account - Make Token amount depend on Commit Type(label) - Send XP Token from DAO Vault to user

- NFT Badge
  How would you guys suggest distributing the Badge NFTs?
  Should a User claim their badge or should it get airdropped by the DAO?

## This is just a draft, it's 100% not working correctly yet

Seahorse doesn't have a String Type yet.
