from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3

def deploy_fund_me():
    account = get_account()

# If we are on a persistent network link rinkeby, use the associated address
# otherwise deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else: 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address


    # Pass the price feed address to our fundme contract
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()