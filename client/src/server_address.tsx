import React, {useContext} from "react";
import {ServerAddressContext} from "./App"
import './style/css/server_address.css'


const ServerAddress = (props: any) => {

    const {serverAddress, setServerAddress,triggerRefresh, setTriggerRefresh} = useContext(ServerAddressContext)

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