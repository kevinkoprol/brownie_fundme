from brownie import accounts, config, network, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    if len(MockV3Aggregator) <= 0:  # dus als er nog geen instance van is
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
    print("Mocks deployed!")
