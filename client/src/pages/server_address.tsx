import React, {useContext, useState, useEffect} from "react";
import {BlockchainContext} from "../App"
import '../style/css/server_address.css'


const ServerAddress = (props: any) => {

    const {setBlockchain} = useContext(BlockchainContext)

    const [serverAddress,setServerAddress] = useState<string>('')
    const [triggerRefresh,setTriggerRefresh] = useState<boolean>(false)

    const refresh = () => {
      if(setBlockchain)
        setBlockchain({blockchain:[], address: serverAddress})
      else return
  
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
  
        fetch(serverAddress,params).then(res => res.json()).then(json => setBlockchain({...json,address: serverAddress})).catch(e => console.log(e))
    }
  
    useEffect(refresh,[serverAddress,triggerRefresh])

    function handleSubmit(e: React.MouseEvent<HTMLFormElement>){
        e.preventDefault()

        const url_regex = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}"

        const address = (e.currentTarget.elements.namedItem("server address") as HTMLInputElement).value
        
        if(address.match(url_regex) != null){
           if (setServerAddress)setServerAddress(address)
        }
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input id="server_address" name="server address" placeholder="Server address:" type="text"/>
        <input id="submit_button" type="submit" value="refresh" className="button-9" onClick={() => {if(setTriggerRefresh)setTriggerRefresh(!triggerRefresh)}}/>
      </form>
    </div>
  );
}

export default ServerAddress