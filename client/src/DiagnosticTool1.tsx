import {useState, useContext, useEffect} from "react";
import { ServerAddressContext } from "./App";
import { BlockchainJSONInterface } from "./classes";
import { Block } from "./components/Block";
import './style/css/server_address.css'
import './style/css/block.css'

const DiagnosticTool1 = (props: any) => {

  const {serverAddress,triggerRefresh} = useContext(ServerAddressContext)

  const [blockchain,setBlockchain] = useState<BlockchainJSONInterface>({blockchain: []})

  const refresh = () => {
    setBlockchain({blockchain:[]})

    if(serverAddress === null || serverAddress === '') return

      let params = {}
      
      if(serverAddress.substring(7,15) === 'localhost' || serverAddress.substring(7,15) === '127.0.0.1'){
        params = {
          method: 'POST',
          mode:'cors',
          headers: {
            'Access-Control-Allow-Origin':'*'
          }
        }
      }else params = {method:'POST'}        

      fetch(serverAddress,params).then(res => res.json()).then(json => setBlockchain(json)).catch(e => console.log(e))
  }

  useEffect(refresh,[serverAddress,triggerRefresh])

  return (
    <>
        <div className="container">
        {
          ((blockchain as BlockchainJSONInterface)['blockchain']).slice().reverse().map((block) => {
            return (
              <Block key={block.index} block = {block}/>
            )
          })
        }
        </div>
    </>
  );
}

export default DiagnosticTool1