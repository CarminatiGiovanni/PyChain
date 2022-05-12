import React, {useState, createContext} from "react";
import './style/css/app.css'

import ServerAddress from './server_address';
import DiagnosticTool1 from './DiagnosticTool1'

type TypeCreateServerContext = {serverAddress: string | null, setServerAddress: React.Dispatch<React.SetStateAction<string>> | null}

export const ServerAddressContext = createContext<TypeCreateServerContext>({serverAddress: null,setServerAddress: null})

export const App = (props: any) => {

  const [serverAddress,setServerAddress] = useState<string>('')
  const [page, setPage] = useState<string>('Blockchain')

  return (
    <ServerAddressContext.Provider value={{serverAddress,setServerAddress}}>
      <ServerAddress />
      
      <input className="pageSelector" value="Blockchain"   name="page" type="button" onClick={() => setPage('Blockchain')}/>
      <input className="pageSelector" value="Transactions" name="page" type="button" onClick={() => setPage('Transactions')}/>

      {
        page === 'Transactions' ? <p>Transaction</p> : <DiagnosticTool1 /> 
      }
    </ServerAddressContext.Provider>
  );
}