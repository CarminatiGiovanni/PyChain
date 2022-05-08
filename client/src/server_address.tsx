import React, {useState, useEffect, useContext} from "react";
import {ServerAddressContext} from "./App"


type Ciaone = {serverAddress: string | null, setServerAddress: React.Dispatch<React.SetStateAction<string>> | null}

const ServerAddress = (props: any) => {

    const {serverAddress, setServerAddress} = useContext(ServerAddressContext)

    useEffect(() => {
        console.log(serverAddress)
    },[serverAddress])


    function handleSubmit(e: React.MouseEvent<HTMLFormElement>){
        e.preventDefault()

        const url_regex = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}"

        const address = (e.currentTarget.elements.namedItem("server address") as HTMLInputElement).value
        
        if(address.match(url_regex) != null){
            setServerAddress ? setServerAddress(address) : null
        }
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input id="server_address" name="server address" placeholder="Server address:" type="text"/>
        <input id="submit_button" type="submit" placeholder="Save"/>
      </form>
    </div>
  );
}

export default ServerAddress