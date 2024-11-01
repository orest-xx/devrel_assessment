import base64
import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algosdk.transaction import PaymentTxn
from algokit_utils import (
    TransactionParameters
)
from algosdk.atomic_transaction_composer import (
    AccountTransactionSigner,
    TransactionWithSigner,
)


logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.devrel_assessment.devrel_assessment_client import (
        DevrelAssessmentClient,
    )

    app_client = DevrelAssessmentClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    # Box name, could be replaced with account.address
    val = b"B"
    # App account topup amount in microAlgo
    amt = 1000_000

    # Construct payment transaction to fund the app account
    ptxn = PaymentTxn(
        sender=deployer.address,
        sp=algod_client.suggested_params(),
        receiver=app_client.app_address,
        amt=amt,
    )

    # Fund the app account
    app_client.fund_account(
        payment=TransactionWithSigner(ptxn, AccountTransactionSigner(deployer.private_key)),
        transaction_parameters=TransactionParameters(boxes=[(app_client.app_id, val)]),
    )
   
    # Define dev name
    name = "Orest Gaboda"

    # Concat greetings
    response = app_client.hello(name=name,
        transaction_parameters=algokit_utils.TransactionParameters(
        boxes=[(app_client.app_id, val)] 
    ),)

    # Store the response in the box
    app_client.box_put(response=response.return_value,
        transaction_parameters=algokit_utils.TransactionParameters(
        boxes=[(app_client.app_id, val)])
    )

    logger.info(
        f"Called hello on {app_spec.contract.name} ({app_client.app_id}) "
        f"with name={name}, received: {response.return_value} and put it in a Box with name {val.decode('utf-8')}. " 
        f"App account was funded for {amt} microAlgos from deployer account"
    )
