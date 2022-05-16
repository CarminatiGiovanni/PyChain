import React, {useState, createContext, useEffect} from "react";
import './style/css/app.css'

import ServerAddress from './pages/server_address';
import Blockchain from './pages/Blockchain'
import {Tabs,Tab} from 'react-bootstrap'
import TransactionTab from './pages/TransactionTab'
import PoolPendingTransactionTab from './pages/PoolPendingTransactionTab'

import { BlockchainJSONInterface } from "./classes";

type TypeBlockchainContext = {blockchain: BlockchainJSONInterface | null, setBlockchain: React.Dispatch<React.SetStateAction<BlockchainJSONInterface>> | null}

export const BlockchainContext = createContext<TypeBlockchainContext>({blockchain: null, setBlockchain: null})

export const App = (props: any) => {

  const [blockchain,setBlockchain] = useState<BlockchainJSONInterface>({blockchain: [],address:''})

  return (
    <BlockchainContext.Provider value={{blockchain,setBlockchain}}>
      <ServerAddress />

      <Tabs defaultActiveKey="Blockchain" id="uncontrolled-tab-example" className="mb-3">
        <Tab eventKey="Blockchain" title="Blockchain">
          <Blockchain /> 
        </Tab>
        <Tab eventKey="Transaction" title="Transaction">
          <TransactionTab/>
        </Tab>
        <Tab eventKey="Pending Transaction" title="Pending Transaction">
          <PoolPendingTransactionTab/>
        </Tab>
      </Tabs>
    </BlockchainContext.Provider>
  );
}