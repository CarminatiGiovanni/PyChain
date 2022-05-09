import {useState, useContext, useEffect} from "react";
import { ServerAddressContext } from "./App";

interface TransactionInterface{
    content_type: string,
    author: string,
    title: string,
    value: string,
    description: string
}

interface BlockInterface{
  index: number,
  hash: string,
  transaction: TransactionInterface[],
  nonce: number,
  prevHash: string,
  timestamp: number
}

interface BlockchainJSONInterface {
  blockchain: BlockInterface[]
}

const DiagnosticTool = (props: any) => {

  const {serverAddress} = useContext(ServerAddressContext)

  const [blockchain,setBlockchain] = useState<BlockchainJSONInterface>({blockchain: []})

  useEffect(() => {
      if(serverAddress === null || serverAddress === '') return

      fetch(serverAddress,{
        method: 'POST',
        mode:'cors',
        headers: {
          'Access-Control-Allow-Origin':'*'
        }
      }).then(res => res.json()).then(json => setBlockchain(json)).catch(e => console.log(e))
  },[serverAddress])

  return (
    <>
        {
          ((blockchain as BlockchainJSONInterface)['blockchain']).map((block: BlockInterface) => {
            return (
              <div key={block.index}>Block</div>
            )
          })
        }
    </>
  );
}

export default DiagnosticTool