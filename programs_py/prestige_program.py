# prestige_program
# Built with Seahorse v0.1.4
from seahorse.prelude import *


declare_id('Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS')

class PrestigeUser(Account):
    xp_token_account: TokenAccount
    github_id: str ## not an anchor string - seahorse should fix it soon
    username: str ## not an anchor string - '

class CommitType(Enum):
    FIX_TYPO = 0
    FIX_BUG = 1
    FIX_CRITICAL_BUG = 2
    ADD_FEATURE = 3
    ADD_BIG_FEATURE = 4
    MAKE_SMALL_COMMIT = 5
    MAKE_COMMIT = 6
    MAKE_BIG_COMMIT = 7


## initialize a new user
@instruction
def initialize_prestige_user(
prestige_user: Empty[PrestigeUser], 
owner: Signer, 
github_id: str, ## not an anchor string
username: str,
user_xp_token_account: Empty[TokenAccount],
xp_token_mint: Pubkey
):

    prestige_user.init(
        payer = owner,
        seeds = ['prestige_user', owner, github_id]
    )
    user_xp_token_account.init(
        payer = owner,
        seeds = ['xp_token', owner, github_id],
        mint = xp_token_mint
    )
    prestige_user.github_id = github_id
    prestige_user.xp_token_account = user_xp_token_account
    prestige_user.username = username

# ## airdrop an nft badge to a user if he has enough tokens // not done yet
# @instruction
# def aidrop_badge(
# user_xp_token_account: TokenAccount,
# signer: Signer,
# ):
#     assert user_xp_token_account.authority() == signer.key(), 'this feature is not implemented yet'
#     
# ## TODO: discuss if a user should be able to claim their own badge or if it should get aidropped
        

## github commit
@instruction
def github_commit(
user: PrestigeUser,
user_xp_token_account: TokenAccount,
github_id: str, 
dao_xp_token_account: TokenAccount,
amount: u8,
commit_type: CommitType,
signer: Pubkey
):
    assert user.github_id == github_id, 'Github id does not match with on chain account record'
    assert amount == 0, 'Base amount must be 0'

    ## adds XP Token amount depending on the commit type
    if commit_type == CommitType.FIX_TYPO:
      amount += 1
    elif commit_type == CommitType.FIX_BUG:
      amount += 5
    elif commit_type == CommitType.FIX_CRITICAL_BUG:
      amount += 10
    elif commit_type == CommitType.ADD_FEATURE:
      amount += 5
    elif commit_type == CommitType.ADD_BIG_FEATURE:
        amount += 20
    elif commit_type == CommitType.MAKE_SMALL_COMMIT:
        amount += 1
    elif commit_type == CommitType.MAKE_COMMIT:
        amount += 5
    elif commit_type == CommitType.MAKE_BIG_COMMIT:
        amount += 10
  
    ## transfer xp tokens to user who made the commit/issue
    dao_xp_token_account.transfer(
    authority = signer,
    to = user_xp_token_account,
    amount = amount
    )
