import React, {useState, useContext, useEffect} from "react";
import { ServerAddressContext } from "./App";

const DiagnosticTool = (props: any) => {

  const {serverAddress} = useContext(ServerAddressContext)

  const [blockchain,setBlockchain] = useState({})

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
      <p>
        {JSON.stringify(blockchain)}
      </p>
    </>
  );
}

export default DiagnosticTool