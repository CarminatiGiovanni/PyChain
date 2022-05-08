import React, {useState, createContext} from "react";

import ServerAddress from './server_address';
import DiagnosticTool from './DiagnosticTool'

type TypeCreateServerContext = {serverAddress: string | null, setServerAddress: React.Dispatch<React.SetStateAction<string>> | null}

export const ServerAddressContext = createContext<TypeCreateServerContext>({serverAddress: null,setServerAddress: null})

export const App = (props: any) => {

  const [serverAddress,setServerAddress] = useState('')

  return (
    <ServerAddressContext.Provider value={{serverAddress,setServerAddress}}>
      <ServerAddress />
      <DiagnosticTool />
    </ServerAddressContext.Provider>
  );
}