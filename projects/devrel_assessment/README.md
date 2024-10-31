# DevRel Assessment

### Task

Your starting point is https://developer.algorand.org/docs/get-started/algokit/.

Use AlgoKit to initialize a Python smart contract project named "devrel_assessment" and modify the starter contract’s hello_world method to take the concatenated phrase with your name and put it in box data storage associated with the contract.

Deploy the contract to your Algorand Localnet network on your machine (bonus points for deploying to the public Testnet) and call the application method, passing in your name to the method call, by modifying the Python code in the deploy_config.py file.

The project should be completed entirely in Python, including the deploy script, using Algorand Python (Puya). Please use Lora as your block explorer, which can also be launched from the AlgoKit CLI via `algokit localnet explore`.

If you have questions as you work on the assessment, you are welcome to ask questions in the Algorand Discord at https://discord.gg/algorand.

### Result
Given approach is pretty simple - it takes my name as input and put it a Box, meanwhile topup created application account with 1 algo.
Results running on localnet:
![alt text](<Screenshot 2024-10-31 at 22.48.56.png>)
![alt text](<Screenshot 2024-10-31 at 22.47.17.png>)
Result running on testnet:
App on testnet - https://lora.algokit.io/testnet/application/728220729
Tx - https://lora.algokit.io/testnet/transaction/XNSQ6DENH5ZB7PD4LMTJVYNAQCKRG2FOI3RSHO4CI6DOMZOHXI7Q
